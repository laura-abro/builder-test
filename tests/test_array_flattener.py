import pytest
from src.array_flattener import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple list."""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_flatten_nested_list():
    """Test flattening a list with one level of nesting."""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a list with multiple levels of nesting."""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_nested_empty_lists():
    """Test flattening lists containing empty lists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_element_type():
    """Test that an error is raised for non-integer, non-list elements."""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 2, "3"])

def test_nested_invalid_element_type():
    """Test error handling with nested invalid elements."""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, [2, "3"], 4])