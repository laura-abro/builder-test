import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple array"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_array():
    """Test flattening a nested array"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_multiple_nested_levels():
    """Test flattening array with multiple nesting levels"""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_array_with_empty_nested_lists():
    """Test flattening an array with empty nested lists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_element_type():
    """Test raising TypeError for invalid element types"""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 'string', 3])

def test_mixed_nested_array_with_errors():
    """Test error handling in a complex nested array"""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, [2, 'invalid'], 3])