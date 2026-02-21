This document provides an overview of the Python codebase, detailing the functionality found within each script. The documentation is generated directly from the provided source code, adhering strictly to the implemented features without inferring or assuming additional capabilities.

## Codebase Overview

This collection of Python scripts demonstrates various functionalities including basic arithmetic operations, a greeting utility, a Fibonacci sequence calculator, and a script for automating Git operations and starting a FastAPI server.

## Table of Contents

*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
*   [File: `main.py`](#file-mainpy)
*   [File: `math_utils.py`](#file-math_utilspy)
*   [File: `new_feature.py`](#file-new_featurepy)
*   [File: `start_server.py`](#file-start_serverpy)
*   [File: `test_feature.py`](#file-test_featurepy)

---

### File: `demo_new_module.py`

This script contains functions for generating a simple greeting and demonstrating its usage.

#### `greet(name: str) -> str`

Returns a personalized greeting message.

*   **Parameters:**
    *   `name` (`str`): The name to include in the greeting.
*   **Returns:**
    *   `str`: A string in the format "Hello, {name}!".

#### `run_demo() -> None`

Executes a demonstration of the `greet` function by printing a greeting to "AI Doc System".

*   **Parameters:**
    *   None
*   **Returns:**
    *   `None`

#### Execution (`if __name__ == "__main__":`)

When executed as a standalone script, `run_demo()` is called, which prints the greeting "Hello, AI Doc System!".

---

### File: `main.py`

This script provides fundamental arithmetic operations.

#### `sum(a, b)`

Adds two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

*   **Parameters:**
    *   `a`: The number to subtract from.
    *   `b`: The number to subtract.
*   **Returns:**
    *   The result of `a - b`.

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Raises:**
    *   `ValueError`: If `b` is `0`.
*   **Returns:**
    *   The result of `a / b`.

---

### File: `math_utils.py`

This module provides basic mathematical utility functions.

#### Module Docstring

```
Math utilities for basic operations
```

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Raises:**
    *   `ValueError`: If `b` is `0`.
*   **Returns:**
    *   The result of `a / b`.

#### `power(base, exponent)`

Calculates the `base` raised to the power of the `exponent`.

*   **Parameters:**
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns:**
    *   The result of `base ** exponent`.

---

### File: `new_feature.py`

This script defines an "advanced calculator" function which encapsulates several arithmetic and mathematical operations, and includes a test suite for these operations.

#### `advanced_calculator()`

This function is intended to represent an advanced calculator. It defines several nested helper functions for arithmetic and mathematical operations:

*   **`add(a, b)`**: Returns the sum of `a` and `b`.
*   **`subtract(a, b)`**: Returns the difference of `a` and `b`.
*   **`multiply(a, b)`**: Returns the product of `a` and `b`.
*   **`divide(a, b)`**: Returns the quotient of `a` and `b`. If `b` is `0`, it returns the string "Error: Division by zero".
*   **`modulo(a, b)`**: Returns the remainder of `a` divided by `b`. If `b` is `0`, it returns the string "Error: Modulo by zero".
*   **`power(base, exponent)`**: Calculates `base` raised to the `exponent` using a loop.
*   **`factorial(n)`**: Calculates the factorial of `n`. Handles negative numbers by returning "Error: Negative number" and `0` by returning `1`.

*Note: The nested functions defined within `advanced_calculator` are local to its scope and are not directly accessible as methods of `advanced_calculator` itself without additional mechanisms like returning a class instance or a dictionary of functions.*

#### `test_calculator()`

This function tests the operations defined within `advanced_calculator`. It attempts to call the nested functions as attributes of `advanced_calculator` (e.g., `advanced_calculator.add(5, 3)`), prints the results, and indicates whether each test case passes or fails.

*   **Tests covered:**
    *   Addition (5 + 3)
    *   Subtraction (10 - 4)
    *   Multiplication (7 * 6)
    *   Division (15 / 3)
    *   Power (2^8)
    *   Factorial (5!)

#### Execution (`if __name__ == "__main__":`)

When executed as a standalone script, `test_calculator()` is called, which runs the defined tests and prints their outcomes.

---

### File: `start_server.py`

This script provides utilities to automate Git operations (add, commit, push) and then start a FastAPI server using `uvicorn`.

#### Module Docstring

```
Start server with single automatic git push
```

#### `run_command(cmd, cwd=None)`

Executes a given shell command. It captures output, checks for errors, and prints status messages.

*   **Parameters:**
    *   `cmd` (`str`): The command string to execute.
    *   `cwd` (`str`, optional): The working directory for the command. Defaults to `None` (current directory).
*   **Returns:**
    *   `bool`: `True` if the command executed successfully, `False` otherwise.

#### `main()`

The main function orchestrates the Git operations and server startup.

1.  **Directory Setup:** Determines the `demoo_dir` (directory of the script) and `project_root` (parent of `demoo_dir`).
2.  **Git Operations:**
    *   Changes the current working directory to `demoo_dir`.
    *   Adds all changes (`git add .`).
    *   Commits changes with an auto-generated timestamped message (e.g., "Auto-update documentation - YYYY-MM-DD HH:MM:SS").
    *   Pushes changes to the remote repository (`git push`).
3.  **Server Startup:**
    *   Changes the current working directory to `project_root`.
    *   Attempts to import `uvicorn` and start a FastAPI server.
    *   The server is configured to run `backend.app:app` (a module not provided in this codebase) on `http://0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Prints a hypothetical Webhook URL: `https://da3b21fd5fff.ngrok-free.app/webhook/git`.
    *   Handles `KeyboardInterrupt` to gracefully stop the server.
    *   Captures and prints other exceptions during server startup.
*   **Returns:**
    *   `bool`: `True` if the process completes, `False` if any critical step (Git or server start) fails.

#### Execution (`if __name__ == "__main__":`)

When executed as a standalone script, `main()` is called to perform the Git operations and attempt to start the server.

---

### File: `test_feature.py`

This script provides a function to calculate Fibonacci numbers using dynamic programming and a function to test it.

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using a dynamic programming approach.

*   **Parameters:**
    *   `n` (`int`): The position in the Fibonacci sequence (0-indexed).
*   **Returns:**
    *   `int`: The nth Fibonacci number. Returns `0` for `n <= 0`, `1` for `n == 1` or `n == 2`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases (0-th to 8-th Fibonacci numbers). It prints the input, calculated result, expected result, and a `✅ PASS` or `❌ FAIL` status for each test.

#### Execution (`if __name__ == "__main__":`)

When executed as a standalone script, `test_fibonacci()` is called to run the tests and print the results.

---

## Language Summary

All provided code snippets are written in **Python**.