This document provides comprehensive documentation for the provided Python codebase, adhering strictly to the code's content without introducing external assumptions or inventing features.

---

# Project Documentation

This project consists of several Python modules demonstrating various functionalities, including basic arithmetic operations, string manipulations, advanced mathematical algorithms, utility functions for server management, and an attempt at an advanced calculator feature.

## Module: `demo_new_module.py`

This module provides a simple demonstration of a greeting function.

### Functions

#### `greet(name: str) -> str`
Returns a personalized greeting message.

**Parameters:**
*   `name` (str): The name to be included in the greeting.

**Returns:**
*   `str`: A string containing "Hello, {name}!".

#### `run_demo() -> None`
Executes a demonstration of the `greet` function by printing a greeting to "AI Doc System".

## Module: `main.py`

This module contains a collection of general-purpose utility functions covering basic arithmetic, financial calculations, string processing, and common mathematical sequences.

### Functions

#### `sum(a, b)`
Adds two numbers together.

**Parameters:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
*   The sum of `a` and `b`.

#### `sub(a, b)`
Subtracts `b` from `a`.

**Parameters:**
*   `a`: The minuend.
*   `b`: The subtrahend.

**Returns:**
*   The result of `a - b`.

#### `multiply(a, b)`
Multiplies two numbers together.

**Parameters:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
*   The product of `a` and `b`.

#### `divide(a, b)`
Divides `a` by `b` with a zero check.

**Parameters:**
*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**
*   The result of `a / b`.

**Raises:**
*   `ValueError`: If `b` is zero, indicating division by zero.

#### `calculate_tax(income: float) -> float`
Calculates tax on income at a 10% rate.

**Parameters:**
*   `income` (float): The income amount.

**Returns:**
*   `float`: The calculated tax amount (10% of income).

#### `calculate_discount(price: float, discount_percent: float) -> float`
Calculates the discount amount on a given price.

**Parameters:**
*   `price` (float): The original price.
*   `discount_percent` (float): The discount percentage, expected to be between 0 and 100.

**Returns:**
*   `float`: The calculated discount amount.

**Raises:**
*   `ValueError`: If `discount_percent` is outside the range of 0 to 100.

#### `average(a: float, b: float) -> float`
Returns the average of two numbers.

**Parameters:**
*   `a` (float): The first number.
*   `b` (float): The second number.

**Returns:**
*   `float`: The average of `a` and `b`.

#### `max_of_two(a: float, b: float) -> float`
Returns the larger of two numbers.

**Parameters:**
*   `a` (float): The first number.
*   `b` (float): The second number.

**Returns:**
*   `float`: The larger of `a` and `b`.

#### `is_palindrome(text: str) -> bool`
Checks if a string is a palindrome (reads the same forwards and backwards), ignoring non-alphanumeric characters and case.

**Parameters:**
*   `text` (str): The string to check.

**Returns:**
*   `bool`: `True` if the string is a palindrome, `False` otherwise.

**Examples:**
```python
>>> is_palindrome("racecar")
True
>>> is_palindrome("hello")
False
>>> is_palindrome("A man a plan a canal Panama")
True
```

#### `fibonacci(n: int) -> int`
Calculates the nth Fibonacci number using iteration.

**Parameters:**
*   `n` (int): The position in the Fibonacci sequence (0-indexed).

**Returns:**
*   `int`: The nth Fibonacci number.

**Raises:**
*   `ValueError`: If `n` is negative.

**Examples:**
```python
>>> fibonacci(0)
0
>>> fibonacci(1)
1
>>> fibonacci(10)
55
```

#### `factorial(n: int) -> int`
Calculates the factorial of a non-negative integer.

**Parameters:**
*   `n` (int): A non-negative integer.

**Returns:**
*   `int`: The factorial of `n`.

**Raises:**
*   `ValueError`: If `n` is negative.

**Examples:**
```python
>>> factorial(0)
1
>>> factorial(5)
120
>>> factorial(10)
3628800
```

## Module: `math_utils.py`

This module provides basic mathematical utility functions.

### Functions

#### `multiply(a, b)`
Multiplies two numbers together.

**Parameters:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
*   The product of `a` and `b`.

#### `divide(a, b)`
Divides two numbers.

**Parameters:**
*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**
*   The result of `a / b`.

**Raises:**
*   `ValueError`: If `b` is zero, indicating division by zero.

#### `power(base, exponent)`
Calculates `base` raised to the power of `exponent`.

**Parameters:**
*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**
*   The result of `base ** exponent`.

## Module: `new_feature.py`

This module defines an `advanced_calculator` function which internally defines several arithmetic operations. It also includes a `test_calculator` function that attempts to demonstrate the usage of these operations.

**Important Note:** The arithmetic functions (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, `factorial`) are defined *inside* the `advanced_calculator` function. As currently implemented, these nested functions are not directly accessible from outside `advanced_calculator`. The `test_calculator` function attempts to call them as `advanced_calculator.add`, etc., which will result in an `AttributeError` at runtime, as `advanced_calculator` is a function, not an object with such attributes.

### Functions

#### `advanced_calculator()`
This function aims to provide an advanced calculator. It internally defines the following operations:

*   `add(a, b)`: Returns the sum of `a` and `b`.
*   `subtract(a, b)`: Returns the result of `a - b`.
*   `multiply(a, b)`: Returns the product of `a` and `b`.
*   `divide(a, b)`: Returns the result of `a / b`. Returns "Error: Division by zero" if `b` is 0.
*   `modulo(a, b)`: Returns the remainder of `a / b`. Returns "Error: Modulo by zero" if `b` is 0.
*   `power(base, exponent)`: Calculates `base` raised to the `exponent` using a loop.
*   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative. Returns 1 if `n` is 0.

#### `test_calculator()`
This function attempts to test the operations defined within `advanced_calculator`. It prints the results of various arithmetic, power, and factorial calculations, indicating whether each test "✅ PASS" or "❌ FAIL" based on expected values.

**Current Behavior:** As noted above, this function will fail to execute successfully due to an `AttributeError` when attempting to access the nested functions (`add`, `subtract`, etc.) via `advanced_calculator.<function_name>`.

## Module: `start_server.py`

This module is a utility script designed to automate Git operations (add, commit, push) and then start a FastAPI server using `uvicorn`.

### Dependencies

*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib.Path`
*   `uvicorn` (imported dynamically within `main` function)

### Functions

#### `run_command(cmd, cwd=None)`
Executes a shell command and captures its output.

**Parameters:**
*   `cmd` (str): The shell command to run.
*   `cwd` (str, optional): The current working directory for the command. Defaults to `None`.

**Returns:**
*   `bool`: `True` if the command executes successfully (return code 0), `False` otherwise. Prints error messages to `stderr` and success messages/output to `stdout`.

#### `main()`
The main function orchestrates the Git operations and server startup.

**Workflow:**
1.  Determines the project root and the script's directory.
2.  Changes the current directory to the script's parent directory (`demoo_dir`) for Git operations.
3.  **Git Operations:**
    *   Adds all changes (`git add .`).
    *   Commits changes with an auto-generated timestamped message (`git commit -m "Auto-update documentation - YYYY-MM-DD HH:MM:SS"`).
    *   Pushes changes to the remote repository (`git push`).
4.  Changes the current directory back to the `project_root`.
5.  **Server Startup:**
    *   Imports `uvicorn`.
    *   Starts a `uvicorn` server for `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Prints a webhook URL `https://da3b21fd5fff.ngrok-free.app/webhook/git`.
    *   Handles `KeyboardInterrupt` to gracefully stop the server.

**Returns:**
*   `bool`: `True` if all operations complete without unhandled exceptions, `False` otherwise.

## Module: `test_feature.py`

This module implements a function to calculate Fibonacci numbers using dynamic programming and includes a test suite for it.

### Functions

#### `calculate_fibonacci(n)`
Calculates the nth Fibonacci number using dynamic programming.

**Parameters:**
*   `n` (int): The position in the Fibonacci sequence.

**Returns:**
*   `int`: The nth Fibonacci number. Returns 0 for `n <= 0`, 1 for `n == 1` or `n == 2`.

#### `test_fibonacci()`
Tests the `calculate_fibonacci` function with a series of predefined test cases. It prints the input `n`, the calculated result, the expected result, and a status (`✅ PASS` or `❌ FAIL`) for each test case.