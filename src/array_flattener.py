from typing import List, Union

def flatten_array(arr: List[Union[int, List]]) -> List[int]:
    """
    Recursively flatten a nested array of integers into a single-level list.

    This function handles nested arrays of arbitrary depth, converting 
    them into a single flat list of integers.

    Args:
        arr (List[Union[int, List]]): A potentially nested list of integers.

    Returns:
        List[int]: A flattened list of integers.

    Raises:
        TypeError: If the input contains non-integer and non-list elements.

    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
    """
    # Initialize the result list
    flattened = []

    # Iterate through each element in the input array
    for item in arr:
        # If the item is a list, recursively flatten it
        if isinstance(item, list):
            flattened.extend(flatten_array(item))
        # If the item is an integer, append it directly
        elif isinstance(item, int):
            flattened.append(item)
        # Raise an error for unsupported types
        else:
            raise TypeError(f"Unsupported type in array: {type(item)}")

    return flattened