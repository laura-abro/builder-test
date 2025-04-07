import pytest
from src.url_parser import parse_url

def test_complete_url():
    url = "https://username:password@example.com:8080/path/to/page?key1=value1&key2=value2#fragment"
    result = parse_url(url)
    
    assert result['scheme'] == 'https'
    assert result['netloc'] == 'username:password@example.com:8080'
    assert result['path'] == '/path/to/page'
    assert result['query'] == {'key1': 'value1', 'key2': 'value2'}
    assert result['fragment'] == 'fragment'
    assert result['hostname'] == 'example.com'
    assert result['port'] == 8080
    assert result['username'] == 'username'
    assert result['password'] == 'password'

def test_simple_url():
    url = "http://www.example.com"
    result = parse_url(url)
    
    assert result['scheme'] == 'http'
    assert result['netloc'] == 'www.example.com'
    assert result['hostname'] == 'www.example.com'
    assert result['path'] is None
    assert result['query'] == {}

def test_url_with_query_params():
    url = "https://search.com/search?q=python&lang=en"
    result = parse_url(url)
    
    assert result['query'] == {'q': 'python', 'lang': 'en'}

def test_url_with_multiple_same_query_params():
    url = "https://example.com/page?tag=python&tag=programming"
    result = parse_url(url)
    
    assert result['query'] == {'tag': ['python', 'programming']}

def test_invalid_url_raises_error():
    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url("")

    with pytest.raises(ValueError, match="Invalid URL"):
        parse_url(None)

def test_url_with_special_characters():
    url = "https://example.com/path/with%20spaces?param=value%20with%20space"
    result = parse_url(url)
    
    assert result['path'] == '/path/with spaces'
    assert result['query'] == {'param': 'value with space'}

def test_url_without_scheme():
    url = "example.com/path"
    result = parse_url(url)
    
    assert result['scheme'] is None
    assert result['netloc'] is None
    assert result['path'] == 'example.com/path'