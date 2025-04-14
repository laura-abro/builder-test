from src.prime_factorization import prime_factorization
from collections import Counter

def gcd_using_prime_factors(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization method.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The Greatest Common Divisor of a and b
    
    Raises:
        ValueError: If either input is less than or equal to 0
    """
    # Validate inputs
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Get prime factorizations of both numbers
    a_factors = Counter(prime_factorization(a))
    b_factors = Counter(prime_factorization(b))
    
    # Find common prime factors with their minimum exponents
    gcd_factors = {}
    for prime in set(a_factors.keys()) & set(b_factors.keys()):
        gcd_factors[prime] = min(a_factors[prime], b_factors[prime])
    
    # Calculate GCD by multiplying common prime factors
    result = 1
    for prime, power in gcd_factors.items():
        result *= prime ** power
    
    return result