from urllib.parse import urlparse, parse_qs
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its components.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing URL components:
        - scheme: The URL scheme (e.g., 'http', 'https')
        - netloc: The network location (domain)
        - path: The path component of the URL
        - params: URL parameters as a dictionary
        - query: Query parameters as a dictionary
        - fragment: The fragment identifier

    Raises:
        ValueError: If the URL is empty or None.
    """
    # Check for empty or None input
    if not url:
        raise ValueError("URL cannot be empty or None")

    # Parse the URL
    parsed_url = urlparse(url)

    # Extract and parse query parameters
    query_params = parse_qs(parsed_url.query)
    # Convert query params to simple values if they have only one element
    query_params = {k: v[0] if len(v) == 1 else v for k, v in query_params.items()}

    # Construct and return the result dictionary
    return {
        'scheme': parsed_url.scheme,
        'netloc': parsed_url.netloc,
        'path': parsed_url.path,
        'params': parsed_url.params,
        'query': query_params,
        'fragment': parsed_url.fragment
    }