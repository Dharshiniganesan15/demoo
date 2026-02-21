# Project Documentation

This documentation details the functionality of the provided Python code files, outlining the purpose of each module, its functions, and their usage.

---

## Table of Contents

*   [Overview](#overview)
*   [Modules](#modules)
    *   [demo_new_module.py](#demo_new_modulepy)
    *   [main.py](#mainpy)
    *   [math_utils.py](#math_utilspy)
    *   [new_feature.py](#new_featurepy)
    *   [start_server.py](#start_serverpy)
    *   [test_feature.py](#test_featurepy)

---

## Overview

This project consists of several Python scripts demonstrating various functionalities, including basic arithmetic operations, string greetings, advanced calculation features (though with an architectural pattern that makes them internally scoped), Fibonacci sequence calculation, and a utility script for automated Git operations and server startup.

---

## Modules

### `demo_new_module.py`

A simple module demonstrating a basic greeting function and its usage within a demo runner.

#### Functions

##### `greet(name: str) -> str`

Returns a personalized greeting message.

*   **Parameters:**
    *   `name` (`str`): The name to include in the greeting.
*   **Returns:**
    *   `str`: A string containing "Hello, {name}!".

##### `run_demo() -> None`

Prints a greeting message using the `greet` function with a predefined name.

*   **Returns:**
    *   `None`

#### Usage

When executed directly, this script will call `run_demo()`, which in turn prints "Hello, AI Doc System!".

```python
if __name__ == "__main__":
    run_demo()
```

---

### `main.py`

This module provides fundamental arithmetic operations.

#### Functions

##### `sum(a, b)`

Adds two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The sum of `a` and `b`.

##### `sub(a, b)`

Subtracts `b` from `a`.

*   **Parameters:**
    *   `a`: The minuend.
    *   `b`: The subtrahend.
*   **Returns:**
    *   The result of `a - b`.

##### `multiply(a, b)`

Multiplies two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

##### `divide(a, b)`

Divides `a` by `b` with a zero check.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The result of `a / b`.
*   **Raises:**
    *   `ValueError`: If `b` is `0`.

---

### `math_utils.py`

This module contains common mathematical utility functions for basic operations.

#### Functions

##### `multiply(a, b)`

Multiplies two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

##### `divide(a, b)`

Divides two numbers.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The result of `a / b`.
*   **Raises:**
    *   `ValueError`: If `b` is `0`.

##### `power(base, exponent)`

Calculates `base` raised to the power of `exponent`.

*   **Parameters:**
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns:**
    *   The result of `base ** exponent`.

---

### `new_feature.py`

This module introduces an `advanced_calculator` function that encapsulates several arithmetic operations as nested functions, along with a `test_calculator` function to demonstrate their (attempted) usage.

#### Functions

##### `advanced_calculator()`

This function defines several arithmetic operations as nested functions (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, `factorial`). These nested functions are scoped within `advanced_calculator` and are not directly accessible from outside the function's scope.

**Nested Functions:**

*   **`add(a, b)`:** Returns the sum of `a` and `b`.
*   **`subtract(a, b)`:** Returns the result of `a - b`.
*   **`multiply(a, b)`:** Returns the product of `a` and `b`.
*   **`divide(a, b)`:** Returns the result of `a / b`. Returns "Error: Division by zero" if `b` is `0`.
*   **`modulo(a, b)`:** Returns the remainder of `a / b`. Returns "Error: Modulo by zero" if `b` is `0`.
*   **`power(base, exponent)`:** Calculates `base` raised to the `exponent` using a loop.
*   **`factorial(n)`:** Calculates the factorial of `n`. Returns "Error: Negative number" if `n < 0`, returns `1` if `n == 0`.

##### `test_calculator()`

Attempts to test the operations defined within `advanced_calculator`. The current implementation of `test_calculator` tries to access the nested functions (e.g., `advanced_calculator.add`) as attributes of the `advanced_calculator` function itself. This will result in an `AttributeError` because these functions are not exposed as attributes of `advanced_calculator`.

#### Usage

When executed directly, this script will call `test_calculator()`, which will attempt to run tests for various arithmetic operations. Due to the scoping of `advanced_calculator`'s nested functions, these tests will encounter `AttributeError`s as written.

```python
if __name__ == "__main__":
    test_calculator()
```

---

### `start_server.py`

This script provides utilities for performing Git operations (add, commit, push) and then starting a FastAPI server using `uvicorn`.

#### Functions

##### `run_command(cmd, cwd=None)`

Executes a shell command and prints its output. Handles errors during command execution.

*   **Parameters:**
    *   `cmd` (`str`): The command string to execute.
    *   `cwd` (`str`, optional): The current working directory to run the command in. Defaults to `None` (current directory of the script).
*   **Returns:**
    *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

##### `main()`

The main function orchestrates the Git operations and server startup.

1.  **Changes Directory:** Changes to the parent directory of the script's location (`demoo_dir`).
2.  **Git Add:** Stages all changes in the current directory (`git add .`).
3.  **Git Commit:** Commits staged changes with an auto-generated commit message including a timestamp.
4.  **Git Push:** Pushes committed changes to the remote repository.
5.  **Changes Directory:** Switches back to the project root directory.
6.  **Start Server:** Attempts to start a FastAPI server using `uvicorn` on `http://0.0.0.0:8000`. It assumes a `backend.app:app` module is available for `uvicorn` to run. It also prints a placeholder webhook URL. The server runs with `reload=True` and `log_level="info"`.

*   **Returns:**
    *   `bool`: `True` if all operations are successful, `False` if any step (git command or server start) fails.

#### Dependencies

*   `os`: For changing directories and path manipulation.
*   `subprocess`: For running shell commands.
*   `time`: For generating timestamps for commit messages.
*   `sys`: Standard system module.
*   `pathlib.Path`: For path manipulation.
*   `uvicorn`: An ASGI web server implementation (imported dynamically).

#### Usage

When executed directly, this script will:
1.  Perform `git add .`, `git commit`, and `git push` in the script's parent directory.
2.  Then, it will attempt to start a `uvicorn` server, expecting a FastAPI application at `backend.app:app`.

```bash
#!/usr/bin/env python3

# Example execution:
# python start_server.py
```

```python
if __name__ == "__main__":
    main()
```

---

### `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and includes a test suite for this function.

#### Functions

##### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

*   **Parameters:**
    *   `n` (`int`): The position in the Fibonacci sequence (0-indexed).
*   **Returns:**
    *   `int`: The nth Fibonacci number. Returns `0` for `n <= 0`, `1` for `n == 1` or `n == 2`.

##### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases. It prints the input, calculated result, expected result, and a pass/fail status for each test case.

#### Usage

When executed directly, this script will call `test_fibonacci()`, which runs the tests for the Fibonacci function and prints the results.

```python
if __name__ == "__main__":
    test_fibonacci()
```