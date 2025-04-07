from typing import Union, List, Any

def flatten_array(arr: Union[List[Any], Any]) -> List[Any]:
    """
    Recursively flatten a nested list into a single-level list.

    Args:
        arr (Union[List[Any], Any]): Input list or nested list to be flattened.

    Returns:
        List[Any]: A flattened list containing all non-list elements.

    Examples:
        >>> flatten_array([1, [2, 3], 4])
        [1, 2, 3, 4]
        >>> flatten_array([1, [2, [3, 4]], 5])
        [1, 2, 3, 4, 5]
        >>> flatten_array([])
        []
    """
    result = []
    
    def _flatten(item):
        if isinstance(item, list):
            for sub_item in item:
                _flatten(sub_item)
        else:
            result.append(item)
    
    _flatten(arr)
    return result