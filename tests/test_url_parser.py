import pytest
from src.url_parser import parse_url

def test_parse_complete_url():
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

def test_parse_simple_url():
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.example.com'
    assert result['path'] is None
    assert result['query'] == {}
    assert result['fragment'] is None

def test_parse_url_with_query_params():
    url = "https://example.com/search?q=python&lang=en"
    result = parse_url(url)
    
    assert result['query'] == {'q': 'python', 'lang': 'en'}

def test_parse_url_with_multiple_same_query_params():
    url = "https://example.com/search?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result['query'] == {'tag': ['python', 'programming']}

def test_invalid_url_input():
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")
    
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_malformed_url():
    with pytest.raises(ValueError, match="Error parsing URL"):
        parse_url("not a valid url")

def test_url_with_special_characters():
    url = "https://example.com/path%20with%20spaces?key=value%20with%20space"
    result = parse_url(url)
    
    assert result['path'] == '/path with spaces'
    assert result['query'] == {'key': 'value with space'}