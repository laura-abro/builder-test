import pytest
from src.url_parser import parse_url

def test_parse_full_url():
    """Test parsing a complete URL with all components."""
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result == {
        "scheme": "https",
        "netloc": "username:password@example.com:8080",
        "path": "/path/to/page",
        "params": None,
        "query": {"key1": "value1", "key2": "value2"},
        "fragment": "fragment",
        "username": "username",
        "password": "password",
        "hostname": "example.com",
        "port": 8080
    }

def test_parse_simple_url():
    """Test parsing a simple URL."""
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result["scheme"] == "http"
    assert result["netloc"] == "www.example.com"
    assert result["hostname"] == "www.example.com"

def test_parse_url_with_query_params():
    """Test parsing URL with multiple query parameters."""
    url = "https://example.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result["query"] == {"q": "python", "category": "programming"}

def test_parse_url_with_single_query_param():
    """Test parsing URL with a single query parameter."""
    url = "https://example.com/page?id=123"
    result = parse_url(url)
    
    assert result["query"] == {"id": "123"}

def test_parse_url_with_no_query_params():
    """Test parsing URL with no query parameters."""
    url = "https://example.com/page"
    result = parse_url(url)
    
    assert result["query"] == {}

def test_invalid_url_empty_string():
    """Test parsing an empty string raises ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url("")

def test_invalid_url_none():
    """Test parsing None raises ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)

def test_url_with_special_characters():
    """Test parsing URL with special characters."""
    url = "https://example.com/path?key=value%20with%20spaces"
    result = parse_url(url)
    
    assert result["query"] == {"key": "value with spaces"}

def test_url_with_multiple_same_query_params():
    """Test parsing URL with multiple values for the same query parameter."""
    url = "https://example.com/page?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result["query"] == {"tag": ["python", "programming"]}