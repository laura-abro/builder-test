"""
Input Validation Utility Module

This module provides a comprehensive set of input validation functions
to ensure data integrity and prevent invalid inputs.
"""

import re
from typing import Any, Union, List, Optional


class ValidationError(ValueError):
    """Custom exception for input validation errors."""
    pass


def validate_not_none(value: Any, field_name: str = "Value") -> Any:
    """
    Validate that the input is not None.

    Args:
        value (Any): The value to validate
        field_name (str, optional): Name of the field for error message. Defaults to "Value".

    Returns:
        Any: The validated value

    Raises:
        ValidationError: If the value is None
    """
    if value is None:
        raise ValidationError(f"{field_name} cannot be None")
    return value


def validate_type(value: Any, expected_type: type, field_name: str = "Value") -> Any:
    """
    Validate the type of the input.

    Args:
        value (Any): The value to validate
        expected_type (type): The expected type of the value
        field_name (str, optional): Name of the field for error message. Defaults to "Value".

    Returns:
        Any: The validated value

    Raises:
        ValidationError: If the value is not of the expected type
    """
    validate_not_none(value, field_name)
    if not isinstance(value, expected_type):
        raise ValidationError(f"{field_name} must be of type {expected_type.__name__}")
    return value


def validate_range(
    value: Union[int, float], 
    min_value: Optional[Union[int, float]] = None, 
    max_value: Optional[Union[int, float]] = None, 
    field_name: str = "Value"
) -> Union[int, float]:
    """
    Validate that a numeric value is within a specified range.

    Args:
        value (Union[int, float]): The value to validate
        min_value (Optional[Union[int, float]], optional): Minimum allowed value. Defaults to None.
        max_value (Optional[Union[int, float]], optional): Maximum allowed value. Defaults to None.
        field_name (str, optional): Name of the field for error message. Defaults to "Value".

    Returns:
        Union[int, float]: The validated value

    Raises:
        ValidationError: If the value is outside the specified range
    """
    validate_type(value, (int, float), field_name)
    
    if min_value is not None and value < min_value:
        raise ValidationError(f"{field_name} must be greater than or equal to {min_value}")
    
    if max_value is not None and value > max_value:
        raise ValidationError(f"{field_name} must be less than or equal to {max_value}")
    
    return value


def validate_string(
    value: str, 
    min_length: Optional[int] = None, 
    max_length: Optional[int] = None, 
    regex: Optional[str] = None, 
    field_name: str = "Value"
) -> str:
    """
    Validate a string input with optional constraints.

    Args:
        value (str): The string to validate
        min_length (Optional[int], optional): Minimum string length. Defaults to None.
        max_length (Optional[int], optional): Maximum string length. Defaults to None.
        regex (Optional[str], optional): Regex pattern for validation. Defaults to None.
        field_name (str, optional): Name of the field for error message. Defaults to "Value".

    Returns:
        str: The validated string

    Raises:
        ValidationError: If the string does not meet the specified constraints
    """
    validate_type(value, str, field_name)
    
    if min_length is not None and len(value) < min_length:
        raise ValidationError(f"{field_name} must be at least {min_length} characters long")
    
    if max_length is not None and len(value) > max_length:
        raise ValidationError(f"{field_name} must be no more than {max_length} characters long")
    
    if regex is not None and not re.match(regex, value):
        raise ValidationError(f"{field_name} does not match the required pattern")
    
    return value


def validate_list(
    value: List[Any], 
    min_length: Optional[int] = None, 
    max_length: Optional[int] = None, 
    item_type: Optional[type] = None, 
    field_name: str = "List"
) -> List[Any]:
    """
    Validate a list input with optional constraints.

    Args:
        value (List[Any]): The list to validate
        min_length (Optional[int], optional): Minimum list length. Defaults to None.
        max_length (Optional[int], optional): Maximum list length. Defaults to None.
        item_type (Optional[type], optional): Expected type of list items. Defaults to None.
        field_name (str, optional): Name of the field for error message. Defaults to "List".

    Returns:
        List[Any]: The validated list

    Raises:
        ValidationError: If the list does not meet the specified constraints
    """
    validate_type(value, list, field_name)
    
    if min_length is not None and len(value) < min_length:
        raise ValidationError(f"{field_name} must contain at least {min_length} items")
    
    if max_length is not None and len(value) > max_length:
        raise ValidationError(f"{field_name} must contain no more than {max_length} items")
    
    if item_type is not None:
        for i, item in enumerate(value):
            try:
                validate_type(item, item_type, f"{field_name} item at index {i}")
            except ValidationError as e:
                raise ValidationError(str(e))
    
    return value