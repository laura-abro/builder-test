import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios"""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    """Test prime numbers have themselves as their only factor"""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(17) == [17]

def test_prime_factorization_edge_cases():
    """Test edge cases"""
    assert prime_factorization(1) == []  # Special case
    assert prime_factorization(2) == [2]
    assert prime_factorization(4) == [2, 2]

def test_prime_factorization_large_number():
    """Test larger numbers"""
    assert prime_factorization(84) == [2, 2, 3, 7]
    assert prime_factorization(360) == [2, 2, 2, 3, 3, 5]

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)