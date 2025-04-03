"""
Test suite for input validation utility.
"""

import pytest
from src.input_validator import (
    validate_string, 
    validate_number, 
    validate_list, 
    ValidationError
)


# String Validation Tests
def test_validate_string_basic():
    assert validate_string("hello") == "hello"


def test_validate_string_min_length():
    assert validate_string("hello", min_length=3) == "hello"
    with pytest.raises(ValidationError):
        validate_string("hi", min_length=3)


def test_validate_string_max_length():
    assert validate_string("hello", max_length=5) == "hello"
    with pytest.raises(ValidationError):
        validate_string("hello world", max_length=5)


def test_validate_string_regex():
    assert validate_string("abc123", regex=r'^[a-z0-9]+$') == "abc123"
    with pytest.raises(ValidationError):
        validate_string("abc 123", regex=r'^[a-z0-9]+$')


def test_validate_string_empty():
    with pytest.raises(ValidationError):
        validate_string("")
    assert validate_string("", allow_empty=True) == ""


def test_validate_string_none():
    with pytest.raises(ValidationError):
        validate_string(None)


# Number Validation Tests
def test_validate_number_basic():
    assert validate_number(42) == 42
    assert validate_number(3.14) == 3.14


def test_validate_number_integer():
    assert validate_number(42, is_integer=True) == 42
    with pytest.raises(ValidationError):
        validate_number(3.14, is_integer=True)


def test_validate_number_min_max():
    assert validate_number(5, min_value=0, max_value=10) == 5
    with pytest.raises(ValidationError):
        validate_number(-1, min_value=0)
    with pytest.raises(ValidationError):
        validate_number(11, max_value=10)


def test_validate_number_none():
    with pytest.raises(ValidationError):
        validate_number(None)


# List Validation Tests
def test_validate_list_basic():
    assert validate_list([1, 2, 3]) == [1, 2, 3]


def test_validate_list_min_max_items():
    assert validate_list([1, 2, 3], min_items=2, max_items=4) == [1, 2, 3]
    with pytest.raises(ValidationError):
        validate_list([1], min_items=2)
    with pytest.raises(ValidationError):
        validate_list([1, 2, 3, 4, 5], max_items=4)


def test_validate_list_item_validator():
    def positive_int(x):
        if not isinstance(x, int) or x <= 0:
            raise ValueError("Must be a positive integer")
        return x
    
    assert validate_list([1, 2, 3], item_validator=positive_int) == [1, 2, 3]
    with pytest.raises(ValidationError):
        validate_list([1, -2, 3], item_validator=positive_int)


def test_validate_list_none():
    with pytest.raises(ValidationError):
        validate_list(None)