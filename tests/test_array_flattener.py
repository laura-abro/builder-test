import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_nested_array():
    """Test flattening a simple nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test an array with no nesting."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_multiple_levels_of_nesting():
    """Test flattening an array with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_types():
    """Test flattening an array with mixed types."""
    assert flatten_array([1, 'a', [2, 'b'], 3]) == [1, 'a', 2, 'b', 3]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")

def test_nested_empty_arrays():
    """Test flattening arrays containing empty arrays."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]