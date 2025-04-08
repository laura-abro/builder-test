from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Flatten a nested list of integers into a single-level list.
    
    This function recursively flattens a nested list, handling 
    lists of varying depths and mixed types.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list containing all integers
    
    Raises:
        TypeError: If the input is not a list or contains non-integer elements
    """
    # Create a list to store flattened result
    flattened = []
    
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Iterate through each element in the input list
    for item in arr:
        # If item is a list, recursively flatten
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If item is an integer, append to result
        elif isinstance(item, int):
            flattened.append(item)
        # Raise error for non-integer, non-list elements
        else:
            raise TypeError(f"List contains non-integer element: {item}")
    
    return flattened