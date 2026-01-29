import math
import statistics
from typing import List, Union

def find_max(numbers: List[float]) -> float:
    """Find the maximum value in a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return max(numbers)



def calculate_average(numbers: List[float]) -> float:
    """Calculate the average of a list of numbers."""
    if not numbers:
        raise ValueError("List cannot be empty")
    return sum(numbers) / len(numbers)

def factorial(n: int) -> int:
    """Calculate the factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def power(base: float, exponent: float) -> float:
    """Calculate base raised to the power of exponent."""
    return base ** exponent

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reverse_string(text: str) -> str:
    """Reverse a given string."""
    return text[::-1]

def count_vowels(text: str) -> int:
    """Count the number of vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def fibonacci(n: int) -> List[int]:
    """Generate Fibonacci sequence up to n terms."""
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

def calculate_discount(original_price: float, discount_percentage: float) -> float:
    """Calculate discounted price."""
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    return original_price * (1 - discount_percentage / 100)

def analyze_data(numbers: List[float]) -> dict:
    """Analyze a list of numbers and return statistics."""
    if not numbers:
        raise ValueError("List cannot be empty")
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "mode": statistics.mode(numbers) if len(set(numbers)) != len(numbers) else None,
        "min": min(numbers),
        "max": max(numbers),
        "range": max(numbers) - min(numbers),
        "std_dev": statistics.stdev(numbers) if len(numbers) > 1 else 0
    }

# Example usage and testing
if __name__ == "__main__":
    # Test functions
    numbers = [1, 5, 3, 9, 2, 8, 4, 6, 7]
    
    print("=== Math Operations ===")
    print(f"Numbers: {numbers}")
    print(f"Max: {find_max(numbers)}")
    print(f"Min: {find_min(numbers)}")
    print(f"Average: {calculate_average(numbers)}")
    print(f"Factorial of 5: {factorial(5)}")
    print(f"2^3: {power(2, 3)}")
    print(f"Is 17 prime? {is_prime(17)}")
    
    print("\n=== String Operations ===")
    text = "Hello World"
    print(f"Original: {text}")
    print(f"Reversed: {reverse_string(text)}")
    print(f"Vowels count: {count_vowels(text)}")
    
    print("\n=== Fibonacci ===")
    print(f"First 10 terms: {fibonacci(10)}")
    
    print("\n=== Temperature Conversion ===")
    print(f"25°C to Fahrenheit: {celsius_to_fahrenheit(25)}")
    print(f"77°F to Celsius: {fahrenheit_to_celsius(77)}")
    
    print("\n=== Discount Calculation ===")
    print(f"20% off $100: ${calculate_discount(100, 20)}")
    
    print("\n=== Data Analysis ===")
    analysis = analyze_data(numbers)
    for key, value in analysis.items():
        print(f"{key}: {value}")