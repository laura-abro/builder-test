def is_prime(n):
    """
    Check if a given number is prime.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        ValueError: If input is less than 2.
        TypeError: If input is not an integer.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    if n < 2:
        raise ValueError("Input must be a positive integer greater than or equal to 2")
    
    # Special cases
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    # Check odd factors up to square root of n
    for factor in range(3, int(n**0.5) + 1, 2):
        if n % factor == 0:
            return False
    
    return True