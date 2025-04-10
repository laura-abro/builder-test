from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested array of integers into a single-level array.
    
    This function recursively flattens a potentially multi-level nested array
    into a single-level array containing only integers.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Raises:
        TypeError: If the input is not a list or contains non-integer/list elements
    """
    # Initialize the result list
    flattened = []
    
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, add it to the result
        elif isinstance(item, int):
            flattened.append(item)
        # Raise an error for any other type of element
        else:
            raise TypeError(f"Invalid element type: {type(item)}. Only integers and lists are allowed.")
    
    return flattened