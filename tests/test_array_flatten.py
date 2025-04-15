import pytest
from src.array_flatten import flatten_array

def test_basic_flatten():
    """Test basic list flattening"""
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_empty_list():
    """Test flattening an empty list"""
    assert flatten_array([]) == []

def test_no_nesting():
    """Test a list with no nesting"""
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_multiple_level_nesting():
    """Test deeply nested list"""
    assert flatten_array([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_mixed_elements():
    """Test list with mixed elements"""
    assert flatten_array([1, [2, 'a'], [3, [4, 'b']]]) == [1, 2, 'a', 3, 4, 'b']

def test_invalid_input():
    """Test that non-list input raises TypeError"""
    with pytest.raises(TypeError):
        flatten_array(123)
    with pytest.raises(TypeError):
        flatten_array("not a list")

def test_nested_empty_lists():
    """Test list with nested empty lists"""
    assert flatten_array([[], [1, []], 2]) == [1, 2]