def sum(a, b):
    """Add two numbers together."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers together."""
    return a * b

def divide(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def calculate_tax(income: float) -> float:
    """Calculate tax on income at 10% rate."""
    return income * 0.1

def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discount amount on price."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price * (discount_percent / 100)

def average(a: float, b: float) -> float:
    """Return the average of two numbers."""
    return (a + b) / 2

def max_of_two(a: float, b: float) -> float:
    """Return the larger of two numbers."""
    return a if a >= b else b

def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]

def fibonacci(n: int) -> int:
    """Calculate the nth Fibonacci number using iteration.
    
    Args:
        n (int): The position in the Fibonacci sequence (0-indexed)
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
    """
    if n < 0:
        raise ValueError("Fibonacci number is not defined for negative numbers")
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        
    Examples:
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Test with Gemini AI documentation - 2026-01-30
