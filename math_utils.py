"""
Math utilities for basic operations
"""

def multiply(a, b):
    """Multiply two numbers together."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent
