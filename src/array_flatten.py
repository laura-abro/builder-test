from typing import List, Union, Any

def flatten_array(arr: List[Union[Any, List]]) -> List[Any]:
    """
    Recursively flatten a nested list into a single-level list.

    This function takes a potentially nested list and returns a flattened 
    version where all nested lists are expanded into a single list.

    Args:
        arr (List[Union[Any, List]]): A potentially nested list to be flattened.

    Returns:
        List[Any]: A flattened list containing all non-list elements.

    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([])
        []
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
    """
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is not a list, add it directly
        else:
            flattened.append(item)
    
    return flattened