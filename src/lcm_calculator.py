def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclidean algorithm.
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The greatest common divisor of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Ensure positive inputs
    a, b = abs(a), abs(b)
    
    # Euclidean algorithm
    while b:
        a, b = b, a % b
    
    return a

def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers using GCD.
    
    LCM(a,b) = |a * b| / GCD(a,b)
    
    Args:
        a (int): First integer
        b (int): Second integer
    
    Returns:
        int: The least common multiple of a and b
    
    Raises:
        ValueError: If either input is not a positive integer
    """
    # Validate inputs
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Inputs must be integers")
    
    # Handle zero case
    if a == 0 or b == 0:
        return 0
    
    # Calculate LCM using the formula: LCM(a,b) = |a * b| / GCD(a,b)
    return abs(a * b) // gcd(a, b)

def lcm_multiple(*numbers: int) -> int:
    """
    Calculate the LCM of multiple numbers.
    
    Args:
        *numbers (int): Variable number of integers
    
    Returns:
        int: The least common multiple of all input numbers
    
    Raises:
        ValueError: If no numbers are provided or inputs are not integers
    """
    # Validate input
    if not numbers:
        raise ValueError("At least one number must be provided")
    
    # Validate all inputs are integers
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All inputs must be integers")
    
    # Start with the first number
    result = numbers[0]
    
    # Iterate through remaining numbers, calculating LCM
    for num in numbers[1:]:
        result = lcm(result, num)
    
    return result