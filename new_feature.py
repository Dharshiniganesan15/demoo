def advanced_calculator():
    """
    Advanced calculator with multiple operations.
    Supports addition, subtraction, multiplication, and division.
    """
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def modulo(a, b):
        if b == 0:
            return "Error: Modulo by zero"
        return a % b
    
    def power(base, exponent):
        result = 1
        for _ in range(exponent):
            result *= base
        return result
    
    def factorial(n):
        if n < 0:
            return "Error: Negative number"
        elif n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def test_calculator():
    """Test the advanced calculator"""
    print("Testing Advanced Calculator:")
    
    # Test addition
    result = advanced_calculator.add(5, 3)
    print(f"  5 + 3 = {result} {'✅' if result == 8 else '❌'}")
    
    # Test subtraction
    result = advanced_calculator.subtract(10, 4)
    print(f"  10 - 4 = {result} {'✅' if result == 6 else '❌'}")
    
    # Test multiplication
    result = advanced_calculator.multiply(7, 6)
    print(f"  7 * 6 = {result} {'✅' if result == 42 else '❌'}")
    
    # Test division
    result = advanced_calculator.divide(15, 3)
    print(f"  15 / 3 = {result} {'✅' if result == 5 else '❌'}")
    
    # Test power
    result = advanced_calculator.power(2, 8)
    print(f"  2^8 = {result} {'✅' if result == 256 else '❌'}")
    
    # Test factorial
    result = advanced_calculator.factorial(5)
    print(f"  5! = {result} {'✅' if result == 120 else '❌'}")

if __name__ == "__main__":
    test_calculator()
