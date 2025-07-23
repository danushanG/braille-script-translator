from ultralytics import YOLO

# Load a model (you can use 'yolov8n.pt' for fastest, or 'yolov8s.pt' for better accuracy)
model = YOLO('yolov8n.pt')  # Use 'yolov8s.pt' if your system can handle it

# Train the model using your dataset
model.train(data='C:/Users/Hp/braille-script-translator/braille-dot-detector-1/data.yaml', epochs=30, imgsz=640)

