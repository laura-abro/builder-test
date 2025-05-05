import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_array():
    """Test flattening a simple array with no nesting"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_array():
    """Test flattening an array with one level of nesting"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_array():
    """Test flattening an array with multiple levels of nesting"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_array():
    """Test flattening an empty array"""
    assert flatten_array([]) == []

def test_flatten_array_with_empty_nested_lists():
    """Test flattening an array with empty nested lists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_flatten_array_with_mixed_types():
    """Test that non-integer and non-list types are ignored"""
    assert flatten_array([1, [2, 'a'], 3, [4.5], None]) == [1, 2, 3, 4]

def test_very_deeply_nested_array():
    """Test flattening a very deeply nested array"""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]