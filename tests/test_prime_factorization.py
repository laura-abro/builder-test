import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    assert prime_factorization(2) == [2]
    assert prime_factorization(17) == [17]
    assert prime_factorization(23) == [23]

def test_prime_factorization_edge_cases():
    assert prime_factorization(1) == []

def test_prime_factorization_large_number():
    result = prime_factorization(84)
    assert result == [2, 2, 3, 7]
    assert all(is_prime(factor) for factor in result)

def test_prime_factorization_invalid_inputs():
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not an int")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)

def is_prime(n):
    """Helper function to check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True