import pytest
from src.binary_search import binary_search

def test_binary_search_basic():
    """Test basic functionality of binary search"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3  # 7 is at index 3
    assert binary_search(arr, 1) == 0  # First element
    assert binary_search(arr, 13) == 6  # Last element

def test_binary_search_not_found():
    """Test when target is not in the array"""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1  # Not in array
    assert binary_search(arr, 0) == -1  # Less than first element
    assert binary_search(arr, 14) == -1  # Greater than last element

def test_binary_search_empty_list():
    """Test binary search on an empty list"""
    assert binary_search([], 5) == -1

def test_binary_search_single_element():
    """Test binary search on a single-element list"""
    arr = [5]
    assert binary_search(arr, 5) == 0  # Found
    assert binary_search(arr, 4) == -1  # Not found

def test_binary_search_error_handling():
    """Test error handling for invalid inputs"""
    # Not a list
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    # Unsorted list
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 4], 3)

def test_binary_search_duplicates():
    """Test binary search with duplicate elements"""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    # Note: returns the first occurrence of the target
    assert binary_search(arr, 2) in [1, 2]
    assert binary_search(arr, 3) in [3, 4, 5]