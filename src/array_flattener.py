from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flatten a nested array into a single-level array.
    
    Args:
        arr (List[Union[Any, List]]): A potentially nested list to be flattened.
    
    Returns:
        List[Any]: A flattened list with all nested elements.
    
    Raises:
        TypeError: If the input is not a list.
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
        >>> flatten_array([])
        []
    """
    # Check if input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Initialize the result list
    flattened = []
    
    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # Otherwise, append the item directly
        else:
            flattened.append(item)
    
    return flattened