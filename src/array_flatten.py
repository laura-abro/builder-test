from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested list of integers into a single-level list.
    
    Args:
        arr (List[Union[int, List]]): A nested list that may contain integers or nested lists
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input is not a list or contains non-integer/non-list elements
    """
    flattened = []
    
    for item in arr:
        if isinstance(item, list):
            # Recursively flatten nested lists
            flattened.extend(flatten_array(item))
        elif isinstance(item, int):
            # Add integers directly to the result
            flattened.append(item)
        else:
            # Raise an error for invalid input types
            raise TypeError(f"Invalid input type: {type(item)}. Only integers and lists are allowed.")
    
    return flattened