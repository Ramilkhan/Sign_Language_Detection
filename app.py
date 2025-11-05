import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import io

# ----------------------------------
# Streamlit UI
# ----------------------------------
st.set_page_config(page_title="🤟 Sign Language Detection", layout="centered")
st.title("🤟 Sign Language Detection using YOLOv8")

# ----------------------------------
# Load model (cached for performance)
# ----------------------------------
@st.cache_resource
def load_model():
    model_path = "best.pt"  # make sure best.pt is in the same directory
    model = YOLO(model_path)
    return model

model = load_model()

# ----------------------------------
# Input Options
# ----------------------------------
st.sidebar.header("Choose Input Type")
option = st.sidebar.radio("Select input source:", ("Upload Image", "Use Camera"))

if option == "Upload Image":
    uploaded_file = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Run prediction
        st.write("🔍 Detecting sign...")
        results = model.predict(image, conf=0.5)
        boxes = results[0].boxes

        if len(boxes) > 0:
            annotated_img = results[0].plot()
            st.image(annotated_img, caption="Detection Result", use_container_width=True)
        else:
            st.warning("No sign detected. Try another image.")

elif option == "Use Camera":
    img_data = st.camera_input("📸 Capture an image")

    if img_data is not None:
        image = Image.open(img_data)
