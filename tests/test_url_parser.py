import pytest
from src.url_parser import parse_url

def test_parse_full_url():
    """Test parsing a complete URL with all components."""
    url = 'https://www.example.com/path/to/page?name=John&age=30#section'
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == '/path/to/page'
    assert result['query'] == {'name': 'John', 'age': '30'}
    assert result['fragment'] == 'section'

def test_parse_url_with_multiple_query_params():
    """Test parsing a URL with multiple query parameters."""
    url = 'http://test.com/search?q=python&category=programming&sort=relevance'
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'test.com'
    assert result['path'] == '/search'
    assert result['query'] == {
        'q': 'python', 
        'category': 'programming', 
        'sort': 'relevance'
    }

def test_parse_url_with_no_query_params():
    """Test parsing a URL without query parameters."""
    url = 'https://www.example.com/about'
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] == '/about'
    assert result['query'] == {}

def test_parse_url_with_special_characters():
    """Test parsing a URL with special characters."""
    url = 'https://example.com/search?q=hello%20world&special=value%2Ftest'
    result = parse_url(url)
    
    assert result['query'] == {'q': 'hello world', 'special': 'value/test'}

def test_invalid_url_empty_string():
    """Test handling of an empty URL."""
    with pytest.raises(ValueError, match="Invalid URL: Must be a non-empty string"):
        parse_url('')

def test_invalid_url_none():
    """Test handling of None input."""
    with pytest.raises(ValueError, match="Invalid URL: Must be a non-empty string"):
        parse_url(None)

def test_url_without_scheme():
    """Test parsing a URL without a scheme."""
    url = 'www.example.com/path'
    result = parse_url(url)
    
    assert result['scheme'] == ''
    assert result['netloc'] == ''
    assert result['path'] == 'www.example.com/path'