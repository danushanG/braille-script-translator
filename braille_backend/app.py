from flask import Flask, request, jsonify 
from flask_cors import CORS  # ✅ Add this
from detect_braille_core import process_braille_image
import os

app = Flask(__name__)
CORS(app)  # ✅ Enable CORS for all domains

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    image = request.files['image']
    if image.filename == "":
        return jsonify({"error": "No file selected"}), 400

    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(image_path)

    # Call your model logic
    translated_text = process_braille_image(image_path)

    return jsonify({
        "translated_text": translated_text
    })

if __name__ == "__main__":
    app.run(debug=True)

