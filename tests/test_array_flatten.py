import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_non_list_single_item():
    """Test flattening a single non-list item."""
    assert flatten_array(42) == [42]

def test_flatten_mixed_nested_list():
    """Test flattening a list with mixed types of nested lists."""
    assert flatten_array([1, [2, 'a', [3, 'b']], 4]) == [1, 2, 'a', 3, 'b', 4]

def test_flatten_list_with_empty_lists():
    """Test flattening a list containing empty lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]