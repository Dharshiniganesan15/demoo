def add(a, b, *args):
    """Add multiple numbers together with timestamp.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        *args: Additional numbers to add
        
    Returns:
        int/float: Sum of all numbers
    """
    print(f"[{datetime.now()}] Adding numbers")  # Add this import at top
    result = a + b
    for num in args:
        result += num
    return result
    