def sum(a,b):return a+b
def sub (a,b):return a-b
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide two numbers safely."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Updated: Testing auto-doc generation 2026-01-30