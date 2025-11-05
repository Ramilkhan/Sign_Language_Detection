import streamlit as st
from PIL import Image
from helper_func import load_model, predict_image

# -----------------------------
# Streamlit UI setup
# -----------------------------
st.set_page_config(page_title="Sign Language Detection", layout="centered")
st.title("🤟 Sign Language Detection using YOLOv8")

# -----------------------------
# Load Model
# -----------------------------
@st.cache_resource
def get_model():
    model = load_model("best.pt")
    return model

model = get_model()

# -----------------------------
# Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload a sign language image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Detecting sign..."):
        predictions, results = predict_image(model, image)

    if predictions:
        st.success(f"🧠 Detected sign(s): {', '.join(predictions)}")
    else:
        st.warning("No signs detected. Try a clearer image.")

    # Optional: display detection result image (YOLO annotated)
    results[0].show()
    st.image(results[0].plot(), caption="Detection Result", use_column_width=True)

st.markdown("---")
st.caption("Built with ❤️ using Streamlit & YOLOv8")
