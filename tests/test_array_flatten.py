import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_nested_list():
    """Test flattening a simple nested list."""
    assert flatten_array([1, [2, 3], [4, 5]]) == [1, 2, 3, 4, 5]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, 4]], [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_non_nested_list():
    """Test flattening a list with no nested elements."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types and nesting."""
    assert flatten_array([1, [2, 'a'], [3, [4, 'b']]]) == [1, 2, 'a', 3, 4, 'b']

def test_flatten_multiple_levels_of_nesting():
    """Test flattening a list with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_nested_lists():
    """Test flattening a list with empty nested lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]