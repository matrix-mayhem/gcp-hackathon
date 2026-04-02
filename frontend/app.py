import streamlit as st
import requests

st.title("📄 AI Document Analyzer")

API_URL = "https://app-939090702834.asia-south1.run.app/upload"

uploaded_file = st.file_uploader("Upload a file")

if uploaded_file:
    st.write("Uploading...")

    response = requests.post(
        f"{API_URL}/upload",
        files={"file": uploaded_file}
    )

    if response.status_code == 200:
        st.success("Uploaded successfully!")
        st.json(response.json())
    else:
        st.error("Upload failed")
        st.text(response.text)

# Show stored files
if st.button("Show Uploaded Files"):
    response = requests.get(f"{API_URL}/files")
    st.json(response.json())