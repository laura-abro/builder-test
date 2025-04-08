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

def test_flatten_list_with_empty_sublists():
    """Test flattening a list with empty sublists."""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_element_type():
    """Test that an error is raised for invalid element types."""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, 'string', 3])

def test_invalid_nested_element_type():
    """Test that an error is raised for invalid nested element types."""
    with pytest.raises(TypeError, match="Invalid element type"):
        flatten_array([1, [2, 'nested'], 3])

def test_complex_nested_structure():
    """Test a more complex nested structure."""
    assert flatten_array([1, [2, [3, [4, 5]]], 6]) == [1, 2, 3, 4, 5, 6]