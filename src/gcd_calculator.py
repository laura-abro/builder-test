from collections import Counter
from src.prime_factorization import prime_factorization

def gcd_using_prime_factors(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) using prime factorization.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # If inputs are the same, return the input
    if a == b:
        return a
    
    # Get prime factorizations
    a_factors = Counter(prime_factorization(a))
    b_factors = Counter(prime_factorization(b))
    
    # Find common prime factors
    gcd = 1
    for prime, count in a_factors.items():
        if prime in b_factors:
            # Take the minimum count of each common prime factor
            gcd *= prime ** min(count, b_factors[prime])
    
    return gcd