from ultralytics import YOLO
import cv2
import numpy as np

# Braille Dictionary (A–Z)
braille_dict = {
    "100000": "A", "101000": "B", "110000": "C", "110100": "D",
    "100100": "E", "111000": "F", "111100": "G", "101100": "H",
    "011000": "I", "011100": "J", "100110": "K", "101110": "L",
    "110110": "M", "110111": "N", "100111": "O", "111110": "P",
    "111111": "Q", "101111": "R", "011110": "S", "011111": "T",
    "100010": "U", "101010": "V", "011101": "W", "110010": "X",
    "110011": "Y", "100011": "Z"
}

# Load model once
model = YOLO("best.pt")

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

def process_braille_image(image_path):
    results = model(image_path)
    if not results or len(results) == 0:
        return "No results found."

    result = results[0]

    if not result.boxes or len(result.boxes) == 0:
        return "No braille dots detected."

    dot_centers = []
    for box in result.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        dot_centers.append((cx, cy))

    dot_centers.sort(key=lambda p: (p[1] // 100, p[0]))
    grouped_cells = [dot_centers[i:i + 6] for i in range(0, len(dot_centers), 6)]

    translated_chars = []
    for cell in grouped_cells:
        pattern = get_braille_binary_from_positions(cell)
        char = braille_dict.get(pattern, "?")
        translated_chars.append(char)

    return "".join(translated_chars)

