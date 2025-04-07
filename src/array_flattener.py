from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers into a single-level array.
    
    This function recursively flattens a nested array, handling 
    multiple levels of nesting and preserving the order of elements.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    flattened = []
    
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, add it directly
        elif isinstance(item, int):
            flattened.append(item)
        # Ignore any other type of item
        else:
            continue
    
    return flattened