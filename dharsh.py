import datetime

def add(a, b, *args, debug=False):
    """Add multiple numbers together with enhanced logging and validation.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        *args: Additional numbers to add
        debug (bool): Enable debug output
        
    Returns:
        int/float: Sum of all numbers
        
    Raises:
        TypeError: If any argument is not a number
    """
    # Add validation
    if not all(isinstance(x, (int, float)) for x in [a, b] + list(args)):
        raise TypeError("All arguments must be numbers")
    
    if debug:
        print(f"[DEBUG] Adding: {a} + {b} + {args}")
    
    print(f"[{datetime.datetime.now()}] Adding numbers")
    result = a + b
    for num in args:
        result += num
    
    if debug:
        print(f"[DEBUG] Result: {result}")
    
    return result

def multiply(a, b, debug=False):
    """Multiply two numbers with logging and validation.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        debug (bool): Enable debug output
        
    Returns:
        int/float: Product of the numbers
        
    Raises:
        TypeError: If any argument is not a number
    """
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("All arguments must be numbers")
    
    if debug:
        print(f"[DEBUG] Multiplying: {a} * {b}")
    
    print(f"[{datetime.datetime.now()}] Multiplying numbers")
    result = a * b
    
    if debug:
        print(f"[DEBUG] Result: {result}")
    
    return result

def divide(a, b, debug=False):
    
    if not all(isinstance(x, (int, float)) for x in [a, b]):
        raise TypeError("All arguments must be numbers")
    
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    
    if debug:
        print(f"[DEBUG] Dividing: {a} / {b}")
    
    print(f"[{datetime.datetime.now()}] Dividing numbers")
    result = a / b
    
    if debug:
        print(f"[DEBUG] Result: {result}")
    
    return result

