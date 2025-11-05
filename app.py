import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

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
    m
