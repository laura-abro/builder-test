"""
Input Validation Utility Module

This module provides robust input validation functions to handle 
various input types and constraints with comprehensive error handling.
"""

import re
from typing import Any, Union, List, Optional


class ValidationError(ValueError):
    """Custom exception for input validation errors."""
    pass


def validate_string(
    value: Any, 
    min_length: Optional[int] = None, 
    max_length: Optional[int] = None, 
    regex: Optional[str] = None, 
    allow_empty: bool = False
) -> str:
    """
    Validate and sanitize string input.
    
    Args:
        value: Input to validate
        min_length: Minimum allowed string length
        max_length: Maximum allowed string length
        regex: Optional regex pattern for validation
        allow_empty: Whether empty strings are allowed
    
    Returns:
        Validated and cleaned string
    
    Raises:
        ValidationError: If input fails validation
    """
    # Check if input is None
    if value is None:
        raise ValidationError("Input cannot be None")
    
    # Convert to string
    try:
        str_value = str(value).strip()
    except Exception:
        raise ValidationError("Input must be convertible to string")
    
    # Check empty string
    if not allow_empty and str_value == "":
        raise ValidationError("Input cannot be an empty string")
    
    # Check minimum length
    if min_length is not None and len(str_value) < min_length:
        raise ValidationError(f"Input must be at least {min_length} characters long")
    
    # Check maximum length
    if max_length is not None and len(str_value) > max_length:
        raise ValidationError(f"Input must be no more than {max_length} characters long")
    
    # Check regex pattern
    if regex is not None:
        if not re.match(regex, str_value):
            raise ValidationError(f"Input does not match required pattern: {regex}")
    
    return str_value


def validate_number(
    value: Any, 
    min_value: Optional[Union[int, float]] = None, 
    max_value: Optional[Union[int, float]] = None, 
    is_integer: bool = False
) -> Union[int, float]:
    """
    Validate numeric input.
    
    Args:
        value: Input to validate
        min_value: Minimum allowed value
        max_value: Maximum allowed value
        is_integer: Whether input must be an integer
    
    Returns:
        Validated numeric value
    
    Raises:
        ValidationError: If input fails validation
    """
    # Check if input is None
    if value is None:
        raise ValidationError("Input cannot be None")
    
    # Convert and validate input
    try:
        # Attempt to convert to float first
        num_value = float(value)
        
        # Check if integer is required
        if is_integer and not num_value.is_integer():
            raise ValidationError("Input must be an integer")
        
        # Convert to int if integer is required
        num_value = int(num_value) if is_integer else num_value
    except ValueError:
        raise ValidationError("Input must be a valid number")
    
    # Check minimum value
    if min_value is not None and num_value < min_value:
        raise ValidationError(f"Input must be at least {min_value}")
    
    # Check maximum value
    if max_value is not None and num_value > max_value:
        raise ValidationError(f"Input must be no more than {max_value}")
    
    return num_value


def validate_list(
    value: Any, 
    min_items: Optional[int] = None, 
    max_items: Optional[int] = None, 
    item_validator: Optional[callable] = None
) -> List[Any]:
    """
    Validate list input.
    
    Args:
        value: Input to validate
        min_items: Minimum number of items
        max_items: Maximum number of items
        item_validator: Optional function to validate individual items
    
    Returns:
        Validated list
    
    Raises:
        ValidationError: If input fails validation
    """
    # Check if input is None
    if value is None:
        raise ValidationError("Input cannot be None")
    
    # Convert to list
    try:
        list_value = list(value)
    except Exception:
        raise ValidationError("Input must be convertible to a list")
    
    # Check minimum items
    if min_items is not None and len(list_value) < min_items:
        raise ValidationError(f"List must have at least {min_items} items")
    
    # Check maximum items
    if max_items is not None and len(list_value) > max_items:
        raise ValidationError(f"List must have no more than {max_items} items")
    
    # Validate individual items if a validator is provided
    if item_validator is not None:
        validated_list = []
        for item in list_value:
            try:
                validated_item = item_validator(item)
                validated_list.append(validated_item)
            except Exception as e:
                raise ValidationError(f"List item validation failed: {str(e)}")
        return validated_list
    
    return list_value