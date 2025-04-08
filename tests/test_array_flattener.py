import pytest
from src.array_flattener import flatten_array

def test_simple_flatten():
    """Test flattening a simple nested array."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_deeply_nested_flatten():
    """Test flattening a deeply nested array."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_multiple_nested_levels():
    """Test flattening array with multiple nested levels."""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_empty_array():
    """Test flattening an empty array."""
    assert flatten_array([]) == []

def test_array_with_empty_lists():
    """Test flattening an array containing empty lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_non_list_input():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")

def test_mixed_type_array():
    """Test flattening an array with mixed types."""
    assert flatten_array([1, "string", [2, [3.14]], True]) == [1, "string", 2, 3.14, True]