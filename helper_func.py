import cv2
import numpy as np

def detect_signs(model, frame):
    """
    Runs YOLOv8 detection on a given frame and returns
    annotated frame and detected class name.
    """
    results = model.predict(frame, verbose=False)
    annotated_frame = results[0].plot()

    # Extract the top detected class name if available
    if len(results[0].boxes.cls) > 0:
        cls_id = int(results[0].boxes.cls[0])
        detected_text = model.names[cls_id]
    else:
        detected_text = "No sign detected"

    return annotated_frame, detected_text
