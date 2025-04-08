import pytest
from src.prime_factorization import prime_factorization, is_prime

def test_is_prime():
    """Test the is_prime function."""
    # Known prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    assert is_prime(17) == True
    assert is_prime(29) == True

    # Known non-prime numbers
    assert is_prime(1) == False
    assert is_prime(0) == False
    assert is_prime(-5) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(15) == False
    assert is_prime(100) == False

    # Error cases
    with pytest.raises(ValueError, match="Input must be an integer"):
        is_prime("12")

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]

def test_prime_factorization_prime_numbers():
    """Test prime numbers are correctly factorized."""
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(17) == [17]

def test_prime_factorization_edge_cases():
    """Test edge case scenarios."""
    assert prime_factorization(1) == []  # Special case
    assert prime_factorization(2) == [2]
    assert prime_factorization(4) == [2, 2]

def test_prime_factorization_large_number():
    """Test a larger composite number."""
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("12")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-5)