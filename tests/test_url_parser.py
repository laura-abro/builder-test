import pytest
from src.url_parser import parse_url

def test_parse_full_url():
    """Test parsing a full URL with all components."""
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'username:password@example.com:8080'
    assert result['path'] == '/path/to/page'
    assert result['query'] == {'key1': ['value1'], 'key2': ['value2']}
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080

def test_parse_simple_url():
    """Test parsing a simple URL."""
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == ''
    assert result['query'] == {}
    assert result['fragment'] is None
    assert result['hostname'] == 'www.example.com'

def test_parse_url_with_query():
    """Test parsing a URL with multiple query parameters."""
    url = "https://example.com/search?q=python&lang=en"
    result = parse_url(url)
    
    assert result['query'] == {'q': ['python'], 'lang': ['en']}

def test_parse_url_with_fragment():
    """Test parsing a URL with a fragment."""
    url = "https://example.com/page#section"
    result = parse_url(url)
    
    assert result['fragment'] == 'section'

def test_invalid_url_empty():
    """Test parsing an empty URL."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url("")

def test_invalid_url_none():
    """Test parsing None as a URL."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)

def test_minimal_url():
    """Test parsing a minimal valid URL."""
    url = "https://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['hostname'] == 'example.com'

def test_url_with_special_characters():
    """Test parsing a URL with special characters."""
    url = "https://example.com/path%20with%20spaces?key=value%26other"
    result = parse_url(url)
    
    assert result['path'] == '/path with spaces'
    assert result['query'] == {'key': ['value&other']}