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
