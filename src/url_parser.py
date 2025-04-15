from urllib.parse import urlparse, parse_qs, unquote
from typing import Dict, Any, Optional

def parse_url(url: str) -> Dict[str, Any]:
    """
    Parse a given URL into its component parts.

    Args:
        url (str): The URL to parse.

    Returns:
        Dict[str, Any]: A dictionary containing parsed URL components:
        - protocol: The URL protocol (e.g., 'http', 'https')
        - domain: The domain name
        - port: The port number (None if not specified)
        - path: The path component of the URL (preserving original encoding)
        - query_params: A dictionary of query parameters (with URL decoding)
        - fragment: The fragment identifier (if present)

    Raises:
        ValueError: If the input URL is invalid or empty.
    """
    # Check for empty or None input
    if not url or not isinstance(url, str):
        raise ValueError("Invalid URL: URL must be a non-empty string")

    try:
        # Use urlparse to break down the URL
        parsed_url = urlparse(url)

        # Extract components
        protocol = parsed_url.scheme
        domain = parsed_url.hostname
        port = parsed_url.port
        path = parsed_url.path  # Keep original path encoding
        fragment = parsed_url.fragment

        # Parse query parameters with URL decoding
        query_params = parse_qs(parsed_url.query, keep_blank_values=True)
        
        # Decode query parameters and convert lists/single items
        query_params = {
            unquote(k): unquote(v[0]) if len(v) == 1 
            else [unquote(item) for item in v] 
            for k, v in query_params.items()
        }

        # Validate protocol
        if not protocol:
            raise ValueError("Invalid URL: No protocol specified")

        return {
            'protocol': protocol,
            'domain': domain,
            'port': port,
            'path': path,
            'query_params': query_params,
            'fragment': fragment or None
        }

    except Exception as e:
        raise ValueError(f"Invalid URL: {str(e)}")