def add(a, b, *args):
    """Add multiple numbers together.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        *args: Additional numbers to add
        
    Returns:
        int/float: Sum of all numbers
    """
    result = a + b
    for num in args:
        result += num
    return result

def subtract(a, b):
    """Subtract two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Difference of a and b
    """ result = a - b
    
    return result

def multiply(a, b):
    """Multiply two numbers.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        
    Returns:
        int/float: Product of a and b
    """
    return a * b