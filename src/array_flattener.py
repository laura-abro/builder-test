from typing import List, Union

def flatten_array(nested_array: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers into a single-level array.
    
    This function recursively flattens a nested array, handling arrays 
    that may contain both integers and nested lists of varying depths.
    
    Args:
        nested_array (List[Union[int, List]]): A potentially nested array of integers
    
    Returns:
        List[int]: A flattened array containing all integers from the input
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Initialize result list
    result = []
    
    # Iterate through each element in the input array
    for item in nested_array:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten_array(item))
        # If the item is an integer, add it to the result
        elif isinstance(item, int):
            result.append(item)
        # Ignore non-integer, non-list items
        else:
            continue
    
    return result