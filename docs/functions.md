# Function Documentation


None
---

## calculate_discount

**Signature:** `def calculate_discount(price: float, discount_percent: float)`

**Summary:** Calculate discount amount on price.

```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """Calculate discount amount on price."""
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("Discount percent must be between 0 and 100")
    return price * (discount_percent / 100)
```

---

## is_palindrome

**Signature:** `def is_palindrome(text: str)`

**Summary:** Check if a string is a palindrome (reads the same forwards and backwards).

Args:
    text (str): The string to check
    
Returns:
    bool: True if the string is a palindrome, False otherwise
    
Examples:
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("hello")
    False
    >>> is_palindrome("A man a plan a canal Panama")
    True

```python
def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome (reads the same forwards and backwards).
    
    Args:
        text (str): The string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
        
    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    # Remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned == cleaned[::-1]
```

---

## `fibonacci`

### Brief Description

This function calculates the nth Fibonacci number using an iterative approach. The sequence is 0-indexed.

### Parameters

*   **`n`** (`int`): The position in the Fibonacci sequence for which to calculate the number. It is 0-indexed, meaning `fibonacci(0)` returns the first number, `fibonacci(1)` the second, and so on.

### Return Value

*   `int`: The nth Fibonacci number corresponding to the input position `n`.

### Usage Example

```python
>>> fibonacci(0)
0
>>> fibonacci(1)
1
>>> fibonacci(10)
55
```

### Edge Cases

*   **Negative Input (`n < 0`):** The function raises a `ValueError` with the message "Fibonacci number is not defined for negative numbers" because Fibonacci numbers are typically defined for non-negative integers.
*   **Zero Input (`n = 0`):** Returns `0`, which is the first number in the 0-indexed Fibonacci sequence.
*   **One Input (`n = 1`):** Returns `1`, which is the second number in the 0-indexed Fibonacci sequence.
---

## `factorial`

Calculates the factorial of a non-negative integer.

### Parameters

*   `n` (`int`): A non-negative integer for which the factorial is to be calculated.

### Return Value

*   `int`: The factorial of `n`.

### Raises

*   `ValueError`: If `n` is a negative integer. Factorial is not defined for negative numbers.

### Usage Examples

```python
>>> factorial(0)
1
>>> factorial(5)
120
>>> factorial(10)
3628800
```

### Edge Cases

*   **Negative Input (`n < 0`):**
    If a negative integer is provided as input, a `ValueError` is raised, as the factorial function is not defined for negative numbers.
*   **Zero Input (`n == 0`):**
    For an input of `0`, the function correctly returns `1`, which is the mathematical definition of `0!`.
---
