import streamlit as st

st.title("Resume to Job Description Matcher")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

description_file = st.file_uploader(
    "Upload Job Description (PDF or Text)", type=["pdf", "txt"]
)

if resume_file is not None:
    st.write("Resume uploaded:", resume_file.name)

if description_file is not None:
    st.write("Job description uploaded:", description_file.name)
