This document provides an overview of the Python modules and functions within this project, generated directly from the provided source code.

---

# Project Documentation

This project consists of several Python modules covering basic mathematical operations, advanced calculation features, Fibonacci and factorial implementations, string utility for palindrome checking, and a script for server management including Git operations.

## Project Structure

*   [`demo_new_module.py`](#demo_new_modulepy)
*   [`main.py`](#mainpy)
*   [`math_utils.py`](#math_utilspy)
*   [`new_feature.py`](#new_featurepy)
*   [`start_server.py`](#start_serverpy)
*   [`test_feature.py`](#test_featurepy)

---

## File: `demo_new_module.py`

This module contains a simple greeting function and a demonstration of its usage.

### Functions

#### `greet(name: str) -> str`

Returns a greeting message for the given name.

**Arguments:**

*   `name` (str): The name to greet.

**Returns:**

*   `str`: A greeting string, e.g., "Hello, [name]!".

#### `run_demo() -> None`

Runs a demonstration by printing the greeting for "AI Doc System".

**Execution:**

When executed as the main script, `demo_new_module.py` calls `run_demo()`.

```python
if __name__ == "__main__":
    run_demo()
```

---

## File: `main.py`

This module provides a collection of utility functions for basic arithmetic, financial calculations, comparison, and common mathematical sequences like Fibonacci and Factorial, along with a string utility for palindrome checking.

### Functions

#### `sum(a, b)`

Adds two numbers together.

#### `sub(a, b)`

Subtracts `b` from `a`.

#### `multiply(a, b)`

Multiply two numbers together.

#### `divide(a, b)`

Divide `a` by `b` with zero check.

**Raises:**

*   `ValueError`: If `b` is 0 (cannot divide by zero).

#### `calculate_tax(income: float) -> float`

Calculate tax on income at a 10% rate.

**Arguments:**

*   `income` (float): The income amount.

**Returns:**

*   `float`: The calculated tax amount.

#### `calculate_discount(price: float, discount_percent: float) -> float`

Calculate discount amount on price.

**Arguments:**

*   `price` (float): The original price.
*   `discount_percent` (float): The discount percentage.

**Returns:**

*   `float`: The calculated discount amount.

**Raises:**

*   `ValueError`: If `discount_percent` is not between 0 and 100 (inclusive).

#### `average(a: float, b: float) -> float`

Return the average of two numbers.

**Arguments:**

*   `a` (float): The first number.
*   `b` (float): The second number.

**Returns:**

*   `float`: The average of `a` and `b`.

#### `max_of_two(a: float, b: float) -> float`

Return the larger of two numbers.

**Arguments:**

*   `a` (float): The first number.
*   `b` (float): The second number.

**Returns:**

*   `float`: The larger of `a` and `b`.

#### `is_palindrome(text: str) -> bool`

Check if a string is a palindrome (reads the same forwards and backwards).

**Arguments:**

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

Calculate the nth Fibonacci number using iteration.

**Arguments:**

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

Calculate the factorial of a non-negative integer.

**Arguments:**

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

---

## File: `math_utils.py`

Math utilities for basic operations.

### Functions

#### `multiply(a, b)`

Multiply two numbers together.

#### `divide(a, b)`

Divide two numbers.

**Raises:**

*   `ValueError`: If `b` is 0 (cannot divide by zero).

#### `power(base, exponent)`

Calculate base raised to the power of exponent.

---

## File: `new_feature.py`

This module defines an `advanced_calculator` function which encapsulates various arithmetic and mathematical operations, and includes a test function to demonstrate their usage.

### Functions

#### `advanced_calculator()`

Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, and division.

This function defines several local (nested) functions for specific operations:

*   ##### `add(a, b)`
    Returns the sum of `a` and `b`.

*   ##### `subtract(a, b)`
    Returns the difference of `a` and `b` (`a - b`).

*   ##### `multiply(a, b)`
    Returns the product of `a` and `b`.

*   ##### `divide(a, b)`
    Returns the quotient of `a` and `b`. If `b` is 0, it returns the string "Error: Division by zero".

*   ##### `modulo(a, b)`
    Returns the remainder of `a` divided by `b`. If `b` is 0, it returns the string "Error: Modulo by zero".

*   ##### `power(base, exponent)`
    Calculates `base` raised to the `exponent` using an iterative approach.

*   ##### `factorial(n)`
    Calculates the factorial of `n`. If `n` is negative, it returns the string "Error: Negative number". If `n` is 0, it returns 1.

#### `test_calculator()`

Tests the advanced calculator operations by attempting to call the nested functions (e.g., `advanced_calculator.add`) and printing the results along with a success/failure indicator.

**Execution:**

When executed as the main script, `new_feature.py` calls `test_calculator()`.

```python
if __name__ == "__main__":
    test_calculator()
```

---

## File: `start_server.py`

Start server with single automatic git push. This script automates Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

### Functions

#### `run_command(cmd, cwd=None)`

Runs a shell command and returns the result.

**Arguments:**

*   `cmd` (str): The command string to execute.
*   `cwd` (str, optional): The current working directory for the command. Defaults to `None`.

**Returns:**

*   `bool`: `True` if the command executes successfully (return code 0), `False` otherwise. Prints error messages to `stderr` on failure.

#### `main()`

Main function to start server with single git push.

This function performs the following steps:

1.  Determines the `demoo_dir` (directory of the current script) and `project_root`.
2.  Changes the current working directory to `demoo_dir`.
3.  **Git Operations:**
    *   Adds all changes to Git staging (`git add .`).
    *   Commits changes with an auto-generated timestamp message (`git commit -m "Auto-update documentation - YYYY-MM-DD HH:MM:SS"`).
    *   Pushes changes to the remote repository (`git push`). This step is intended to be executed "only once!".
4.  Changes the current working directory back to `project_root`.
5.  **Starts FastAPI Server:**
    *   Imports `uvicorn`.
    *   Prints server URLs (`http://localhost:8000` and `https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Starts the server using `uvicorn.run("backend.app:app", host="0.0.0.0", port=8000, reload=True, log_level="info")`.
    *   Handles `KeyboardInterrupt` to gracefully stop the server.

**Returns:**

*   `bool`: `True` on successful execution, `False` if any critical step (Git command or server start) fails.

**Execution:**

When executed as the main script, `start_server.py` calls `main()`.

```python
if __name__ == "__main__":
    main()
```

---

## File: `test_feature.py`

This module contains a function to calculate Fibonacci numbers using dynamic programming and a test function to verify its correctness.

### Functions

#### `calculate_fibonacci(n)`

Calculate the nth Fibonacci number using dynamic programming.

**Arguments:**

*   `n` (int): The position in the Fibonacci sequence.

**Returns:**

*   `int`: The nth Fibonacci number.

#### `test_fibonacci()`

Tests the Fibonacci function by iterating through a predefined list of expected values (Fibonacci numbers for indices 0 to 8) and printing the results, indicating whether each test case passed or failed.

**Execution:**

When executed as the main script, `test_feature.py` calls `test_fibonacci()`.

```python
if __name__ == "__main__":
    test_fibonacci()
```