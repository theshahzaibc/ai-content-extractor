import httpx
from bs4 import BeautifulSoup


def extract_content(url: str) -> str:
    """Simple content extractor: title + first 200 chars"""
    try:
        r = httpx.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        title = soup.title.string if soup.title else "No title"
        text = soup.get_text()[:200]
        return f"{title}\n{text}"
    except Exception:
        return "Failed to extract content"
