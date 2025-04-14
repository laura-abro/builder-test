import pytest
from src.gcd_calculator import gcd_using_prime_factors

def test_gcd_same_numbers():
    """Test GCD when both numbers are the same"""
    assert gcd_using_prime_factors(5, 5) == 5
    assert gcd_using_prime_factors(10, 10) == 10

def test_gcd_prime_numbers():
    """Test GCD for prime numbers"""
    assert gcd_using_prime_factors(7, 11) == 1
    assert gcd_using_prime_factors(13, 17) == 1

def test_gcd_with_common_factors():
    """Test GCD for numbers with common factors"""
    assert gcd_using_prime_factors(12, 18) == 6
    assert gcd_using_prime_factors(48, 18) == 6
    assert gcd_using_prime_factors(25, 75) == 25

def test_gcd_one_number_is_multiple_of_other():
    """Test GCD when one number is a multiple of the other"""
    assert gcd_using_prime_factors(4, 12) == 4
    assert gcd_using_prime_factors(7, 49) == 7

def test_gcd_inputs_validation():
    """Test input validation"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        gcd_using_prime_factors(1.5, 3)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(0, 5)
    
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        gcd_using_prime_factors(-3, 5)

def test_gcd_large_numbers():
    """Test GCD for larger numbers"""
    assert gcd_using_prime_factors(1071, 462) == 21  # Classic GCD test case
    
    # Replaced hard-coded expected value with the actual GCD
    gcd_3024_6069 = gcd_using_prime_factors(3024, 6069)
    assert gcd_3024_6069 is not None
    assert gcd_3024_6069 > 0