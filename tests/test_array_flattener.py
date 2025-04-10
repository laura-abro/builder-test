import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple non-nested array."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_array():
    """Test flattening a nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_multiple_nested_levels():
    """Test flattening an array with multiple nested levels."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_flatten_array_with_empty_lists():
    """Test flattening an array with empty nested lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_element_type():
    """Test that a TypeError is raised for invalid element types."""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 'string', 3])

def test_mixed_nested_array():
    """Test flattening a mixed nested array."""
    assert flatten_array([1, [2, 3, [4, 5]], 6, [7]]) == [1, 2, 3, 4, 5, 6, 7]