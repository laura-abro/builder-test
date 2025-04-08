import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factorization(2) == {2: 1}
    assert prime_factorization(12) == {2: 2, 3: 1}
    assert prime_factorization(15) == {3: 1, 5: 1}
    assert prime_factorization(100) == {2: 2, 5: 2}

def test_prime_factorization_prime_numbers():
    """Test prime numbers themselves."""
    assert prime_factorization(7) == {7: 1}
    assert prime_factorization(17) == {17: 1}
    assert prime_factorization(29) == {29: 1}

def test_prime_factorization_large_number():
    """Test a larger number with multiple prime factors."""
    assert prime_factorization(84) == {2: 2, 3: 1, 7: 1}

def test_prime_factorization_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(TypeError):
        prime_factorization("not an int")
    
    with pytest.raises(TypeError):
        prime_factorization(3.14)
    
    with pytest.raises(ValueError):
        prime_factorization(1)
    
    with pytest.raises(ValueError):
        prime_factorization(0)
    
    with pytest.raises(ValueError):
        prime_factorization(-10)

def test_prime_factorization_edge_cases():
    """Test various edge cases."""
    # Smallest prime
    assert prime_factorization(2) == {2: 1}
    
    # Larger prime
    assert prime_factorization(997) == {997: 1}
    
    # Composite number with repeated prime factors
    assert prime_factorization(64) == {2: 6}