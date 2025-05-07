def prime_factorization(n):
    """
    Compute the prime factorization of a given integer.
    
    Args:
        n (int): The number to factorize. Must be a positive integer.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    
    # Handle special cases
    if n < 1:
        raise ValueError("Input must be a positive integer")
    
    # Special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Handle 2 as a special case to simplify the main loop
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd prime factors
    # We only need to check up to sqrt(n)
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
        else:
            factor += 2
    
    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
    
    return factors