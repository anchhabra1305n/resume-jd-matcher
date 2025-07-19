# resume-jd-matcher

A simple Streamlit app for uploading a resume and job description.

## Usage

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Text preprocessing

A helper function `clean_text` is provided in `text_utils.py` to clean raw text by:

- converting to lowercase
- removing common English stopwords
- stripping special characters

```python
from text_utils import clean_text
print(clean_text("This is an Example!"))
# output: 'example'
```
