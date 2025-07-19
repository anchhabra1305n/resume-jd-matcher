import io
import re
import streamlit as st


# ---------- Text Extraction ----------
def extract_text(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile) -> str:
    """Extract text from uploaded PDF or text file."""
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8", errors="ignore")

    data = uploaded_file.read()

    # Try PyMuPDF
    try:
        import fitz  # PyMuPDF
        text = ""
        with fitz.open(stream=data, filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception:
        pass

    # Fallback to pdfminer.six
    try:
        from pdfminer.high_level import extract_text as pdfminer_extract
        return pdfminer_extract(io.BytesIO(data))
    except Exception as e:
        return f"Error extracting text: {e}"


# ---------- Tokenization ----------
def tokenize(text: str) -> set[str]:
    """Simple tokenizer that returns a set of lowercase words with 3+ letters."""
    return set(re.findall(r"\b[a-zA-Z]{3,}\b", text.lower()))


# ---------- UI ----------
st.title("Resume to Job Description Matcher")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
description_file