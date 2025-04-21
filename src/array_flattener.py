def flatten_array(arr):
    """
    Recursively flattens a nested array into a single-level array.
    
    Args:
        arr (list): A potentially nested list to be flattened.
    
    Returns:
        list: A flattened version of the input array.
    
    Raises:
        TypeError: If the input is not a list or contains non-list/non-iterable elements.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Initialize the result list
    flattened = []
    
    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is not a list, add it directly
        else:
            flattened.append(item)
    
    return flattened