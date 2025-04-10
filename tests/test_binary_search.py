import pytest
from src.binary_search import binary_search

def test_binary_search_basic():
    """Test basic binary search functionality."""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 7) == 3  # 7 is at index 3
    assert binary_search(arr, 13) == 6  # Last element
    assert binary_search(arr, 1) == 0   # First element

def test_binary_search_not_found():
    """Test when target is not in the array."""
    arr = [1, 3, 5, 7, 9, 11, 13]
    assert binary_search(arr, 4) == -1
    assert binary_search(arr, 0) == -1
    assert binary_search(arr, 14) == -1

def test_binary_search_edge_cases():
    """Test edge cases like empty list and single-element list."""
    assert binary_search([], 5) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1

def test_binary_search_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Not a list
    with pytest.raises(TypeError, match="Input must be a list"):
        binary_search("not a list", 5)
    
    # Unsorted list
    with pytest.raises(ValueError, match="Input list must be sorted in ascending order"):
        binary_search([5, 3, 1], 3)

def test_binary_search_duplicate_values():
    """Test handling of duplicate values."""
    arr = [1, 2, 2, 3, 3, 3, 4, 5]
    # Returns the index of the first occurrence of the target
    assert binary_search(arr, 3) in [3, 4, 5]
    assert binary_search(arr, 2) in [1, 2]