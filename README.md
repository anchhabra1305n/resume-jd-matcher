# resume-jd-matcher

A simple Streamlit app for uploading a resume and job description.
The files are parsed using **PyMuPDF** with a fallback to **pdfminer.six** so
that PDF and plain text files can be read directly in the browser.

## Usage

```bash
pip install -r requirements.txt
streamlit run app.py
```
