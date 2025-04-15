def flatten_array(arr):
    """
    Recursively flatten a nested list/array into a single-level list.
    
    Args:
        arr (list): A potentially nested list to be flattened.
    
    Returns:
        list: A flattened version of the input list.
    
    Raises:
        TypeError: If the input is not a list or if it contains non-iterable elements 
                   that are not atomic (like numbers, strings).
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
    """
    # Handle edge cases
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Use a recursive approach to flatten the array
    flattened = []
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is not a list, add it directly
        else:
            flattened.append(item)
    
    return flattened