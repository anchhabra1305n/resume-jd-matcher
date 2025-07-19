import streamlit as st
from text_utils import clean_text

st.title("Resume to Job Description Matcher")

resume_file = st.file_uploader("Upload Resume (PDF or Text)", type=["pdf", "txt"])

description_file = st.file_uploader(
    "Upload Job Description (PDF or Text)", type=["pdf", "txt"]
)

if resume_file is not None:
    st.write("Resume uploaded:", resume_file.name)
    if resume_file.type == "text/plain":
        text = resume_file.read().decode("utf-8")
        cleaned = clean_text(text)
        st.subheader("Cleaned Resume Text")
        st.write(cleaned)

if description_file is not None:
    st.write("Job description uploaded:", description_file.name)
    if description_file.type == "text/plain":
        text = description_file.read().decode("utf-8")
        cleaned = clean_text(text)
        st.subheader("Cleaned Job Description")
        st.write(cleaned)
