from typing import List, Union, Any

def flatten_array(arr: List[Union[int, List[Any]]]) -> List[int]:
    """
    Flatten a nested array of integers into a single-level array.
    
    This function recursively flattens nested lists of arbitrary depth 
    into a single list of integers.
    
    Args:
        arr (List[Union[int, List[Any]]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Flattening logic using recursive approach
    flattened = []
    for item in arr:
        # If item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is an integer, add to the list
        elif isinstance(item, int):
            flattened.append(item)
        else:
            # Raise error for non-integer, non-list elements
            raise TypeError(f"Invalid element type: {type(item)}. Only integers and nested lists are allowed.")
    
    return flattened