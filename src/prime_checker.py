def is_prime(n):
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    
    Args:
        n (int): The number to check for primality.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    
    Raises:
        TypeError: If the input is not an integer.
        ValueError: If the input is less than or equal to 0.
    """
    # Check input type
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    
    # Check input range
    if n <= 0:
        raise ValueError("Input must be a positive integer greater than 0")
    
    # Handle small prime numbers
    if n == 1:
        return False
    if n <= 3:
        return True
    
    # Optimize for even numbers
    if n % 2 == 0:
        return False
    
    # Check for divisibility up to the square root of n
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True