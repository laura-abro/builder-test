from typing import Union, List, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested array into a single-level list.

    Args:
        arr (Union[List[Any], Any]): Input array that may contain nested lists.

    Returns:
        List[Any]: A flattened list containing all non-list elements.

    Raises:
        TypeError: If the input is not a list or nested list.
    """
    # Check if input is None or not a list/nested list
    if arr is None:
        return []
    
    # If it's not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]
    
    # Recursive flattening
    flattened = []
    for item in arr:
        # Recursively flatten each item
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            flattened.append(item)
    
    return flattened