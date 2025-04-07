from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.
    
    Args:
        url (str): The URL to parse
    
    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components
    
    Raises:
        ValueError: If the URL is invalid or empty
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed = urlparse(url)
        
        # Extract query parameters using parse_qs and decode them
        query_params = parse_qs(parsed.query)
        
        # Flatten single-item lists in query params and decode values
        query_params = {
            k: unquote(v[0]) if len(v) == 1 else [unquote(item) for item in v] 
            for k, v in query_params.items()
        }
        
        # Construct and return the parsed URL components
        return {
            'scheme': parsed.scheme or None,
            'netloc': parsed.netloc or None,
            'path': unquote(parsed.path) or None,
            'params': parsed.params or None,
            'query': query_params,
            'fragment': parsed.fragment or None,
            'hostname': parsed.hostname or None,
            'port': parsed.port,
            'username': parsed.username,
            'password': parsed.password
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")