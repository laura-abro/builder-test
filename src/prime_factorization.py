from collections import Counter
from src.is_prime import is_prime

def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        dict: A dictionary of prime factors and their frequencies, 
              where keys are prime factors and values are their counts.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Check for valid input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Handle special case for 1
    if n == 1:
        return {}
    
    # Dictionary to store prime factors and their frequencies
    factors = {}
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor^2 <= n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Verify the divisor is prime
            if not is_prime(divisor):
                raise ValueError(f"Unexpected non-prime divisor: {divisor}")
            
            # Increment the factor count
            factors[divisor] = factors.get(divisor, 0) + 1
            
            # Divide n by the divisor
            n //= divisor
        else:
            # If not divisible, move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        if not is_prime(n):
            raise ValueError(f"Unexpected non-prime factor: {n}")
        factors[n] = factors.get(n, 0) + 1
    
    return factors