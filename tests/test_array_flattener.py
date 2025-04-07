import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple nested array"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_multi_level_nested_array():
    """Test flattening a multi-level nested array"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_flatten_no_nesting():
    """Test flattening an array with no nesting"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_deeply_nested_array():
    """Test flattening a deeply nested array"""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_types():
    """Test flattening an array with mixed types (ignoring non-int/list)"""
    assert flatten_array([1, [2, 'a'], 3, None]) == [1, 2, 3]

def test_flatten_nested_empty_arrays():
    """Test flattening an array with nested empty arrays"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]