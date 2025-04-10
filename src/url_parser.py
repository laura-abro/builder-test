from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a URL into its constituent parts.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components.

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)

        # Prepare the result dictionary
        result = {
            'scheme': parsed_url.scheme or None,
            'netloc': parsed_url.netloc or None,
            'path': unquote(parsed_url.path) if parsed_url.path else '',
            'params': parsed_url.params or None,
            'query': parse_qs(parsed_url.query) if parsed_url.query else {},
            'fragment': parsed_url.fragment or None,
            'username': parsed_url.username,
            'password': parsed_url.password,
            'hostname': parsed_url.hostname,
            'port': parsed_url.port
        }

        return result

    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")