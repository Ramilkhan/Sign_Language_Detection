import streamlit as st
import cv2
import tempfile
from ultralytics import YOLO
from helper_func import detect_signs

st.title("🤟 Real-Time Sign Language Detection")

# Load trained YOLOv8 model
model_path = "best.pt"  # adjust if your file is elsewhere
model = YOLO(model_path)

st.sidebar.title("Settings")
source_option = st.sidebar.selectbox("Select Input Source", ["Webcam", "Upload Video"])

if source_option == "Webcam":
    st.info("Click 'Start Detection' to open webcam and detect signs.")
    if st.button("Start Detection"):
        stframe = st.empty()
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                st.warning("No camera input detected.")
                break

            # Run detection
            annotated_frame, detected_text = detect_signs(model, frame)

            stframe.image(annotated_frame, channels="BGR", use_column_width=True)
            st.text(f"Detected Sign: {detected_text}")

            if st.button("Stop"):
                break

        cap.release()

elif source_option == "Upload Video":
    uploaded_file = st.file_uploader("Upload a video", type=["mp4", "mov", "avi"])
    if uploaded_file:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_file.read())

        st.video(tfile.name)
        st.write("Processing video...")

        # Run detection
        cap = cv2.VideoCapture(tfile.name)
        stframe = st.empty()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            annotated_frame, detected_text = detect_signs(model, frame)
            stframe.image(annotated_frame, channels="BGR", use_column_width=True)
            st.text(f"Detected Sign: {detected_text}")

        cap.release()
