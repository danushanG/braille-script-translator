from ultralytics import YOLO
import cv2
import numpy as np
from fpdf import FPDF
import pyttsx3

# --- Load YOLOv8 Model ---
model = YOLO("best.pt")

# --- Load Image ---
image_path = r"C:/Users/Hp/braille_project/braille_sample.jpg"
results = model(image_path)
result = results[0]

# --- Draw Detection Boxes on Image ---
img = cv2.imread(image_path)
dot_centers = []

for box in result.boxes:
    x1, y1, x2, y2 = map(int, box.xyxy[0])
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dot_centers.append((cx, cy))
    # Draw box
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Sort by rows (Y), then by columns (X)
dot_centers.sort(key=lambda p: (p[1] // 100, p[0]))  # assume ~100px line height

# Group into 6-dot Braille cells
grouped_cells = [dot_centers[i:i + 6] for i in range(0, len(dot_centers), 6)]

# --- Braille Dictionary ---
braille_dict = {
    "100000": "A", "101000": "B", "110000": "C", "110100": "D",
    "100100": "E", "111000": "F", "111100": "G", "101100": "H",
    "011000": "I", "011100": "J", "100110": "K", "101110": "L",
    "110110": "M", "110111": "N", "100111": "O", "111110": "P",
    "111111": "Q", "101111": "R", "011110": "S", "011111": "T",
    "100010": "U", "101010": "V", "011101": "W", "110010": "X",
    "110011": "Y", "100011": "Z"
}

# --- Position Mapping Function ---
def get_braille_binary_from_positions(cell):
    braille_bits = ["0"] * 6
    if not cell:
        return "".join(braille_bits)

    xs = [pt[0] for pt in cell]
    x_avg = sum(xs) / len(xs)

    left_col = [pt for pt in cell if pt[0] < x_avg]
    right_col = [pt for pt in cell if pt[0] >= x_avg]

    left_col = sorted(left_col, key=lambda p: p[1])
    right_col = sorted(right_col, key=lambda p: p[1])

    for i, pt in enumerate(left_col):
        if i < 3:
            braille_bits[i] = "1"
    for i, pt in enumerate(right_col):
        if i < 3:
            braille_bits[i + 3] = "1"

    return "".join(braille_bits)

# --- Translation ---
print("\nGrouped Braille Cells:")
for idx, cell in enumerate(grouped_cells):
    print(f"Cell {idx + 1}: {cell}")

print("\nTranslated Text:")
translated_chars = []
for idx, cell in enumerate(grouped_cells):
    pattern = get_braille_binary_from_positions(cell)
    char = braille_dict.get(pattern, "?")
    print(f"Cell {idx + 1}: {pattern} → {char}")
    translated_chars.append(char)

final_output = "".join(translated_chars)
print("\nFinal Decoded Text:", final_output)

# --- Save Output to .txt ---
with open("braille_output.txt", "w", encoding="utf-8") as f:
    f.write("Braille Script Translation\n\n")
    for idx, cell in enumerate(grouped_cells):
        pattern = get_braille_binary_from_positions(cell)
        char = braille_dict.get(pattern, "?")
        f.write(f"Cell {idx + 1}: {pattern} → {char}\n")
    f.write("\nFinal Decoded Text: " + final_output)

# --- Save Output to .pdf ---
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Braille Script Translation", ln=True, align='C')
pdf.ln(10)
for idx, cell in enumerate(grouped_cells):
    pattern = get_braille_binary_from_positions(cell)
    char = braille_dict.get(pattern, "?")
    pdf.cell(200, 10, txt=f"Cell {idx + 1}: {pattern} -> {char}", ln=True)
pdf.ln(5)
pdf.cell(200, 10, txt="Final Decoded Text: " + final_output, ln=True)
pdf.output("braille_output.pdf")

# --- Text to Speech ---
engine = pyttsx3.init()
engine.say("The final translated text is " + final_output)
engine.runAndWait()

# --- Show Image with Boxes ---
cv2.imshow("Detections", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
