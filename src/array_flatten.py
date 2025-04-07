from typing import Union, List, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested list into a single-level list.

    This function takes a potentially nested list and returns a flattened 
    version where all nested lists are expanded into a single list.

    Args:
        arr (Union[List[Any], Any]): Input list that may contain nested lists.

    Returns:
        List[Any]: A flattened list containing all elements.

    Examples:
        >>> flatten_array([1, [2, 3], [4, [5, 6]]])
        [1, 2, 3, 4, 5, 6]
        >>> flatten_array([1, 2, 3])
        [1, 2, 3]
        >>> flatten_array([])
        []
    """
    # Initialize the result list
    flattened = []

    # If input is not a list, return it as a single-element list
    if not isinstance(arr, list):
        return [arr]

    # Iterate through each element in the input list
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        else:
            # If it's not a list, add it directly to the result
            flattened.append(item)

    return flattened