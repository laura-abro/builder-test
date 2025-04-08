import pytest
from src.array_flattener import flatten_array

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_simple_list():
    """Test flattening a simple list with no nesting."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_single_nested_list():
    """Test flattening a list with one level of nesting."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_multiple_nested_lists():
    """Test flattening a list with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4, [5]]]], 6]) == [1, 2, 3, 4, 5, 6]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types."""
    assert flatten_array([1, 'a', [2, 'b'], 3]) == [1, 'a', 2, 'b', 3]

def test_flatten_non_list_input():
    """Test flattening a non-list input."""
    assert flatten_array(42) == [42]
    assert flatten_array("string") == ["string"]

def test_flatten_none_input():
    """Test flattening None input."""
    assert flatten_array(None) == []

def test_nested_empty_lists():
    """Test flattening list with nested empty lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]