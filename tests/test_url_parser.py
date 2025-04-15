import pytest
from src.url_parser import parse_url

def test_basic_url_parsing():
    """Test parsing a basic URL with all components."""
    url = 'https://www.example.com:8080/path/to/page?param1=value1&param2=value2#section'
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'www.example.com',
        'port': 8080,
        'path': '/path/to/page',
        'query_params': {'param1': 'value1', 'param2': 'value2'},
        'fragment': 'section'
    }

def test_url_without_port():
    """Test parsing a URL without a port."""
    url = 'http://example.com/path'
    result = parse_url(url)
    
    assert result == {
        'protocol': 'http',
        'domain': 'example.com',
        'port': None,
        'path': '/path',
        'query_params': {},
        'fragment': None
    }

def test_url_with_multiple_query_params():
    """Test parsing a URL with multiple values for a query parameter."""
    url = 'https://example.com/search?tag=python&tag=programming'
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'example.com',
        'port': None,
        'path': '/search',
        'query_params': {'tag': ['python', 'programming']},
        'fragment': None
    }

def test_url_without_path_or_query():
    """Test parsing a URL without path or query parameters."""
    url = 'https://example.com'
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'example.com',
        'port': None,
        'path': '',
        'query_params': {},
        'fragment': None
    }

def test_invalid_url_empty_string():
    """Test parsing an empty string raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url('')

def test_invalid_url_none():
    """Test parsing None raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)

def test_invalid_url_no_protocol():
    """Test parsing a URL without a protocol raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: No protocol specified"):
        parse_url('example.com/path')

def test_url_with_special_characters():
    """Test parsing a URL with special characters in path and query params."""
    url = 'https://example.com/path%20with%20spaces?param=value%20with%20space'
    result = parse_url(url)
    
    assert result == {
        'protocol': 'https',
        'domain': 'example.com',
        'port': None,
        'path': '/path%20with%20spaces',
        'query_params': {'param': 'value with space'},
        'fragment': None
    }