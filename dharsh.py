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

def concat(a, b, *args, sep="", debug=False):
    """Concatenate multiple values into a single string.
    
    Args:
        a: First value
        b: Second value
        *args: Additional values
        sep (str): Separator inserted between values
        debug (bool): Enable debug output
        
    Returns:
        str: Concatenated string
    """
    parts = [str(a), str(b)] + [str(x) for x in args]

    if debug:
        print(f"[DEBUG] Concatenating {len(parts)} parts with sep={sep!r}")

    print(f"[{datetime.datetime.now()}] Concatenating strings")
    return sep.join(parts)


def factorial(n, debug=False):
    """Compute factorial of a non-negative integer.
    
    Args:
        n (int): Non-negative integer
        debug (bool): Enable debug output
        
    Returns:
        int: Factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
    """
    if not isinstance(n, int):
        raise TypeError("Factorial input must be an integer")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    if debug:
        print(f"[DEBUG] Computing factorial({n})")

    print(f"[{datetime.datetime.now()}] Calculating factorial")
    result = 1
    for i in range(2, n + 1):
        result *= i
        if debug:
            print(f"[DEBUG] Step {i}: result = {result}")

    if debug:
        print(f"[DEBUG] Final factorial({n}) = {result}")

    return result

def power(base, exp, debug=False):
    """Calculate base^exp with logging."""
    if debug:
        print(f"[DEBUG] Calculating {base}^{exp}")
    result = base ** exp
    return result

def to_uppercase(text, debug=False):
    """Convert text to uppercase with logging.
    
    Args:
        text (str): Input text to convert
        debug (bool): Enable debug output
        
    Returns:
        str: Uppercase version of the input text
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if debug:
        print(f"[DEBUG] Converting to uppercase: {text!r}")
    
    print(f"[{datetime.datetime.now()}] Converting text to uppercase")
    result = text.upper()
    
    if debug:
        print(f"[DEBUG] Result: {result!r}")
    
    return result


def reverse_string(text, debug=False):
    """Reverse a string with logging.
    
    Args:
        text (str): Input text to reverse
        debug (bool): Enable debug output
        
    Returns:
        str: Reversed version of the input text
        
    Raises:
        TypeError: If input is not a string
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")
    
    if debug:
        print(f"[DEBUG] Reversing string: {text!r}")
    
    print(f"[{datetime.datetime.now()}] Reversing string")
    result = text[::-1]
    
    if debug:
        print(f"[DEBUG] Result: {result!r}")
    
    return result


def calculate_average(numbers, debug=False):
    """Calculate the average (mean) of a list of numbers.
    
    Args:
        numbers (list): List of numbers to calculate average
        debug (bool): Enable debug output
        
    Returns:
        float: Average of the numbers
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements in the list must be numbers")
    
    if debug:
        print(f"[DEBUG] Calculating average of {len(numbers)} numbers: {numbers}")
    
    print(f"[{datetime.datetime.now()}] Calculating average")
    total = sum(numbers)
    count = len(numbers)
    result = total / count
    
    if debug:
        print(f"[DEBUG] Sum: {total}, Count: {count}, Average: {result}")
    
    return result