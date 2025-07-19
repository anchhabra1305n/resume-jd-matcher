import io
import streamlit as st


def extract_text(uploaded_file: st.runtime.uploaded_file_manager.UploadedFile) -> str:
    """Extract text from an uploaded file."""
    if uploaded_file.type == "text/plain":
        return uploaded_file.read().decode("utf-8", errors="ignore")

    # Assume PDF for anything else
    data = uploaded_file.read()

    # Try PyMuPDF first
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


st.title("Resume to Job Description Matcher")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

description_file = st.file_uploader(
    "Upload Job Description (PDF or Text)", type=["pdf", "txt"]
)

if resume_file is not None:
    st.write("Resume uploaded:", resume_file.name)
    resume_text = extract_text(resume_file)
    st.text_area("Resume Text", resume_text, height=200)

if description_file is not None:
    st.write("Job description uploaded:", description_file.name)
    description_text = extract_text(description_file)
    st.text_area("Job Description Text", description_text, height=200)
