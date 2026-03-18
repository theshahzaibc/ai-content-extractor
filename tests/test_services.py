from app.services.extractor import extract_content


def test_extract_content_success():
    # Using a real simple page
    result = extract_content("https://www.example.com")
    assert "Example Domain" in result


def test_extract_content_failure():
    # Invalid URL should return fail message
    result = extract_content("https://invalid-url.test")
    assert "Failed to extract content" in result
