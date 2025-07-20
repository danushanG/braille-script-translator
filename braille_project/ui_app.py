import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import subprocess
import os

# Run detection and read output
def run_translation():
    if not image_path.get():
        messagebox.showerror("Error", "Please select a Braille image first.")
        return

    try:
        # Call the detection script
        subprocess.run(["python", "detect_braille.py"], check=True)

        # Read the translated text from .txt file
        with open("braille_output.txt", "r", encoding="utf-8") as f:
            output = f.read()
            output_text.delete("1.0", tk.END)
            output_text.insert(tk.END, output)

        messagebox.showinfo("Success", "Translation complete!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

# File selection
def browse_image():
    file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.jpeg")])
    if file_path:
        image_path.set(file_path)
        img = Image.open(file_path)
        img = img.resize((300, 150))
        img_preview = ImageTk.PhotoImage(img)
        image_label.config(image=img_preview)
        image_label.image = img_preview

        # Update detect_braille.py with new image path
        with open("detect_braille.py", "r", encoding="utf-8") as f:
            lines = f.readlines()
        with open("detect_braille.py", "w", encoding="utf-8") as f:
            for line in lines:
                if line.strip().startswith("image_path ="):
                    f.write(f'image_path = r"{file_path}"\n')
                else:
                    f.write(line)

# GUI setup
root = tk.Tk()
root.title("Braille Translator")
root.geometry("600x500")
root.resizable(False, False)

image_path = tk.StringVar()

# UI elements
tk.Label(root, text="Braille Script Translator", font=("Arial", 16)).pack(pady=10)

tk.Button(root, text="Select Braille Image", command=browse_image).pack()

image_label = tk.Label(root)
image_label.pack(pady=10)

tk.Button(root, text="Translate Image", command=run_translation, bg="#4CAF50", fg="white").pack(pady=5)

output_text = tk.Text(root, height=10, width=70)
output_text.pack(pady=10)

tk.Label(root, text="Translated Output (.txt & .pdf saved)", font=("Arial", 10)).pack()

# Start app
root.mainloop()
