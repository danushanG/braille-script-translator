import cv2
import numpy as np

def preprocess_braille_image(input_path, output_path):
    # Load image
    img = cv2.imread(input_path)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Invert colors (black dots -> white dots if needed)
    _, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY_INV)

    # Resize image (YOLO expects ~640x640)
    resized = cv2.resize(binary, (640, 640), interpolation=cv2.INTER_LINEAR)

    # Add Gaussian noise (simulate scanned paper)
    noise = np.zeros(resized.shape, np.uint8)
    cv2.randn(noise, 0, 25)  # mean=0, stddev=25
    noisy = cv2.add(resized, noise)

    # Slight blur to soften sharp edges
    blurred = cv2.GaussianBlur(noisy, (3,3), 0)

    # Save preprocessed image
    cv2.imwrite(output_path, blurred)
    print(f"Preprocessed image saved at {output_path}")

# Example usage
preprocess_braille_image("contracted_braille_example.jpg", "preprocessed_braille.jpg")
