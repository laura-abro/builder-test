"""
Input Validation and Error Handling Module

This module provides utility functions for validating and sanitizing inputs
with comprehensive error handling.
"""

class ValidationError(Exception):
    """Custom exception for input validation errors."""
    pass

def validate_email(email: str) -> str:
    """
    Validate and sanitize an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        str: The sanitized email address.

    Raises:
        ValidationError: If the email is invalid.
    """
    # Remove leading/trailing whitespace
    email = email.strip()

    # Check for empty email
    if not email:
        raise ValidationError("Email cannot be empty")

    # Basic email validation regex
    import re
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        raise ValidationError(f"Invalid email format: {email}")

    # Convert to lowercase for consistency
    return email.lower()

def validate_age(age: int) -> int:
    """
    Validate an age value.

    Args:
        age (int): The age to validate.

    Returns:
        int: The validated age.

    Raises:
        ValidationError: If the age is invalid.
    """
    # Check if age is an integer
    if not isinstance(age, int):
        raise ValidationError(f"Age must be an integer, got {type(age)}")

    # Check age range
    if age < 0:
        raise ValidationError(f"Age cannot be negative, got {age}")
    
    if age > 150:
        raise ValidationError(f"Age is implausibly high, got {age}")

    return age

def validate_phone_number(phone: str) -> str:
    """
    Validate and sanitize a phone number.

    Args:
        phone (str): The phone number to validate.

    Returns:
        str: The sanitized phone number.

    Raises:
        ValidationError: If the phone number is invalid.
    """
    # Remove all non-digit characters
    import re
    digits_only = re.sub(r'\D', '', phone)

    # Check length (assuming US/international phone number conventions)
    if len(digits_only) < 10 or len(digits_only) > 15:
        raise ValidationError(f"Invalid phone number length: {phone}")

    return digits_only