import pytest
from src.array_flattener import flatten_array

def test_flatten_basic_list():
    """Test flattening a simple list"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a nested list"""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_list_with_empty_lists():
    """Test flattening a list with empty nested lists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_input_type():
    """Test that a non-list input raises a TypeError"""
    with pytest.raises(TypeError):
        flatten_array("not a list")

def test_mixed_type_list():
    """Test flattening a list with mixed types"""
    assert flatten_array([1, "a", [2, [3.14], "b"], None]) == [1, "a", 2, 3.14, "b", None]