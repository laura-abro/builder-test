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
    
    # Handle special case for 1
    if n == 1:
        return []
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue factoring while divisor * divisor <= n
    while divisor * divisor <= n:
        # If divisor divides n evenly
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        
        # Move to next potential divisor
        divisor += 1
    
    # If n is greater than 1, it means n itself is prime
    if n > 1:
        factors.append(n)
    
    return factors