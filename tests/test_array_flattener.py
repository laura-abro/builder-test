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

def test_flatten_multiple_levels_of_nesting():
    """Test flattening array with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_array_with_empty_nested_arrays():
    """Test flattening an array with empty nested arrays."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")
        flatten_array(123)
        flatten_array(None)

def test_mixed_content_array():
    """Test flattening an array with mixed content types."""
    assert flatten_array([1, "string", [2, 3.14], [None]]) == [1, "string", 2, 3.14, None]