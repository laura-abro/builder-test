import pytest
from src.array_flatten import flatten_array

def test_flat_list():
    """Test flattening a already flat list"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_nested_list():
    """Test flattening a nested list"""
    assert flatten_array([1, [2, 3], 4]) == [1, 2, 3, 4]

def test_deeply_nested_list():
    """Test flattening a deeply nested list"""
    assert flatten_array([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_multiple_levels_of_nesting():
    """Test flattening list with multiple levels of nesting"""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_list_with_empty_lists():
    """Test flattening a list containing empty lists"""
    assert flatten_array([1, [], [2, []], 3]) == [1, 2, 3]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        flatten_array(123)

def test_invalid_element_type():
    """Test that TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError):
        flatten_array([1, 'a', 2])

def test_nested_mixed_nesting():
    """Test flattening a list with various nesting levels"""
    assert flatten_array([1, [2, 3, [4, 5]], 6, [7]]) == [1, 2, 3, 4, 5, 6, 7]