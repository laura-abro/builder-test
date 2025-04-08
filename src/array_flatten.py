from typing import List, Any, Union

def flatten_array(arr: List[Any]) -> List[Any]:
    """
    Recursively flatten a nested list of arbitrary depth.
    
    Args:
        arr (List[Any]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list with all nested elements.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Initialize flattened list
    flattened = []
    
    # Iterate through each element in the input list
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # If not a list, add the item directly
            flattened.append(item)
    
    return flattened