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
    """Test flattening array with multiple levels of nesting"""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_nested_empty_arrays():
    """Test flattening array with nested empty arrays"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_type_raises_error():
    """Test that non-integer and non-list types raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "three"])
    
    with pytest.raises(TypeError):
        flatten_array([1, [2, 3.5], 4])

def test_mixed_nesting_levels():
    """Test flattening array with mixed nesting levels"""
    assert flatten_array([1, [2], [[3]], [[[4]]], 5]) == [1, 2, 3, 4, 5]