import pytest
from src.url_parser import parse_url

def test_basic_url_parsing():
    """Test parsing a basic URL."""
    url = "https://www.example.com/path/to/page"
    result = parse_url(url)
    assert result == {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/path/to/page',
        'params': '',
        'query': {},
        'fragment': ''
    }

def test_url_with_query_params():
    """Test parsing a URL with query parameters."""
    url = "https://www.example.com/search?q=python&lang=en"
    result = parse_url(url)
    assert result == {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/search',
        'params': '',
        'query': {'q': 'python', 'lang': 'en'},
        'fragment': ''
    }

def test_url_with_multiple_query_params():
    """Test parsing a URL with multiple values for a query parameter."""
    url = "https://www.example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    assert result == {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/search',
        'params': '',
        'query': {'tag': ['python', 'programming']},
        'fragment': ''
    }

def test_url_with_fragment():
    """Test parsing a URL with a fragment."""
    url = "https://www.example.com/page#section1"
    result = parse_url(url)
    assert result == {
        'scheme': 'https',
        'netloc': 'www.example.com',
        'path': '/page',
        'params': '',
        'query': {},
        'fragment': 'section1'
    }

def test_complex_url():
    """Test parsing a complex URL with all components."""
    url = "https://user:pass@www.example.com:8080/path/to/page?q=test&x=y#fragment"
    result = parse_url(url)
    assert result == {
        'scheme': 'https',
        'netloc': 'user:pass@www.example.com:8080',
        'path': '/path/to/page',
        'params': '',
        'query': {'q': 'test', 'x': 'y'},
        'fragment': 'fragment'
    }

def test_empty_url_raises_error():
    """Test that an empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty or None"):
        parse_url("")

def test_none_url_raises_error():
    """Test that a None URL raises a ValueError."""
    with pytest.raises(ValueError, match="URL cannot be empty or None"):
        parse_url(None)