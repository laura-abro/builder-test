from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Flatten a nested array/list into a single-level array.
    
    This function recursively flattens a potentially deeply nested list 
    into a single-level list containing all non-list elements.
    
    Args:
        arr (List[Union[Any, List]]): A potentially nested list to flatten
    
    Returns:
        List[Any]: A flattened list with all nested elements
    
    Raises:
        TypeError: If input is not a list
    
    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # Check input type
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Flattening logic
    flattened = []
    for item in arr:
        # Recursively flatten if the item is a list
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            flattened.append(item)
    
    return flattened