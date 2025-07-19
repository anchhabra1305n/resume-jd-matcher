import re

from PyPDF2 import PdfReader
import streamlit as st


def read_pdf(uploaded_file) -> str:
    """Extract text from an uploaded PDF file."""
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text


def read_txt(uploaded_file) -> str:
    """Read text from an uploaded text file."""
    return uploaded_file.read().decode("utf-8")


def tokenize(text: str) -> set[str]:
    """Simple tokenizer that returns a set of words."""
    return set(re.findall(r"\b[a-zA-Z]{3,}\b", text.lower()))

st.title("Resume to Job Description Matcher")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

description_file = st.file_uploader(
    "Upload Job Description (PDF or Text)", type=["pdf", "txt"]
)

if resume_file is not None:
    st.write("Resume uploaded:", resume_file.name)

if description_file is not None:
    st.write("Job description uploaded:", description_file.name)

if resume_file is not None and description_file is not None:
    with st.spinner("Analyzing..."):
        # Read resume
        resume_text = read_pdf(resume_file)

        # Read job description (PDF or txt)
        if description_file.type == "text/plain":
            jd_text = read_txt(description_file)
        else:
            jd_text = read_pdf(description_file)

        resume_tokens = tokenize(resume_text)
        jd_tokens = tokenize(jd_text)

        if jd_tokens:
            common = resume_tokens & jd_tokens
            score = len(common) / len(jd_tokens)
        else:
            score = 0.0

        missing_skills = sorted(jd_tokens - resume_tokens)

    st.subheader("Results")
    st.write(f"Match Score: {score:.0%}")

    if missing_skills:
        st.write("Skills to consider adding:")
        st.write(", ".join(missing_skills[:10]))
