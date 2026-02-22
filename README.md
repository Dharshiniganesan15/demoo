This document provides comprehensive documentation for the Python codebase, derived directly and solely from the provided source files.

---

# Project Documentation

This project comprises several Python modules demonstrating various functionalities, including basic arithmetic operations, string manipulations, sequence calculations, an advanced calculator concept, and a server management script that integrates with Git and attempts to start a Uvicorn server.

## File: `demo_new_module.py`

This module contains a simple demonstration of a greeting function and a runner.

### Functions

#### `greet(name: str) -> str`

Returns a personalized greeting string.

**Parameters:**
*   `name` (`str`): The name to greet.

**Returns:**
*   `str`: A greeting string, e.g., "Hello, [name]!".

#### `run_demo() -> None`

Executes the `greet` function with a predefined name and prints the result.

**Execution:**
When this script is run directly, the `run_demo()` function is called.

```python
if __name__ == "__main__":
    run_demo()
```

## File: `main.py`

This module provides a collection of general-purpose utility functions covering basic arithmetic, financial calculations, comparison, string manipulation, and recursive sequence calculations.

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
*   `a`: The number to subtract from.
*   `b`: The number to subtract.

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
*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**
*   The result of `a / b`.

**Raises:**
*   `ValueError`: If `b` is zero.

#### `calculate_tax(income: float) -> float`

Calculates tax on income at a 10% rate.

**Parameters:**
*   `income` (`float`): The income amount.

**Returns:**
*   `float`: The calculated tax amount (10% of income).

#### `calculate_discount(price: float, discount_percent: float) -> float`

Calculates the discount amount on a given price.

**Parameters:**
*   `price` (`float`): The original price.
*   `discount_percent` (`float`): The discount percentage.

**Returns:**
*   `float`: The calculated discount amount.

**Raises:**
*   `ValueError`: If `discount_percent` is not between 0 and 100.

#### `average(a: float, b: float) -> float`

Returns the average of two numbers.

**Parameters:**
*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**
*   `float`: The average of `a` and `b`.

#### `max_of_two(a: float, b: float) -> float`

Returns the larger of two numbers.

**Parameters:**
*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**
*   `float`: The larger of `a` or `b`.

#### `is_palindrome(text: str) -> bool`

Checks if a string is a palindrome (reads the same forwards and backwards).
Non-alphanumeric characters are removed, and the string is converted to lowercase for the check.

**Parameters:**
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

#### `fibonacci(n: int) -> int`

Calculates the nth Fibonacci number using iteration. The sequence is 0-indexed (F0 = 0, F1 = 1).

**Parameters:**
*   `n` (`int`): The position in the Fibonacci sequence.

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
*   `n` (`int`): A non-negative integer.

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

## File: `math_utils.py`

This module provides utility functions for basic mathematical operations.

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
*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**
*   The result of `a / b`.

**Raises:**
*   `ValueError`: If `b` is zero.

#### `power(base, exponent)`

Calculates `base` raised to the power of `exponent`.

**Parameters:**
*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**
*   The result of `base ** exponent`.

## File: `new_feature.py`

This module defines an `advanced_calculator` function which internally defines several arithmetic and mathematical operations. It also includes a `test_calculator` function that attempts to test these operations.

### Functions

#### `advanced_calculator()`

An advanced calculator function with multiple operations.
This function locally defines nested functions for addition, subtraction, multiplication, division, modulo, power, and factorial. These nested functions are only accessible within the scope of `advanced_calculator` itself and are not directly exposed or returned by `advanced_calculator`.

**Nested Functions (locally defined within `advanced_calculator`):**

*   `add(a, b)`: Returns the sum of `a` and `b`.
*   `subtract(a, b)`: Returns the result of `a - b`.
*   `multiply(a, b)`: Returns the product of `a` and `b`.
*   `divide(a, b)`: Returns the result of `a / b`. Returns "Error: Division by zero" if `b` is 0.
*   `modulo(a, b)`: Returns the result of `a % b`. Returns "Error: Modulo by zero" if `b` is 0.
*   `power(base, exponent)`: Calculates `base` raised to the `exponent` using a loop.
*   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative. Returns 1 if `n` is 0.

#### `test_calculator()`

Attempts to test the operations defined within `advanced_calculator`. The test tries to access the nested functions using `advanced_calculator.add`, `advanced_calculator.subtract`, etc. and prints the results with pass/fail indicators.

**Execution:**
When this script is run directly, the `test_calculator()` function is called.

```python
if __name__ == "__main__":
    test_calculator()
```

## File: `start_server.py`

This script is designed to automate a sequence of Git operations (add, commit, push) and then start a FastAPI server using Uvicorn.

### Functions

#### `run_command(cmd, cwd=None)`

Runs a shell command and captures its output. It prints success/error messages and the command's standard output if successful.

**Parameters:**
*   `cmd` (`str`): The command string to execute.
*   `cwd` (`str`, optional): The working directory for the command. Defaults to `None` (current directory).

**Returns:**
*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

#### `main()`

The main function orchestrates the Git operations and server startup.

1.  **Directory Navigation:** Determines the project root and the script's directory.
2.  **Git Operations:**
    *   Changes to the script's directory (`demoo_dir`).
    *   Executes `git add .` to stage all changes.
    *   Executes `git commit -m "Auto-update documentation - [timestamp]"` with a timestamped commit message.
    *   Executes `git push` to push committed changes to the remote repository.
3.  **Server Startup:**
    *   Changes to the `project_root` directory.
    *   Attempts to import `uvicorn`.
    *   Starts a Uvicorn server, configured to run `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Prints expected server URL and a webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Handles `KeyboardInterrupt` for graceful shutdown and other exceptions during server startup.

**Execution:**
When this script is run directly, the `main()` function is called.

```python
if __name__ == "__main__":
    main()
```

## File: `test_feature.py`

This module provides an implementation for calculating Fibonacci numbers using dynamic programming and includes a dedicated test function for it.

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.
The function initializes a DP table and fills it iteratively.

**Parameters:**
*   `n` (`int`): The position in the Fibonacci sequence.

**Returns:**
*   `int`: The nth Fibonacci number. Returns 0 for `n <= 0`, 1 for `n = 1`, and 1 for `n = 2` as base cases before DP table computation.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases.
It prints the input `n`, the calculated result, the expected result, and a pass/fail status for each test case.

**Execution:**
When this script is run directly, the `test_fibonacci()` function is called.

```python
if __name__ == "__main__":
    test_fibonacci()
```