from typing import List, Union

def flatten_array(nested_array: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers to a single-level list.
    
    This function recursively flattens any level of nested lists into a single 
    list of integers. It handles various levels of nesting and supports empty 
    lists and nested empty lists.
    
    Args:
        nested_array (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input contains non-integer non-list elements
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    result = []
    
    for item in nested_array:
        if isinstance(item, list):
            # Recursively flatten nested lists
            result.extend(flatten_array(item))
        elif isinstance(item, int):
            # Add integers directly to the result
            result.append(item)
        else:
            # Raise error for non-integer, non-list items
            raise TypeError(f"Unsupported type in array: {type(item)}")
    
    return result