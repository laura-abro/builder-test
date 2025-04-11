import pytest
from src.prime_factorization import prime_factorization

def test_prime_factorization_basic():
    assert prime_factorization(12) == [2, 2, 3]
    assert prime_factorization(15) == [3, 5]
    assert prime_factorization(100) == [2, 2, 5, 5]
    assert prime_factorization(2) == [2]

def test_prime_factorization_prime_numbers():
    assert prime_factorization(7) == [7]
    assert prime_factorization(11) == [11]
    assert prime_factorization(13) == [13]

def test_prime_factorization_large_number():
    assert prime_factorization(84) == [2, 2, 3, 7]

def test_prime_factorization_invalid_input():
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(1)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(0)
    
    with pytest.raises(ValueError, match="Input must be greater than or equal to 2"):
        prime_factorization(-5)

def test_prime_factorization_type_error():
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(3.14)
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization("12")
    
    with pytest.raises(TypeError, match="Input must be an integer"):
        prime_factorization(None)