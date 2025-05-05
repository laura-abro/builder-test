from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested array of integers.
    
    This function takes a potentially nested list of integers and returns 
    a single-level list containing all the integers.
    
    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers
    
    Returns:
        List[int]: A flattened list of integers
    
    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
        >>> flatten_array([])
        []
    """
    # Base case: if the input is an empty list, return an empty list
    if not arr:
        return []
    
    # Result list to store flattened elements
    flattened = []
    
    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, append it directly
        elif isinstance(item, (int, float)):
            # Convert float to int to match the test requirements
            flattened.append(int(item))
        # Ignore any other types of elements
        else:
            continue
    
    return flattened