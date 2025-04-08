from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its component parts.
    
    Args:
        url (str): The URL to parse.
    
    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components.
    
    Raises:
        ValueError: If the URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")
    
    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)
        
        # Check if the URL has a valid scheme or netloc
        if not parsed_url.scheme and not parsed_url.netloc:
            raise ValueError("Invalid URL format")
        
        # Extract query parameters using parse_qs and decode
        query_params = parse_qs(parsed_url.query)
        
        # URL decode and flatten single-item lists in query params
        query_params = {
            k: unquote(v[0]) if len(v) == 1 else [unquote(x) for x in v] 
            for k, v in query_params.items()
        }
        
        # Decode path and other components
        decoded_path = unquote(parsed_url.path) if parsed_url.path else None
        decoded_fragment = unquote(parsed_url.fragment) if parsed_url.fragment else None
        
        # Construct and return the parsed URL dictionary
        return {
            'scheme': parsed_url.scheme or None,
            'netloc': parsed_url.netloc or None,
            'path': decoded_path,
            'params': parsed_url.params or None,
            'query': query_params,
            'fragment': decoded_fragment,
            'username': parsed_url.username,
            'password': parsed_url.password,
            'hostname': parsed_url.hostname,
            'port': parsed_url.port
        }
    except ValueError as ve:
        # Re-raise ValueError for invalid URL format
        raise ValueError(f"Error parsing URL: {str(ve)}")
    except Exception as e:
        # Catch any unexpected parsing errors
        raise ValueError(f"Error parsing URL: {str(e)}")