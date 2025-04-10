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

def test_flatten_no_nested_array():
    """Test flattening an array without nesting."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_multiple_levels_of_nesting():
    """Test flattening an array with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types():
    """Test flattening an array with mixed types (only keeping integers)."""
    assert flatten_array([1, [2, 'a', 3], 4, [5, [6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_complex_nested_structure():
    """Test flattening a complex nested structure."""
    assert flatten_array([1, [2, [3, [4, [5]]], 6], 7]) == [1, 2, 3, 4, 5, 6, 7]