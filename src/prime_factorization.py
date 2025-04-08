from src.is_prime import is_prime
from collections import Counter

def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        dict: A dictionary with prime factors as keys and their frequencies as values.
    
    Raises:
        ValueError: If the input is less than 2.
        TypeError: If the input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case first
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            # Verify factor is prime
            if is_prime(factor):
                factors.append(factor)
                n //= factor
            else:
                factor += 2
        else:
            factor += 2
    
    # If n is a prime number greater than 2
    if n > 2 and is_prime(n):
        factors.append(n)
    
    # Use Counter to convert list to frequency dictionary
    return dict(Counter(factors))