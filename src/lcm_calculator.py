def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate input
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers using GCD.
    
    LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First positive integer
        b (int): Second positive integer
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
        TypeError: If inputs are not integers
    """
    # Validate input
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers")
    
    if a <= 0 or b <= 0:
        raise ValueError("Inputs must be positive integers")
    
    # Calculate LCM using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)