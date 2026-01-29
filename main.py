from typing import List

def find_min(numbers: List[float]) -> float:
    """Find the minimum value in a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return min(numbers)

def find_max(numbers: List[float]) -> float:
    """Find the maximum value in a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)


#