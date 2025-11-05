# app.py
import streamlit as st
import pandas as pd
from helper_fun import save_to_excel  # This will work if helper_fun.py is in the same folder

st.set_page_config(page_title="Allocation Form", layout="wide")
st.title("Dynamic Allocation Form")

# Step 1: Upload Excel/CSV template
uploaded_file = st.file_uploader("Upload your Excel/CSV file with column headers", type=["xlsx", "csv"])

if uploaded_file is not None:
    # Detect file type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file, nrows=0)
    else:
        df = pd.read_excel(uploaded_file, engine='openpyxl', nrows=0)

    columns = df.columns.tolist()
    st.success(f"Detected columns: {columns}")

    # Step 2: Create dynamic form
    st.header("Fill the Form")
    form_data = {}
    with st.form("allocation_form"):
        for col in columns:
            # Simple text input for all columns (can be enhanced for numbers/dates)
            form_data[col] = st.text_input(label=col)
        
        submitted = st.form_submit_button("Submit")
        if submitted:
            save_to_excel(form_data)
            st.success("Form submitted successfully!")
            st.json(form_data)
