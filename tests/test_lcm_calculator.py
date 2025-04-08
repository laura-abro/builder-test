import pytest
from src.lcm_calculator import gcd, lcm

def test_gcd_basic():
    """Test basic GCD calculations"""
    assert gcd(48, 18) == 6
    assert gcd(54, 24) == 6
    assert gcd(17, 23) == 1

def test_lcm_basic():
    """Test basic LCM calculations"""
    assert lcm(4, 6) == 12
    assert lcm(21, 6) == 42
    assert lcm(17, 23) == 391

def test_gcd_same_number():
    """Test GCD when both numbers are the same"""
    assert gcd(5, 5) == 5
    assert gcd(100, 100) == 100

def test_lcm_same_number():
    """Test LCM when both numbers are the same"""
    assert lcm(5, 5) == 5
    assert lcm(100, 100) == 100

def test_gcd_one_number_is_one():
    """Test GCD when one number is 1"""
    assert gcd(1, 5) == 1
    assert gcd(5, 1) == 1

def test_lcm_one_number_is_one():
    """Test LCM when one number is 1"""
    assert lcm(1, 5) == 5
    assert lcm(5, 1) == 5

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Negative numbers
    with pytest.raises(ValueError):
        gcd(-1, 5)
    with pytest.raises(ValueError):
        gcd(5, -1)
    with pytest.raises(ValueError):
        lcm(-1, 5)
    with pytest.raises(ValueError):
        lcm(5, -1)

    # Zero values
    with pytest.raises(ValueError):
        gcd(0, 5)
    with pytest.raises(ValueError):
        gcd(5, 0)
    with pytest.raises(ValueError):
        lcm(0, 5)
    with pytest.raises(ValueError):
        lcm(5, 0)

    # Non-integer inputs
    with pytest.raises(TypeError):
        gcd(1.5, 5)
    with pytest.raises(TypeError):
        gcd(5, 1.5)
    with pytest.raises(TypeError):
        lcm(1.5, 5)
    with pytest.raises(TypeError):
        lcm(5, 1.5)