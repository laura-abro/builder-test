import pytest
from src.array_flatten import flatten_array

def test_flatten_simple_list():
    """Test flattening a simple nested list"""
    input_list = [1, [2, 3], 4]
    assert flatten_array(input_list) == [1, 2, 3, 4]

def test_flatten_deeply_nested_list():
    """Test flattening a deeply nested list"""
    input_list = [1, [2, [3, 4]], 5, [6, [7, 8]]]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_flatten_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_flatten_single_list():
    """Test flattening a single list element"""
    assert flatten_array([1]) == [1]

def test_flatten_no_nested_list():
    """Test flattening a list with no nested lists"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_invalid_input_type():
    """Test that an error is raised for invalid input types"""
    with pytest.raises(TypeError):
        flatten_array([1, 'a', 2])
    
    with pytest.raises(TypeError):
        flatten_array([1, None, 2])

def test_multiple_layers_of_nesting():
    """Test flattening with multiple layers of nested lists"""
    input_list = [1, [2, [3, [4]]], 5]
    assert flatten_array(input_list) == [1, 2, 3, 4, 5]