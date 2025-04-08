import pytest
from src.url_parser import parse_url

def test_full_url_parsing():
    """Test parsing a full URL with all components."""
    url = "https://www.example.com:8080/path/to/page?param1=value1&param2=value2#section"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'www.example.com',
        'path': '/path/to/page',
        'query_params': {'param1': ['value1'], 'param2': ['value2']},
        'port': 8080,
        'fragment': 'section'
    }

def test_minimal_url():
    """Test parsing a minimal URL."""
    url = "http://example.com"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'http',
        'domain': 'example.com',
        'path': None,
        'query_params': {},
        'port': None,
        'fragment': None
    }

def test_url_with_query_params():
    """Test parsing a URL with multiple query parameters."""
    url = "https://search.com/search?q=python&category=programming"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'search.com',
        'path': '/search',
        'query_params': {'q': ['python'], 'category': ['programming']},
        'port': None,
        'fragment': None
    }

def test_invalid_url_input():
    """Test handling of invalid URL inputs."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)

def test_url_without_protocol():
    """Test parsing a URL without a protocol."""
    url = "example.com/path"
    result = parse_url(url)
    
    assert result == {
        'protocol': None,
        'domain': None,
        'path': 'example.com/path',
        'query_params': {},
        'port': None,
        'fragment': None
    }

def test_complex_url_with_special_characters():
    """Test parsing a URL with special characters."""
    url = "https://example.com/path%20with%20spaces?key=value%20with%20space"
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'example.com',
        'path': '/path with spaces',
        'query_params': {'key': ['value with space']},
        'port': None,
        'fragment': None
    }