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

        # Decode path to handle URL-encoded characters
        decoded_path = unquote(parsed_url.path) if parsed_url.path else None

        # Extract query parameters
        query_params = parse_qs(parsed_url.query)
        # Convert query params to single values if they have only one element
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        # Construct and return the parsed URL dictionary
        return {
            "scheme": parsed_url.scheme or '',
            "netloc": parsed_url.netloc or '',
            "path": decoded_path or None,
            "params": parsed_url.params or None,
            "query": query_params,
            "fragment": parsed_url.fragment or None,
            "username": parsed_url.username,
            "password": parsed_url.password,
            "hostname": parsed_url.hostname,
            "port": parsed_url.port
        }
    except Exception as e:
        # Catch any unexpected parsing errors
        # For malformed URLs, treat the entire input as the path
        return {
            "scheme": '',
            "netloc": '',
            "path": url,
            "params": None,
            "query": {},
            "fragment": None,
            "username": None,
            "password": None,
            "hostname": None,
            "port": None
        }