import pytest
from src.url_parser import parse_url

def test_parse_full_url():
    """Test parsing a complete URL with all components."""
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'username:password@example.com:8080'
    assert result['path'] == '/path/to/page'
    assert result['query'] == {'key1': 'value1', 'key2': 'value2'}
    assert result['fragment'] == 'fragment'
    assert result['username'] == 'username'
    assert result['password'] == 'password'
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080

def test_parse_minimal_url():
    """Test parsing a minimal URL."""
    url = "http://example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'example.com'
    assert result['path'] is None
    assert result['query'] == {}
    assert result['fragment'] is None

def test_parse_url_with_multiple_query_params():
    """Test parsing URL with multiple values for a single query parameter."""
    url = "https://example.com?key=value1&key=value2"
    result = parse_url(url)
    
    assert result['query'] == {'key': ['value1', 'value2']}

def test_empty_url_raises_error():
    """Test that empty URL raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url("")

def test_none_url_raises_error():
    """Test that None input raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid URL: URL must be a non-empty string"):
        parse_url(None)

def test_malformed_url_handling():
    """Test handling of malformed URLs."""
    url = "not a valid url"
    result = parse_url(url)
    
    assert result['scheme'] == ''
    assert result['netloc'] == ''
    assert result['path'] == 'not a valid url'

def test_url_with_special_characters():
    """Test URL parsing with special characters."""
    url = "https://example.com/path%20with%20spaces?param=value%26another"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'example.com'
    assert result['path'] == '/path with spaces'
    assert result['query'] == {'param': 'value&another'}