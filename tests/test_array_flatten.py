import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_nested_list():
    """Test flattening a simple nested list"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, 4]], [5, [6, 7]]]) == [1, 2, 3, 4, 5, 6, 7]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_list_with_empty_sublists():
    """Test flattening a list with empty sublists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_flatten_single_element_list():
    """Test flattening a list with a single element"""
    assert flatten_array([42]) == [42]

def test_flatten_mixed_type_list():
    """Test flattening a list with mixed types"""
    assert flatten_array([1, 'a', [2, 'b'], [3, [4, 'c']]]) == [1, 'a', 2, 'b', 3, 4, 'c']

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(42)

def test_nested_mixed_types_with_various_depths():
    """Test flattening a complex nested list with varying depths and types"""
    complex_list = [1, [2, 3, [4, 5]], 6, ['a', ['b', 'c']], []]
    assert flatten_array(complex_list) == [1, 2, 3, 4, 5, 6, 'a', 'b', 'c']