import streamlit as st
import requests

uploaded_file = st.file_uploader("Upload file")

if uploaded_file:
    response = requests.post(
        "https://app-939090702834.asia-south1.run.app/upload",
        files={"file":uploaded_file}
    )
    st.write(response.json)