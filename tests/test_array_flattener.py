import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple nested array"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test flattening an array with no nesting"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_multiple_levels_of_nesting():
    """Test flattening multiple levels of nested arrays"""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_element_type():
    """Test that non-integer/non-list elements raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, "string", 3])

def test_nested_non_list_raises_error():
    """Test that a nested non-list element raises a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, [2, "invalid"], 3])

def test_complex_nested_structure():
    """Test a more complex nested structure"""
    assert flatten_array([1, [], [2], [[3]], [[[4]]]]) == [1, 2, 3, 4]