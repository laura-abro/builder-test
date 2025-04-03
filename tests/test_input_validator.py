"""
Tests for Input Validation Module
"""

import pytest
from src.input_validator import validate_email, validate_age, validate_phone_number, ValidationError

def test_validate_email_valid():
    """Test valid email addresses."""
    assert validate_email("test@example.com") == "test@example.com"
    assert validate_email("  user@domain.org  ") == "user@domain.org"
    assert validate_email("UPPERCASE@DOMAIN.COM") == "uppercase@domain.com"

def test_validate_email_invalid():
    """Test invalid email addresses."""
    with pytest.raises(ValidationError, match="Invalid email format"):
        validate_email("invalid-email")
    
    with pytest.raises(ValidationError, match="Invalid email format"):
        validate_email("missing@domain")
    
    with pytest.raises(ValidationError, match="Email cannot be empty"):
        validate_email("")
    
    with pytest.raises(ValidationError, match="Email cannot be empty"):
        validate_email("   ")

def test_validate_age_valid():
    """Test valid age values."""
    assert validate_age(25) == 25
    assert validate_age(0) == 0
    assert validate_age(150) == 150

def test_validate_age_invalid():
    """Test invalid age values."""
    with pytest.raises(ValidationError, match="Age cannot be negative"):
        validate_age(-1)
    
    with pytest.raises(ValidationError, match="Age is implausibly high"):
        validate_age(151)
    
    with pytest.raises(ValidationError, match="Age must be an integer"):
        validate_age("25")
    
    with pytest.raises(ValidationError, match="Age must be an integer"):
        validate_age(25.5)

def test_validate_phone_number_valid():
    """Test valid phone number formats."""
    assert validate_phone_number("1234567890") == "1234567890"
    assert validate_phone_number("+1 (123) 456-7890") == "11234567890"
    assert validate_phone_number("123-456-7890") == "1234567890"

def test_validate_phone_number_invalid():
    """Test invalid phone number formats."""
    with pytest.raises(ValidationError, match="Invalid phone number length"):
        validate_phone_number("123")
    
    with pytest.raises(ValidationError, match="Invalid phone number length"):
        validate_phone_number("123456789012345678")