import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_nested_list():
    """Test flattening a simple nested list."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_list_with_single_element():
    """Test flattening a list with a single element."""
    assert flatten_array([42]) == [42]

def test_flatten_already_flat_list():
    """Test flattening a list that is already flat."""
    assert flatten_array([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types_list():
    """Test flattening a list with mixed nested levels."""
    assert flatten_array([1, [2, 3], 4, [5, [6, 7]], 8]) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_invalid_input_raises_type_error():
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(42)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(None)