import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(12) == {2: 2, 3: 1}
    assert prime_factorization(15) == {3: 1, 5: 1}
    assert prime_factorization(100) == {2: 2, 5: 2}

def test_prime_factorization_prime_numbers():
    """Test prime numbers are correctly factorized."""
    assert prime_factorization(7) == {7: 1}
    assert prime_factorization(11) == {11: 1}
    assert prime_factorization(17) == {17: 1}

def test_prime_factorization_special_cases():
    """Test special cases like 1 and large numbers."""
    assert prime_factorization(1) == {}
    assert prime_factorization(2) == {2: 1}
    assert prime_factorization(997) == {997: 1}  # Large prime

def test_prime_factorization_complex_numbers():
    """Test more complex prime factorization scenarios."""
    assert prime_factorization(84) == {2: 2, 3: 1, 7: 1}
    assert prime_factorization(360) == {2: 3, 3: 2, 5: 1}

def test_prime_factorization_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factorization(-10)
    
    with pytest.raises(ValueError, match="Input must be an integer"):
        prime_factorization("not a number")