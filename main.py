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

# Test with Gemini AI documentation - 2026-01-30
