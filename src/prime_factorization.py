def prime_factorization(n):
    """
    Compute the prime factorization of a given positive integer.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is less than 2.
    """
    # Validate input
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be greater than or equal to 2")
    
    # Initialize list to store prime factors
    factors = []
    
    # Start with the smallest prime number
    divisor = 2
    
    # Continue until the number is fully factorized
    while divisor * divisor <= n:
        # If divisor divides n, add it to factors
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            # If not divisible, move to next potential divisor
            divisor += 1
    
    # If n is still greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors