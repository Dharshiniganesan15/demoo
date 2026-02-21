def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    
    # Initialize DP table
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    
    # Fill DP table
    for i in range(3, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    
    return fib[n]

def test_fibonacci():
    """Test the Fibonacci function"""
    test_cases = [0, 1, 2, 3, 5, 8, 13, 21, 34]
    
    print("Testing Fibonacci function:")
    for i, expected in enumerate(test_cases):
        result = calculate_fibonacci(i)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"  fib({i}) = {result} (expected {expected}) {status}")

if __name__ == "__main__":
    test_fibonacci()
