import pytest
from src.array_flatten import flatten_array

def test_flatten_basic_nested_list():
    """Test flattening a simple nested list."""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_flatten_empty_list():
    """Test flattening an empty list."""
    assert flatten_array([]) == []

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list."""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_flatten_mixed_types():
    """Test flattening a list with mixed types."""
    assert flatten_array([1, 'a', [2, 'b'], [3, [4, 'c']]]) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_flatten_single_element_list():
    """Test flattening a list with a single nested element."""
    assert flatten_array([1, [2]]) == [1, 2]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)