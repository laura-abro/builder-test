from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing URL components:
        - scheme: URL scheme (e.g., 'http', 'https')
        - netloc: Network location (domain)
        - path: URL path
        - params: URL parameters
        - query: Parsed query parameters as a dictionary
        - fragment: URL fragment

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: Must be a non-empty string")

    try:
        # Parse the URL
        parsed = urlparse(url)

        # Parse query parameters
        query_params = parse_qs(parsed.query)
        
        # Convert query params values from lists to single values if possible
        query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

        return {
            'scheme': parsed.scheme,
            'netloc': parsed.netloc,
            'path': parsed.path,
            'params': parsed.params,
            'query': query_params,
            'fragment': parsed.fragment
        }

    except Exception as e:
        raise ValueError(f"Error parsing URL: {str(e)}")