This document provides comprehensive documentation for the provided Python codebase, adhering strictly to the code's content and structure without external assumptions.

---

# Python Codebase Documentation

This codebase comprises several Python modules demonstrating various functionalities, including basic arithmetic operations, string manipulation, Fibonacci sequence calculation, and a script for automating Git operations and starting a FastAPI server.

---

## `demo_new_module.py`

This module contains a simple greeting function and a demo runner.

### Functions

#### `greet(name: str) -> str`

Returns a personalized greeting message.

**Parameters:**

*   `name` (`str`): The name to be included in the greeting.

**Returns:**

*   `str`: A string in the format "Hello, {name}!".

**Example Usage (from `run_demo`):**

```python
name = "AI Doc System"
greeting = greet(name) # "Hello, AI Doc System!"
```

#### `run_demo() -> None`

Executes a demonstration of the `greet` function by printing a greeting to "AI Doc System".

**Example Usage (when run as main script):**

```
Hello, AI Doc System!
```

---

## `main.py`

This module provides a collection of fundamental arithmetic functions.

### Functions

#### `sum(a, b)`

Adds two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

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

Divides the first number (`a`) by the second number (`b`), with a check for division by zero.

**Parameters:**

*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**

*   The result of `a / b`.

**Raises:**

*   `ValueError`: If `b` is `0`, indicating an attempt to divide by zero.

#### `calculate_tax(income: float) -> float`

Calculates tax for a given income at a fixed 10% rate.

**Parameters:**

*   `income` (`float`): The taxable income amount.

**Returns:**

*   `float`: The computed tax amount (`income * 0.1`).

#### `average(a: float, b: float) -> float`

Calculates the arithmetic mean of two numbers.

**Parameters:**

*   `a` (`float`): First value.
*   `b` (`float`): Second value.

**Returns:**

*   `float`: The average value `((a + b) / 2)`.

**Internal Notes:**

*   A comment indicates "Test with Gemini AI documentation - 2026-01-30".

---

## `math_utils.py`

This module contains a set of utility functions for common mathematical operations.

**Module Docstring:**

```
Math utilities for basic operations
```

### Functions

#### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), with a check for division by zero.

**Parameters:**

*   `a`: The dividend.
*   `b`: The divisor.

**Returns:**

*   The result of `a / b`.

**Raises:**

*   `ValueError`: If `b` is `0`, indicating an attempt to divide by zero.

#### `power(base, exponent)`

Calculates the base raised to the power of the exponent.

**Parameters:**

*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**

*   The result of `base ** exponent`.

---

## `new_feature.py`

This module defines an `advanced_calculator` function which internally defines various arithmetic operations. It also includes a `test_calculator` function to demonstrate the intended use of these operations.

**Important Note:** The `advanced_calculator()` function defines nested functions (`add`, `subtract`, etc.) that are local to its scope. As written, these nested functions are not directly accessible from outside `advanced_calculator()` itself in the manner attempted by `test_calculator`. The `test_calculator` function's attempts to call `advanced_calculator.add`, `advanced_calculator.subtract`, etc., will result in an `AttributeError` at runtime, as `advanced_calculator` is a function object, not an object containing these methods.

### Functions

#### `advanced_calculator()`

Defines a set of nested functions for various mathematical operations:

*   `add(a, b)`: Returns the sum of `a` and `b`.
*   `subtract(a, b)`: Returns the difference of `a` and `b`.
*   `multiply(a, b)`: Returns the product of `a` and `b`.
*   `divide(a, b)`: Returns the division of `a` by `b`. Returns "Error: Division by zero" if `b` is `0`.
*   `modulo(a, b)`: Returns the modulo of `a` by `b`. Returns "Error: Modulo by zero" if `b` is `0`.
*   `power(base, exponent)`: Calculates `base` raised to `exponent` using a loop.
*   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n < 0`. Returns `1` if `n == 0`.

**Note:** As described above, these nested functions are not directly callable from the module scope.

#### `test_calculator()`

This function attempts to test the operations defined within `advanced_calculator`. It prints the results of various arithmetic operations (addition, subtraction, multiplication, division, power, factorial) and indicates whether each test passed or failed.

**Example Usage (when run as main script):**

```
Testing Advanced Calculator:
  5 + 3 = ... ❌ # This will fail due to AttributeError
  10 - 4 = ... ❌ # This will fail due to AttributeError
  7 * 6 = ... ❌ # This will fail due to AttributeError
  15 / 3 = ... ❌ # This will fail due to AttributeError
  2^8 = ... ❌ # This will fail due to AttributeError
  5! = ... ❌ # This will fail due to AttributeError
```

---

## `start_server.py`

This script automates Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

**Shebang:**

```python
#!/usr/bin/env python3
```

**Module Docstring:**

```
Start server with single automatic git push
```

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command using `subprocess`. It captures standard output and standard error, and prints messages indicating success or failure.

**Parameters:**

*   `cmd` (`str`): The command string to execute.
*   `cwd` (`str`, optional): The working directory for the command. Defaults to `None` (current working directory).

**Returns:**

*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

#### `main()`

The main function orchestrates the Git operations and server startup.

1.  **Determines Paths:** Identifies the current script's directory (`demoo_dir`) and the project root directory.
2.  **Git Operations:**
    *   Changes the current directory to `demoo_dir`.
    *   Adds all changes to Git staging (`git add .`).
    *   Commits changes with an auto-generated timestamped message (`git commit -m "Auto-update documentation - YYYY-MM-DD HH:MM:SS"`).
    *   Pushes the committed changes to the remote repository (`git push`).
3.  **Server Startup:**
    *   Changes the current directory back to `project_root`.
    *   Imports `uvicorn`.
    *   Starts a `uvicorn` server for `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Prints messages indicating the server's local URL and a webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Handles `KeyboardInterrupt` to gracefully stop the server and other exceptions during server startup.

**Returns:**

*   `bool`: `True` if all operations (Git and server start) are completed successfully, `False` if any step fails.

**Example Usage (when run as main script):**

```
Project root: /path/to/project_root
Demoo directory: /path/to/demoo_dir

=== Adding changes to git ===
Success: git add .

=== Committing changes ===
Success: git commit -m "Auto-update documentation - 2023-10-27 10:30:00"

=== Pushing to git (once) ===
Success: git push

=== Git push completed successfully! ===

=== Starting FastAPI server ===
Starting server on http://localhost:8000
Webhook URL: https://da3b21fd5fff.ngrok-free.app/webhook/git
Press Ctrl+C to stop the server
INFO:     Will watch for changes in these directories: ['/path/to/project_root']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [PID] using WatchFiles
INFO:     Started server process [PID]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
... (server logs)
```

---

## `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a test function to verify its correctness.

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using a dynamic programming approach.

**Parameters:**

*   `n` (`int`): The position in the Fibonacci sequence (0-indexed where fib(0)=0).

**Returns:**

*   `int`: The nth Fibonacci number.

**Logic:**

*   Returns `0` for `n <= 0`.
*   Returns `1` for `n == 1` or `n == 2`.
*   For `n >= 3`, it initializes a DP table `fib` and iteratively calculates `fib[i] = fib[i-1] + fib[i-2]`.

**Example Usage:**

```python
fib_5 = calculate_fibonacci(5) # 5
fib_0 = calculate_fibonacci(0) # 0
```

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases. It prints the expected and actual results for each test case, along with a "PASS" or "FAIL" status.

**Test Cases Covered:**

| Input `n` | Expected Fibonacci |
| :-------- | :----------------- |
| 0         | 0                  |
| 1         | 1                  |
| 2         | 1                  |
| 3         | 2                  |
| 4         | 5                  |
| 5         | 8                  |
| 6         | 13                 |
| 7         | 21                 |
| 8         | 34                 |

**Example Usage (when run as main script):**

```
Testing Fibonacci function:
  fib(0) = 0 (expected 0) ✅ PASS
  fib(1) = 1 (expected 1) ✅ PASS
  fib(2) = 1 (expected 1) ✅ PASS
  fib(3) = 2 (expected 3) ❌ FAIL # Note: The provided test case is fib(3) should be 2, but the test_cases array has 5 at index 4, which corresponds to fib(4). This discrepancy is reflected in the output from the provided code.
  fib(4) = 5 (expected 8) ❌ FAIL # Same discrepancy as above. The test_cases array elements are fib(0), fib(1), fib(2), fib(3), fib(4), fib(5), fib(6), fib(7), fib(8) according to the enumerate loop.
  ...
```
