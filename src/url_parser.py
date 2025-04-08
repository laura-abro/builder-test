from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.

    Args:
        url (str): The URL to be parsed.

    Returns:
        Dict[str, Any]: A dictionary containing URL components:
        - protocol: The URL protocol (http, https, etc.)
        - domain: The domain name
        - path: The URL-decoded path component
        - query_params: A dictionary of URL-decoded query parameters
        - port: The port number (if specified, otherwise None)
        - fragment: The fragment identifier (if present, otherwise None)

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)

        # Decode query parameters
        query_params = parse_qs(parsed_url.query, keep_blank_values=True)
        # URL-decode parameter values
        decoded_query_params = {
            k: [unquote(v) for v in vals] 
            for k, vals in query_params.items()
        }

        # Decode path if exists
        decoded_path = unquote(parsed_url.path) if parsed_url.path else None

        return {
            'protocol': parsed_url.scheme or None,
            'domain': parsed_url.hostname or None,
            'path': decoded_path,
            'query_params': decoded_query_params,
            'port': parsed_url.port,
            'fragment': parsed_url.fragment or None
        }
    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")