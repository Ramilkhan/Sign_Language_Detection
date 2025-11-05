from ultralytics import YOLO
from PIL import Image
import numpy as np

def load_model(model_path="best.pt"):
    """Load YOLOv8 model"""
    model = YOLO(model_path)
    return model

def predict_image(model, image):
    """Run YOLO prediction on a PIL image"""
    # Convert image to numpy array
    img_array = np.array(image)
    results = model.predict(source=img_array, conf=0.5, verbose=False)
    predictions = []
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            predictions.append(label)
    return predictions, results
