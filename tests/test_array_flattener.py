import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test flattening an already flat array."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_nested_empty_lists():
    """Test flattening an array with empty nested lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_multiple_levels_of_nesting():
    """Test flattening an array with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_invalid_type_raises_error():
    """Test that an unsupported type raises a TypeError."""
    with pytest.raises(TypeError, match="Unsupported type in array"):
        flatten_array([1, 2, "3"])

def test_mixed_nesting_and_types():
    """Test flattening an array with mixed nesting and integers."""
    assert flatten_array([1, [2, 3, [4]], 5, [6]]) == [1, 2, 3, 4, 5, 6]