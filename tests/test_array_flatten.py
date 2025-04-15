import pytest
from src.array_flatten import flatten_array

def test_flat_array():
    """Test flattening an already flat array"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_simple_nested_array():
    """Test flattening a simply nested array"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_multiple_levels_of_nesting():
    """Test flattening multiple levels of nested lists"""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_nested_empty_arrays():
    """Test flattening arrays with nested empty arrays"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_type_raises_error():
    """Test that non-integer, non-list types raise a TypeError"""
    with pytest.raises(TypeError):
        flatten_array([1, 2, "3"])
    
    with pytest.raises(TypeError):
        flatten_array([1, [2, 3.5], 4])

def test_mixed_nesting():
    """Test flattening an array with mixed nesting patterns"""
    assert flatten_array([1, [2, 3, [4]], 5, [6]]) == [1, 2, 3, 4, 5, 6]