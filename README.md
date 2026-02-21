# Project Documentation

This document provides a comprehensive overview of the Python codebase, detailing the functionality of each script and its respective functions. The documentation is generated directly and exclusively from the provided code, without external assumptions or inferred features.

## Table of Contents

*   [File: `main.py`](#file-mainpy)
    *   [`sum(a, b)`](#suma-b)
    *   [`sub(a, b)`](#suba-b)
    *   [`multiply(a, b)`](#multiplya-b)
    *   [`divide(a, b)`](#dividea-b)
*   [File: `math_utils.py`](#file-math_utilspy)
    *   [`multiply(a, b)`](#multiplya-b-1)
    *   [`divide(a, b)`](#dividea-b-1)
    *   [`power(base, exponent)`](#powerbase-exponent)
*   [File: `new_feature.py`](#file-new_featurepy)
    *   [`advanced_calculator()`](#advanced_calculator)
    *   [`test_calculator()`](#test_calculator)
*   [File: `start_server.py`](#file-start_serverpy)
    *   [`run_command(cmd, cwd=None)`](#run_commandcmd-cwdnone)
    *   [`main()`](#main)
*   [File: `test_feature.py`](#file-test_featurepy)
    *   [`calculate_fibonacci(n)`](#calculate_fibonaccin)
    *   [`test_fibonacci()`](#test_fibonacci)

---

## File: `main.py`

This file contains fundamental arithmetic operations.

### `sum(a, b)`

Adds two numbers together.

```python
def sum(a, b):
    # ...
```

**Parameters:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
The sum of `a` and `b`.

### `sub(a, b)`

Subtracts `b` from `a`.

```python
def sub(a, b):
    # ...
```

**Parameters:**
*   `a`: The number to subtract from.
*   `b`: The number to subtract.

**Returns:**
The result of `a - b`.

### `multiply(a, b)`

Multiplies two numbers together.

```python
def multiply(a, b):
    # ...
```

**Parameters:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
The product of `a` and `b`.

### `divide(a, b)`

Divides `a` by `b`, including a zero check.

```python
def divide(a, b):
    # ...
```

**Parameters:**
*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**
The result of `a / b`.

**Raises:**
*   `ValueError`: If `b` is `0`, indicating division by zero.

---

## File: `math_utils.py`

This module provides mathematical utilities for basic operations.

### `multiply(a, b)`

Multiplies two numbers together.

```python
def multiply(a, b):
    # ...
```

**Parameters:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
The product of `a` and `b`.

### `divide(a, b)`

Divides `a` by `b`. Includes a zero check.

```python
def divide(a, b):
    # ...
```

**Parameters:**
*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**
The result of `a / b`.

**Raises:**
*   `ValueError`: If `b` is `0`, indicating division by zero.

### `power(base, exponent)`

Calculates `base` raised to the power of `exponent`.

```python
def power(base, exponent):
    # ...
```

**Parameters:**
*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**
The result of `base ** exponent`.

---

## File: `new_feature.py`

This file defines an `advanced_calculator` function and a test suite for it.

### `advanced_calculator()`

An advanced calculator function that internally defines multiple operations.
When called, this function defines the following nested functions:

*   **`add(a, b)`**: Returns the sum of `a` and `b`.
*   **`subtract(a, b)`**: Returns the result of `a - b`.
*   **`multiply(a, b)`**: Returns the product of `a` and `b`.
*   **`divide(a, b)`**: Returns the result of `a / b`. If `b` is `0`, it returns the string `"Error: Division by zero"`.
*   **`modulo(a, b)`**: Returns the remainder of `a % b`. If `b` is `0`, it returns the string `"Error: Modulo by zero"`.
*   **`power(base, exponent)`**: Calculates `base` raised to the power of `exponent` using a loop.
*   **`factorial(n)`**: Calculates the factorial of `n`. If `n` is negative, it returns `"Error: Negative number"`. If `n` is `0`, it returns `1`.

**Note:** The nested functions (`add`, `subtract`, etc.) are defined within the scope of `advanced_calculator()` and are not directly accessible from outside this function as attributes of `advanced_calculator` itself based on the current code structure.

### `test_calculator()`

Tests the advanced calculator by attempting to call its operations and printing the results. It demonstrates expected output for various operations and indicates whether the actual result matches the expectation.

```python
def test_calculator():
    """Test the advanced calculator"""
    print("Testing Advanced Calculator:")
    
    # Test addition
    result = advanced_calculator.add(5, 3) # This call attempts to access nested function as attribute
    # ...
```

This function *attempts* to call the operations (e.g., `advanced_calculator.add(5, 3)`) as if they were attributes of the `advanced_calculator` function.
It performs tests for:
*   Addition (5 + 3)
*   Subtraction (10 - 4)
*   Multiplication (7 * 6)
*   Division (15 / 3)
*   Power (2^8)
*   Factorial (5!)

When `new_feature.py` is executed directly (`if __name__ == "__main__":`), the `test_calculator()` function is called.

---

## File: `start_server.py`

This script provides functionality to automatically stage, commit, and push Git changes, and then start a FastAPI server.

### `run_command(cmd, cwd=None)`

Executes a shell command and captures its output. It prints success messages with output or error messages if the command fails.

```python
def run_command(cmd, cwd=None):
    # ...
```

**Parameters:**
*   `cmd` (str): The command to execute.
*   `cwd` (str, optional): The current working directory for the command. Defaults to `None`.

**Returns:**
*   `True` if the command executed successfully.
*   `False` if the command failed or an exception occurred.

### `main()`

The main function orchestrates the Git operations and server startup.

```python
def main():
    # ...
```

**Functionality:**
1.  **Directory Setup:** Identifies the current script's directory (`demoo_dir`) and the project root.
2.  **Git Operations:**
    *   Changes the current directory to `demoo_dir`.
    *   **Adds all changes** to Git using `git add .`.
    *   **Commits changes** with an auto-generated message including the current timestamp (e.g., "Auto-update documentation - YYYY-MM-DD HH:MM:SS").
    *   **Pushes changes** to the remote Git repository using `git push`. This operation is intended to happen once.
3.  **Server Startup:**
    *   Changes the current directory back to the `project_root`.
    *   Imports `uvicorn`.
    *   Prints messages indicating the server's local URL (`http://localhost:8000`) and a webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Starts a `uvicorn` server to run `backend.app:app` with the following configuration:
        *   `host="0.0.0.0"`
        *   `port=8000`
        *   `reload=True`
        *   `log_level="info"`
    *   Handles `KeyboardInterrupt` to gracefully stop the server.

**Returns:**
*   `True` if all operations complete successfully.
*   `False` if any Git operation or server startup fails.

When `start_server.py` is executed directly (`if __name__ == "__main__":`), the `main()` function is called.

---

## File: `test_feature.py`

This file provides a function to calculate Fibonacci numbers and a test suite for it.

### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

```python
def calculate_fibonacci(n):
    # ...
```

**Parameters:**
*   `n` (int): The position in the Fibonacci sequence.

**Returns:**
*   `int`: The nth Fibonacci number.
    *   Returns `0` if `n <= 0`.
    *   Returns `1` if `n == 1` or `n == 2`.

**Logic:**
*   Initializes a DP table `fib` of size `n + 1`.
*   Sets base cases: `fib[0] = 0`, `fib[1] = 1`, `fib[2] = 1`.
*   Iteratively fills the `fib` table from `i = 3` to `n` using the recurrence `fib[i] = fib[i-1] + fib[i-2]`.

### `test_fibonacci()`

Tests the `calculate_fibonacci` function with a predefined set of test cases. It prints the expected versus actual results and indicates whether each test case passed or failed.

```python
def test_fibonacci():
    """Test the Fibonacci function"""
    # ...
```

**Test Cases:**
The function is tested for `n` values corresponding to the indices of the following `test_cases` list: `[0, 1, 2, 3, 5, 8, 13, 21, 34]`. This means it tests `fib(0)` up to `fib(8)`.

When `test_feature.py` is executed directly (`if __name__ == "__main__":`), the `test_fibonacci()` function is called.