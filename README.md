This documentation provides an overview of the Python codebase, detailing the functionality found in each script and its respective functions. The information is derived directly and exclusively from the provided source code, without external assumptions or interpretations.

---

# Project Documentation

This project comprises several Python scripts demonstrating various functionalities, including basic mathematical operations, advanced calculation features, string manipulation, sequence generation, and a utility for managing Git operations and starting a FastAPI server.

## Files

The project is structured into the following Python files:

*   [`demo_new_module.py`](#file-demonewmodulepy)
*   [`main.py`](#file-mainpy)
*   [`math_utils.py`](#file-mathutilspy)
*   [`new_feature.py`](#file-newfeaturepy)
*   [`start_server.py`](#file-startserverpy)
*   [`test_feature.py`](#file-testfeaturepy)

---

## File: `demo_new_module.py`

This file contains a simple greeting function and a demonstration of its usage.

### Functions

#### `greet(name: str) -> str`

Returns a greeting string.

**Arguments:**

*   `name` (`str`): The name to greet.

**Returns:**

*   `str`: A greeting message, e.g., "Hello, [name]!".

#### `run_demo() -> None`

Executes a demonstration by calling `greet` with "AI Doc System" and printing the result.

### Usage Example

When executed as the main script, `demo_new_module.py` will run the `run_demo` function.

```python
if __name__ == "__main__":
    run_demo()
```

---

## File: `main.py`

This file provides a collection of utility functions for basic arithmetic, financial calculations, comparison, string manipulation, and sequence generation.

### Functions

#### `sum(a, b)`

Add two numbers together.

**Arguments:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The sum of `a` and `b`.

#### `sub(a, b)`

Subtract `b` from `a`.

**Arguments:**

*   `a`: The minuend.
*   `b`: The subtrahend.

**Returns:**

*   The result of `a - b`.

#### `multiply(a, b)`

Multiply two numbers together.

**Arguments:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

#### `divide(a, b)`

Divide `a` by `b` with zero check.

**Arguments:**

*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**

*   The result of `a / b`.

**Raises:**

*   `ValueError`: If `b` is zero.

#### `calculate_tax(income: float) -> float`

Calculate tax on income at a 10% rate.

**Arguments:**

*   `income` (`float`): The income amount.

**Returns:**

*   `float`: The calculated tax amount (10% of income).

#### `calculate_discount(price: float, discount_percent: float) -> float`

Calculate discount amount on price.

**Arguments:**

*   `price` (`float`): The original price.
*   `discount_percent` (`float`): The discount percentage (between 0 and 100).

**Returns:**

*   `float`: The calculated discount amount.

**Raises:**

*   `ValueError`: If `discount_percent` is not between 0 and 100.

#### `average(a: float, b: float) -> float`

Return the average of two numbers.

**Arguments:**

*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**

*   `float`: The average of `a` and `b`.

#### `max_of_two(a: float, b: float) -> float`

Return the larger of two numbers.

**Arguments:**

*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**

*   `float`: The larger of `a` and `b`.

#### `is_palindrome(text: str) -> bool`

Check if a string is a palindrome (reads the same forwards and backwards).

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

#### `fibonacci(n: int) -> int`

Calculate the nth Fibonacci number using iteration.

**Arguments:**

*   `n` (`int`): The position in the Fibonacci sequence (0-indexed).

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

---

## File: `math_utils.py`

This module provides utility functions for basic mathematical operations.

### Functions

#### `multiply(a, b)`

Multiply two numbers together.

**Arguments:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

#### `divide(a, b)`

Divide two numbers.

**Arguments:**

*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**

*   The result of `a / b`.

**Raises:**

*   `ValueError`: If `b` is zero.

#### `power(base, exponent)`

Calculate base raised to the power of exponent.

**Arguments:**

*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**

*   The result of `base ** exponent`.

---

## File: `new_feature.py`

This file defines an `advanced_calculator` function which encapsulates several mathematical operations as nested functions, and a `test_calculator` function to demonstrate their usage.

### Functions

#### `advanced_calculator()`

Advanced calculator with multiple operations.
Supports addition, subtraction, multiplication, and division.

This function defines the following nested operations:

*   **`add(a, b)`**: Returns `a + b`.
*   **`subtract(a, b)`**: Returns `a - b`.
*   **`multiply(a, b)`**: Returns `a * b`.
*   **`divide(a, b)`**: Returns `a / b`, or "Error: Division by zero" if `b` is 0.
*   **`modulo(a, b)`**: Returns `a % b`, or "Error: Modulo by zero" if `b` is 0.
*   **`power(base, exponent)`**: Calculates `base` raised to `exponent` using iteration.
*   **`factorial(n)`**: Calculates the factorial of `n`. Returns 1 if `n` is 0. Returns "Error: Negative number" if `n` is negative.

#### `test_calculator()`

Test the advanced calculator. This function attempts to call the nested operations defined within `advanced_calculator` as if they were attributes of `advanced_calculator` and prints test results for addition, subtraction, multiplication, division, power, and factorial.

### Usage Example

When executed as the main script, `new_feature.py` will run the `test_calculator` function.

```python
if __name__ == "__main__":
    test_calculator()
```

---

## File: `start_server.py`

This script is designed to automate Git operations (add, commit, push) and then start a FastAPI server using `uvicorn`.

### Functions

#### `run_command(cmd, cwd=None)`

Run a command and return the result.

**Arguments:**

*   `cmd` (`str`): The command string to execute in the shell.
*   `cwd` (`str`, `optional`): The current working directory for the command. Defaults to `None` (current directory).

**Returns:**

*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise. Prints error messages to `stderr` and command output to `stdout`.

#### `main()`

Main function to start server with single git push.

This function performs the following sequence of operations:
1.  Determines the project root and current `demoo` directory.
2.  Changes the current working directory to `demoo_dir`.
3.  Adds all changes to Git using `git add .`.
4.  Commits changes to Git with an auto-generated timestamped commit message.
5.  Pushes committed changes to the remote Git repository using `git push`.
6.  Changes the current working directory back to `project_root`.
7.  Starts a `uvicorn` server for the `backend.app:app` application, listening on `0.0.0.0:8000` with `reload` enabled and `log_level` set to "info".
8.  Provides instructions for stopping the server and displays a webhook URL (hardcoded: `https://da3b21fd5fff.ngrok-free.app/webhook/git`).
9.  Handles `KeyboardInterrupt` to gracefully stop the server and other exceptions during server startup.

**Returns:**

*   `bool`: `True` if all operations complete successfully, `False` if any step fails.

### Usage Example

To run the Git operations and start the server, execute the script directly:

```bash
python3 start_server.py
```

This will automatically add, commit, and push current changes, then launch the server.

---

## File: `test_feature.py`

This file implements a dynamic programming approach to calculate Fibonacci numbers and includes a test function to verify its correctness.

### Functions

#### `calculate_fibonacci(n)`

Calculate the nth Fibonacci number using dynamic programming.

**Arguments:**

*   `n` (`int`): The position in the Fibonacci sequence.

**Returns:**

*   `int`: The nth Fibonacci number. Returns 0 for `n <= 0`, and 1 for `n = 1` or `n = 2`.

#### `test_fibonacci()`

Test the Fibonacci function. This function runs `calculate_fibonacci` against a predefined set of test cases (0, 1, 2, 3, 5, 8, 13, 21, 34 corresponding to `fib(0)` through `fib(8)`) and prints whether each test case passes or fails.

### Usage Example

When executed as the main script, `test_feature.py` will run the `test_fibonacci` function.

```python
if __name__ == "__main__":
    test_fibonacci()
```