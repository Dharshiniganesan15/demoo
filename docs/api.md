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
- `a` (int|float): Primary numeric operand for the add operation
- `b` (int|float): Primary numeric operand for the add operation
- `*args`: Additional variable arguments for extended functionality
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (int|float) The computed result of the mathematical operation with precision preservation
**Raises**: TypeError - When any argument is not a numeric type (int or float)
**Examples**:
```python
# Basic addition
result = add(5, 3)  # Returns 8
# Multiple numbers
result = add(1, 2, 3, 4, 5)  # Returns 15
# With debug
result = add(10, 20, debug=True)  # Shows calculation steps
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


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
- `a` (int|float): Primary numeric operand for the multiply operation
- `b` (int|float): Primary numeric operand for the multiply operation
- `*args`: Additional variable arguments for extended functionality
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (int|float) The computed result of the mathematical operation with precision preservation
**Raises**: TypeError - When any argument is not a numeric type (int or float)
**Examples**:
```python
# Basic multiplication
result = multiply(4, 5)  # Returns 20
# Multiple factors
result = multiply(2, 3, 4)  # Returns 24
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


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
- `a` (int|float): Primary numeric operand for the divide operation
- `b` (int|float): Primary numeric operand for the divide operation
- `*args`: Additional variable arguments for extended functionality
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (int|float) The result of sequential division with floating-point precision
**Raises**: TypeError - When any argument is not a numeric type (int or float)
**Raises**: ZeroDivisionError - When attempting division by zero
**Examples**:
```python
# Basic division
result = divide(10, 2)  # Returns 5.0
# Sequential division
result = divide(100, 5, 2)  # Returns 10.0
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


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
- `a`: Function parameter with type-specific validation
- `b`: Function parameter with type-specific validation
- `*args`: Additional variable arguments for extended functionality
- `sep`: Function parameter with type-specific validation
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (str) The concatenated string with optional separator between elements
**Raises**: Type-specific exceptions based on input validation requirements
**Examples**:
```python
# Basic concatenation
result = concat('a', 'b', 'c')  # Returns 'abc'
# With separator
result = concat('a', 'b', 'c', sep='-')  # Returns 'a-b-c'
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


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
- `n` (int): Non-negative integer for factorial calculation (0 ≤ n ≤ ∞)
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (int) The factorial value representing the product of all positive integers up to n
**Raises**: TypeError - When input is not an integer
**Raises**: ValueError - When input is negative (factorial undefined for negative numbers)
**Examples**:
```python
# Basic factorial
result = factorial(5)  # Returns 120
# Zero factorial
result = factorial(0)  # Returns 1
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


### Power Function
<!-- doc:ref=power -->
**Description**: Calculate base^exp with logging.
**Function**: `power(base, exp, debug=False)`
**Parameters**:
- `base` (int|float): Base number to be raised to the specified power
- `exp` (int|float): Exponent value determining the power to raise the base
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (int|float) The result of base raised to the power of exp (base^exp)
**Raises**: Type-specific exceptions based on input validation requirements
**Examples**:
```python
# Basic power
result = power(2, 3)  # Returns 8
# Fractional exponent
result = power(9, 0.5)  # Returns 3.0
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


### To Uppercase Function
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
- `text`: Function parameter with type-specific validation
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (str) The uppercase version of the input string with Unicode character preservation
**Raises**: TypeError - When input is not a string type
**Examples**:
```python
# Basic conversion
result = to_uppercase('hello')  # Returns 'HELLO'
# Mixed case
result = to_uppercase('Hello World')  # Returns 'HELLO WORLD'
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


### Reverse String Function
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
- `text` (str): Input string to be processed and transformed
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (str) The input string reversed character by character using efficient slicing
**Raises**: TypeError - When input is not a string type
**Examples**:
```python
# Basic reversal
result = reverse_string('hello')  # Returns 'olleh'
# Palindrome check
result = reverse_string('racecar')  # Returns 'racecar'
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


### Calculate Average Function
<!-- doc:ref=calculate_average -->
**Description**: Calculate the average (mean) of a list of numbers.
    
    Args:
        numbers (list): List of numbers to calculate average
        debug (bool): Enable debug output
        
    Returns:
        float: Average of the numbers
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
**Function**: `calculate_average(numbers, debug=False)`
**Parameters**:
- `numbers` (list): Sequence of numeric values to process (must contain at least one element)
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (float) The arithmetic mean of all numbers in the input list
**Raises**: TypeError - When input is not a list or contains non-numeric elements
**Raises**: ValueError - When input list is empty
**Examples**:
```python
# Basic average
result = calculate_average([1, 2, 3, 4, 5])  # Returns 3.0
# With decimals
result = calculate_average([1.5, 2.5, 3.5])  # Returns 2.5
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


### Find Max Function
<!-- doc:ref=find_max -->
**Description**: Find the maximum value in a list of numbers.
    
    Args:
        numbers (list): List of numbers to find maximum
        debug (bool): Enable debug output
        
    Returns:
        int/float: Maximum value in the list
        
    Raises:
        TypeError: If input is not a list or contains non-numeric values
        ValueError: If list is empty
**Function**: `find_max(numbers, debug=False)`
**Parameters**:
- `numbers` (list): Sequence of numeric values to process (must contain at least one element)
- `debug` (bool): Enables detailed debug logging to trace function execution and intermediate values
**Returns**: (int|float) The maximum value found in the input list
**Raises**: TypeError - When input is not a list or contains non-numeric elements
**Raises**: ValueError - When input list is empty
**Examples**:
```python
# Basic maximum
result = find_max([1, 5, 3, 9, 2])  # Returns 9
# With negatives
result = find_max([-5, -2, -8])  # Returns -2
```
**Notes**:
- This function includes comprehensive input validation
- Debug mode provides detailed execution tracing
- Performance optimized for typical use cases
- Follows Python best practices and type hints


