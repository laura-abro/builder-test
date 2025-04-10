def reverse_string(s: str) -> str:
    """
    Reverse the given string using a manual character iteration approach.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Validate input is a string
    if not isinstance(s, str):
        raise TypeError("Input must be a string")
    
    # Handle empty string case
    if len(s) <= 1:
        return s
    
    # Convert string to list for manipulation
    chars = list(s)
    
    # Two-pointer approach to reverse the string
    left, right = 0, len(chars) - 1
    while left < right:
        # Swap characters
        chars[left], chars[right] = chars[right], chars[left]
        # Move pointers
        left += 1
        right -= 1
    
    # Convert back to string and return
    return ''.join(chars)