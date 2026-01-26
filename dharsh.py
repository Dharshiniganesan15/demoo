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

def multiply(a, b, *args, debug=False):
    """Multiply multiple numbers together with logging and validation.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        *args: Additional numbers to multiply
        debug (bool): Enable debug output
        
    Returns:
        int/float: Product of all numbers
        
    Raises:
        TypeError: If any argument is not a number
    """
    if not all(isinstance(x, (int, float)) for x in [a, b] + list(args)):
        raise TypeError("All arguments must be numbers")

    if debug:
        print(f"[DEBUG] Multiplying: {a} * {b} * {args}")

    print(f"[{datetime.datetime.now()}] Multiplying numbers")
    result = a * b
    for num in args:
        result *= num

    if debug:
        print(f"[DEBUG] Result: {result}")

    return result

def divide(a, b, *args, debug=False):
    """Divide multiple numbers sequentially with logging and validation.
    
    Args:
        a (int/float): First number
        b (int/float): Second number (divisor)
        *args: Additional divisors (applied in order)
        debug (bool): Enable debug output
        
    Returns:
        int/float: Result of sequential division
        
    Raises:
        TypeError: If any argument is not a number
        ZeroDivisionError: If any divisor is zero
    """
    if not all(isinstance(x, (int, float)) for x in [a, b] + list(args)):
        raise TypeError("All arguments must be numbers")

    divisors = [b] + list(args)
    if any(d == 0 for d in divisors):
        raise ZeroDivisionError("Division by zero is not allowed")

    if debug:
        print(f"[DEBUG] Dividing: {a} / {b} / {args}")

    print(f"[{datetime.datetime.now()}] Dividing numbers")
    result = a / b
    for d in args:
        result /= d

    if debug:
        print(f"[DEBUG] Result: {result}")

    return result