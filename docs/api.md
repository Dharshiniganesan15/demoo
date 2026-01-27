# API Documentation

## Function Reference

### Add Function
<!-- doc:ref=add -->
**Description**: Add multiple numbers together with enhanced logging and validation.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        *args: Additional numbers to add
        debug (bool): Enable debug output
        
    Returns:
        int/float: Sum of all numbers
        
    Raises:
        TypeError: If any argument is not a number
**Function**: `add(a, b, *args, debug=False)`
**Parameters**:
- `a` (int|float): Numeric value for add operation
- `b` (int|float): Numeric value for add operation
- `*args`: Additional variable arguments
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (int|float) The result of the mathematical operation
**Raises**: TypeError - If any argument is not a number
**Examples**:
```python
result = add(2, 3)  # Returns 5
result = add(1, 2, 3, 4)  # Returns 10
```

### Multiply Function
<!-- doc:ref=multiply -->
**Description**: Multiply multiple numbers together with logging and validation.
    
    Args:
        a (int/float): First number
        b (int/float): Second number
        *args: Additional numbers to multiply
        debug (bool): Enable debug output
        
    Returns:
        int/float: Product of all numbers
        
    Raises:
        TypeError: If any argument is not a number
**Function**: `multiply(a, b, *args, debug=False)`
**Parameters**:
- `a` (int|float): Numeric value for multiply operation
- `b` (int|float): Numeric value for multiply operation
- `*args`: Additional variable arguments
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (int|float) The result of the mathematical operation
**Raises**: TypeError - If any argument is not a number
**Examples**:
```python
result = multiply(2, 3)  # Returns 6
result = multiply(2, 3, 4)  # Returns 24
```

### Divide Function
<!-- doc:ref=divide -->
**Description**: Divide multiple numbers sequentially with logging and validation.
    
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
**Function**: `divide(a, b, *args, debug=False)`
**Parameters**:
- `a` (int|float): Numeric value for divide operation
- `b` (int|float): Numeric value for divide operation
- `*args`: Additional variable arguments
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (int|float) The result of division
**Raises**: TypeError - If any argument is not a number
**Raises**: ZeroDivisionError - If attempting to divide by zero
**Examples**:
```python
result = divide(10, 2)  # Returns 5.0
```

### Concat Function
<!-- doc:ref=concat -->
**Description**: Concatenate multiple values into a single string.
    
    Args:
        a: First value
        b: Second value
        *args: Additional values
        sep (str): Separator inserted between values
        debug (bool): Enable debug output
        
    Returns:
        str: Concatenated string
**Function**: `concat(a, b, *args, sep="", debug=False)`
**Parameters**:
- `a`: Function parameter
- `b`: Function parameter
- `*args`: Additional variable arguments
- `sep`: Function parameter
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (str) Processed string result
**Raises**: See implementation for specific error conditions
**Examples**:
```python
result = concat('a', 'b', 'c')  # Returns 'abc'
result = concat('a', 'b', sep='-')  # Returns 'a-b'
```

### Factorial Function
<!-- doc:ref=factorial -->
**Description**: Compute factorial of a non-negative integer.
    
    Args:
        n (int): Non-negative integer
        debug (bool): Enable debug output
        
    Returns:
        int: Factorial of n
        
    Raises:
        TypeError: If n is not an integer
        ValueError: If n is negative
**Function**: `factorial(n, debug=False)`
**Parameters**:
- `n` (int): Non-negative integer for factorial calculation
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (int) Factorial of the input number
**Raises**: TypeError - If input is not an integer
**Raises**: ValueError - If input is negative
**Examples**:
```python
result = factorial(5)  # Returns 120
```

### Power Function
<!-- doc:ref=power -->
**Description**: Calculate base^exp with logging.
**Function**: `power(base, exp, debug=False)`
**Parameters**:
- `base` (int|float): Base number for exponentiation
- `exp` (int|float): Exponent value
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (int|float) Result of base raised to the exponent
**Raises**: See implementation for specific error conditions
**Examples**:
```python
result = power(2, 3)  # Returns 8
```

### To_Uppercase Function
<!-- doc:ref=to_uppercase -->
**Description**: Convert text to uppercase with logging.
    
    Args:
        text (str): Input text to convert
        debug (bool): Enable debug output
        
    Returns:
        str: Uppercase version of the input text
        
    Raises:
        TypeError: If input is not a string
**Function**: `to_uppercase(text, debug=False)`
**Parameters**:
- `text`: Function parameter
- `debug` (bool): Enable debug output for detailed logging
**Returns**: Result of the function operation
**Raises**: See implementation for specific error conditions
**Examples**:
```python
result = to_uppercase('hello')  # Returns 'HELLO'
```

### Reverse_String Function
<!-- doc:ref=reverse_string -->
**Description**: Reverse a string with logging.
    
    Args:
        text (str): Input text to reverse
        debug (bool): Enable debug output
        
    Returns:
        str: Reversed version of the input text
        
    Raises:
        TypeError: If input is not a string
**Function**: `reverse_string(text, debug=False)`
**Parameters**:
- `text` (str): Input string to process
- `debug` (bool): Enable debug output for detailed logging
**Returns**: (str) Processed string result
**Raises**: TypeError - If input is not a string
**Examples**:
```python
result = reverse_string('hello')  # Returns 'olleh'
```

