


def find_max(numbers, debug=False):
    """Find the maximum value in a list of numbers.
    
    Args:
        numbers (list): List of numbers to find maximum
        debug (bool): Enable debug output
        
    Returns:
        int/float: Maximum value in the list
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers")
    
    if not numbers:
        raise ValueError("Cannot find maximum of empty list")
    
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("All elements in the list must be numbers")
    
    if debug:
        print(f"[DEBUG] Finding maximum in {len(numbers)} numbers: {numbers}")
    
    print(f"[{datetime.datetime.now()}] Finding maximum value")
    result = max(numbers)
    
    if debug:
        print(f"[DEBUG] Maximum value found: {result}")
    
    return result

