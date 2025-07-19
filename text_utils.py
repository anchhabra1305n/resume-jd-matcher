import re

# Basic stopword list
STOPWORDS = {
    'a', 'an', 'the', 'and', 'or', 'for', 'nor', 'but', 'is', 'are',
    'was', 'were', 'in', 'on', 'at', 'of', 'to', 'from', 'by', 'with',
    'about', 'as', 'into', 'like', 'through', 'after', 'over', 'between',
    'out', 'against', 'during', 'without', 'before', 'under', 'around',
    'among', 'this', 'that', 'it', 'be', 'been', 'being', 'have', 'has',
    'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should',
    'can', 'could', 'may', 'might', 'must', 'if', 'because', 'while',
    'where', 'when', 'who', 'whom', 'which', 'there', 'their', 'so',
    'too', 'very'
}


def clean_text(text: str) -> str:
    """Return cleaned text with stopwords and special characters removed."""
    # Convert to lowercase
    text = text.lower()
    # Replace special characters with space
    text = re.sub(r'[^a-z\s]', ' ', text)
    # Tokenize by splitting on whitespace
    tokens = text.split()
    # Filter out stopwords
    tokens = [t for t in tokens if t not in STOPWORDS]
    # Reconstruct string
    return ' '.join(tokens)
