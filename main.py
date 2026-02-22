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

def average(a: float, b: float) -> float:
    """Return the average of two numbers."""
    return (a + b) / 2

def max_of_two(a: float, b: float) -> float:
    """Return the larger of two numbers."""
    return a if a >= b else b

# Test with Gemini AI documentation - 2026-01-30
