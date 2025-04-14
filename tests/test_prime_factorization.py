import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization cases."""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    """Test prime numbers."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(17) == [17]

def test_prime_factorization_one():
    """Test factorization of 1."""
    assert prime_factorization(1) == []

def test_prime_factorization_edge_cases():
    """Test edge cases and error handling."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)

def test_prime_factorization_large_number():
    """Test a larger number with multiple prime factors."""
    assert prime_factorization(84) == [2, 2, 3, 7]