def is_prime(n):
    """
    Check if a given number is prime.

    Args:
        n (int): A positive integer to check for primality.

    Returns:
        bool: True if the number is prime, False otherwise.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 1:
        return False
    
    # 2 is the only even prime number
    if n == 2:
        return True
    
    # Even numbers greater than 2 are not prime
    if n % 2 == 0:
        return False
    
    # Check odd factors up to sqrt(n)
    for factor in range(3, int(n**0.5) + 1, 2):
        if n % factor == 0:
            return False
    
    return True

def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.

    Args:
        n (int): A positive integer to factorize.

    Returns:
        list: A list of prime factors in ascending order.

    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Try to divide by prime factors
    for potential_factor in range(2, int(n**0.5) + 1):
        # Only use prime factors
        if is_prime(potential_factor):
            # Keep dividing while divisible
            while n % potential_factor == 0:
                factors.append(potential_factor)
                n //= potential_factor
    
    # If the remaining number is greater than 1, it must be a prime
    if n > 1:
        factors.append(n)
    
    return factors