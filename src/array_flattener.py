from typing import List, Union

def flatten_array(nested_array: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers into a single-level array.
    
    This function recursively flattens a nested array, handling multiple 
    levels of nesting and preserving the order of elements.
    
    Args:
        nested_array (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input contains non-integer and non-list elements
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Initialize the result list
    result = []
    
    # Iterate through each element in the input array
    for item in nested_array:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            result.extend(flatten_array(item))
        # If the item is an integer, append it directly
        elif isinstance(item, int):
            result.append(item)
        # Raise an error for unsupported types
        else:
            raise TypeError(f"Unsupported type in array: {type(item)}")
    
    return result