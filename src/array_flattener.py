def flatten_array(arr):
    """
    Flatten a nested array (list) to a single-level array.
    
    This function recursively flattens a nested list of arbitrary depth 
    into a single-level list.
    
    Args:
        arr (list): The input nested list to be flattened.
    
    Returns:
        list: A flattened list containing all elements from the input list.
    
    Raises:
        TypeError: If the input is not a list or contains non-list/non-iterable elements.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Result list to store flattened elements
    result = []
    
    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten_array(item))
        # Otherwise, add the item directly to the result
        else:
            result.append(item)
    
    return result