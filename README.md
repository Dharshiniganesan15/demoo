This document provides comprehensive documentation for the provided Python code, adhering strictly to the given rules.

---

# Project Documentation

This project consists of several Python modules demonstrating various functionalities, including basic arithmetic operations, string manipulation, sequence generation, advanced calculator features, utility functions for system commands, and a server startup script.

## File: `demo_new_module.py`

This module provides a simple greeting function and a demo runner.

### `greet(name: str) -> str`

Returns a personalized greeting string.

**Arguments:**
*   `name` (`str`): The name to greet.

**Returns:**
*   `str`: A greeting message, e.g., "Hello, [name]!".

### `run_demo() -> None`

Executes a demonstration of the `greet` function by printing a greeting to "AI Doc System".

**Arguments:**
*   None

**Returns:**
*   `None`

### Execution (`if __name__ == "__main__":`)

When the script is run directly, the `run_demo()` function is called.

## File: `main.py`

This module contains a collection of fundamental utility functions, primarily focused on mathematical operations and string processing.

### `sum(a, b)`

Adds two numbers together.

**Arguments:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
*   The sum of `a` and `b`.

### `sub(a, b)`

Subtracts `b` from `a`.

**Arguments:**
*   `a`: The number to subtract from.
*   `b`: The number to subtract.

**Returns:**
*   The difference of `a` and `b`.

### `multiply(a, b)`

Multiplies two numbers together.

**Arguments:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
*   The product of `a` and `b`.

### `divide(a, b)`

Divides `a` by `b` with a zero division check.

**Arguments:**
*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**
*   The result of `a` divided by `b`.

**Raises:**
*   `ValueError`: If `b` is `0`, indicating division by zero.

### `calculate_tax(income: float) -> float`

Calculates tax on a given income at a fixed rate of 10%.

**Arguments:**
*   `income` (`float`): The income amount.

**Returns:**
*   `float`: The calculated tax amount (10% of income).

### `calculate_discount(price: float, discount_percent: float) -> float`

Calculates the discount amount based on a price and a discount percentage.

**Arguments:**
*   `price` (`float`): The original price.
*   `discount_percent` (`float`): The discount percentage, expected to be between 0 and 100.

**Returns:**
*   `float`: The calculated discount amount.

**Raises:**
*   `ValueError`: If `discount_percent` is less than 0 or greater than 100.

### `average(a: float, b: float) -> float`

Returns the average of two numbers.

**Arguments:**
*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**
*   `float`: The average of `a` and `b`.

### `max_of_two(a: float, b: float) -> float`

Returns the larger of two numbers.

**Arguments:**
*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**
*   `float`: The larger of `a` and `b`.

### `is_palindrome(text: str) -> bool`

Checks if a string is a palindrome (reads the same forwards and backwards), ignoring non-alphanumeric characters and case.

**Arguments:**
*   `text` (`str`): The string to check.

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

### `fibonacci(n: int) -> int`

Calculates the nth Fibonacci number using an iterative approach. The sequence is 0-indexed (e.g., `fibonacci(0)` is 0, `fibonacci(1)` is 1).

**Arguments:**
*   `n` (`int`): The position in the Fibonacci sequence.

**Returns:**
*   `int`: The nth Fibonacci number.

**Raises:**
*   `ValueError`: If `n` is negative, as Fibonacci numbers are not defined for negative indices in this implementation.

**Examples:**
```python
>>> fibonacci(0)
0
>>> fibonacci(1)
1
>>> fibonacci(10)
55
```

## File: `math_utils.py`

This module provides basic mathematical utility functions.

### `multiply(a, b)`

Multiply two numbers together.

**Arguments:**
*   `a`: The first number.
*   `b`: The second number.

**Returns:**
*   The product of `a` and `b`.

### `divide(a, b)`

Divide two numbers.

**Arguments:**
*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**
*   The result of `a` divided by `b`.

**Raises:**
*   `ValueError`: If `b` is `0`, indicating division by zero.

### `power(base, exponent)`

Calculate base raised to the power of exponent.

**Arguments:**
*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**
*   The `base` raised to the `exponent` power.

## File: `new_feature.py`

This module defines an `advanced_calculator` function which encapsulates several arithmetic and mathematical operations as nested functions, along with a testing utility.

### `advanced_calculator()`

This function defines a set of operations including addition, subtraction, multiplication, division, modulo, power, and factorial. These operations are implemented as nested functions within `advanced_calculator()`.

**Nested Functions (accessible only within `advanced_calculator`'s scope):**

*   **`add(a, b)`**: Returns the sum of `a` and `b`.
*   **`subtract(a, b)`**: Returns the difference of `a` and `b`.
*   **`multiply(a, b)`**: Returns the product of `a` and `b`.
*   **`divide(a, b)`**: Returns the result of `a` divided by `b`. If `b` is `0`, returns the string `"Error: Division by zero"`.
*   **`modulo(a, b)`**: Returns the remainder of `a` divided by `b`. If `b` is `0`, returns the string `"Error: Modulo by zero"`.
*   **`power(base, exponent)`**: Calculates `base` raised to the `exponent` using a loop.
*   **`factorial(n)`**: Calculates the factorial of `n`. Returns `1` if `n` is `0`. If `n` is negative, returns the string `"Error: Negative number"`.

### `test_calculator()`

Tests the functionality of the advanced calculator's operations by attempting to call the nested functions via `advanced_calculator.<function_name>`. It prints the results of various test cases, indicating success (`✅ PASS`) or failure (`❌ FAIL`).

**Arguments:**
*   None

**Returns:**
*   `None`

### Execution (`if __name__ == "__main__":`)

When the script is run directly, the `test_calculator()` function is called to perform tests and print their outcomes.

## File: `start_server.py`

This script automates a sequence of Git operations (add, commit, push) and then starts a FastAPI web server using `uvicorn`.

### Shebang

`#!/usr/bin/env python3` specifies the interpreter for execution.

### Module Docstring

"Start server with single automatic git push"

### `run_command(cmd, cwd=None)`

Executes a shell command and captures its output and return code. It prints status messages indicating success or error.

**Arguments:**
*   `cmd` (`str`): The shell command to execute.
*   `cwd` (`str`, optional): The directory in which to execute the command. Defaults to the current working directory.

**Returns:**
*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise or if an exception occurred.

### `main()`

This function orchestrates the Git operations and server startup.

1.  **Directory Setup**: Determines the script's own directory (`demoo_dir`) and the presumed project root.
2.  **Git Operations**:
    *   Changes directory to `demoo_dir`.
    *   Adds all changes (`git add .`).
    *   Commits changes with an auto-generated timestamp message (`git commit -m "Auto-update documentation - <timestamp>"`). Prints a message if no changes were committed.
    *   Pushes changes to the remote repository (`git push`).
3.  **Server Startup**:
    *   Changes directory to `project_root`.
    *   Attempts to start a FastAPI server by importing `uvicorn` and running it.
    *   The server is configured to run `backend.app:app` on `0.0.0.0:8000`, with `reload=True` and `log_level="info"`.
    *   Prints expected server URL (`http://localhost:8000`) and a static ngrok webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Handles `KeyboardInterrupt` to gracefully stop the server and general exceptions during server startup.

**Arguments:**
*   None

**Returns:**
*   `bool`: `True` if all operations (Git and server start) complete successfully, `False` if any step fails.

### Execution (`if __name__ == "__main__":`)

When the script is run directly, the `main()` function is called to initiate the Git push and server startup process.

## File: `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a test suite for it.

### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

**Arguments:**
*   `n` (`int`): The position in the Fibonacci sequence (0-indexed).

**Returns:**
*   `int`: The nth Fibonacci number. Returns `0` for `n <= 0`, `1` for `n == 1` or `n == 2`.

### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of Fibonacci numbers. It prints the input, calculated result, expected result, and a status (`✅ PASS` or `❌ FAIL`) for each test case.

**Arguments:**
*   None

**Returns:**
*   `None`

### Execution (`if __name__ == "__main__":`)

When the script is run directly, the `test_fibonacci()` function is called to execute the tests and print their results.