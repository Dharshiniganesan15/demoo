This document provides comprehensive documentation for the Python codebase, analyzing each file and its components based strictly on the provided code.

---

# Python Codebase Documentation

This repository contains various Python scripts demonstrating basic utilities, mathematical operations, a feature in development, and a server management script with Git integration.

## Table of Contents

*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
*   [File: `main.py`](#file-mainpy)
*   [File: `math_utils.py`](#file-math_utilspy)
*   [File: `new_feature.py`](#file-new_featurepy)
*   [File: `start_server.py`](#file-start_serverpy)
*   [File: `test_feature.py`](#file-test_featurepy)

---

### File: `demo_new_module.py`

This module contains simple functions to demonstrate a basic greeting and a demo execution.

#### Functions

*   `greet(name: str) -> str`
    *   **Description**: Generates a personalized greeting message.
    *   **Parameters**:
        *   `name` (`str`): The name to be included in the greeting.
    *   **Returns**:
        *   `str`: A string containing the greeting, e.g., "Hello, [name]!".

*   `run_demo() -> None`
    *   **Description**: Executes a demonstration by printing a greeting for "AI Doc System" to the console.
    *   **Parameters**: None
    *   **Returns**: None

#### Usage Example

When executed as the main script, `demo_new_module.py` will call `run_demo()`:

```python
if __name__ == "__main__":
    run_demo()
```

---

### File: `main.py`

This module provides fundamental arithmetic operations.

#### Functions

*   `sum(a, b)`
    *   **Description**: Add two numbers together.
    *   **Parameters**:
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns**: The sum of `a` and `b`.

*   `sub(a, b)`
    *   **Description**: Subtract b from a.
    *   **Parameters**:
        *   `a`: The number from which `b` will be subtracted.
        *   `b`: The number to subtract.
    *   **Returns**: The result of `a - b`.

*   `multiply(a, b)`
    *   **Description**: Multiply two numbers together.
    *   **Parameters**:
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns**: The product of `a` and `b`.

*   `divide(a, b)`
    *   **Description**: Divide a by b with zero check.
    *   **Parameters**:
        *   `a`: The numerator.
        *   `b`: The denominator.
    *   **Returns**: The result of `a / b`.
    *   **Raises**:
        *   `ValueError`: If `b` is `0`, indicating division by zero.

---

### File: `math_utils.py`

This module offers a collection of mathematical utilities for basic operations, including multiplication, division, and exponentiation.

#### Functions

*   `multiply(a, b)`
    *   **Description**: Multiply two numbers together.
    *   **Parameters**:
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns**: The product of `a` and `b`.

*   `divide(a, b)`
    *   **Description**: Divide two numbers.
    *   **Parameters**:
        *   `a`: The numerator.
        *   `b`: The denominator.
    *   **Returns**: The result of `a / b`.
    *   **Raises**:
        *   `ValueError`: If `b` is `0`, indicating division by zero.

*   `power(base, exponent)`
    *   **Description**: Calculate base raised to the power of exponent.
    *   **Parameters**:
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns**: The result of `base ** exponent`.

---

### File: `new_feature.py`

This module defines an `advanced_calculator` function which internally defines various arithmetic and mathematical operations. It also includes a testing function for these operations.

#### Functions

*   `advanced_calculator()`
    *   **Description**: Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, division, modulo, power, and factorial.
    *   **Internal Functions**: This function defines several nested functions (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, `factorial`). These functions are scoped within `advanced_calculator` and are not directly accessible from outside this function unless `advanced_calculator` returns them (which it does not in the current implementation).
        *   `add(a, b)`: Returns the sum of `a` and `b`.
        *   `subtract(a, b)`: Returns the difference `a - b`.
        *   `multiply(a, b)`: Returns the product of `a` and `b`.
        *   `divide(a, b)`: Returns the quotient `a / b`. Returns "Error: Division by zero" if `b` is `0`.
        *   `modulo(a, b)`: Returns the remainder of `a % b`. Returns "Error: Modulo by zero" if `b` is `0`.
        *   `power(base, exponent)`: Calculates `base` raised to the `exponent` using a loop.
        *   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative. Returns `1` if `n` is `0`.
    *   **Parameters**: None
    *   **Returns**: None

*   `test_calculator()`
    *   **Description**: Attempts to test the operations defined within `advanced_calculator`.
    *   **Note**: As `advanced_calculator` is defined as a function containing nested functions that are not returned or otherwise exposed, direct access using `advanced_calculator.add`, `advanced_calculator.subtract`, etc., will result in an `AttributeError` when this test function is executed. The code as written *attempts* to test these operations but will fail due to the scope of the nested functions.
    *   **Parameters**: None
    *   **Returns**: None (Prints test results to console).

#### Usage Example

When executed as the main script, `new_feature.py` will call `test_calculator()`:

```python
if __name__ == "__main__":
    test_calculator()
```

---

### File: `start_server.py`

This script is designed to automate a Git workflow (add, commit, push) and then start a FastAPI server. It includes utility functions for running shell commands.

#### Shebang

`#!/usr/bin/env python3` ensures the script is executed using the specified Python 3 interpreter.

#### Imports

The script uses standard Python libraries:
*   `os`: For interacting with the operating system, like changing directories.
*   `subprocess`: For running external commands (e.g., Git commands).
*   `time`: For time-related operations, specifically for generating commit messages.
*   `sys`: Provides access to system-specific parameters and functions.
*   `pathlib`: For object-oriented filesystem paths.
*   `uvicorn`: A lightning-fast ASGI server, used to run the FastAPI application.

#### Functions

*   `run_command(cmd, cwd=None)`
    *   **Description**: Runs a shell command and captures its output and error. It provides feedback on success or failure and prints the command's standard output.
    *   **Parameters**:
        *   `cmd` (`str`): The command string to execute.
        *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`, meaning the current directory of the Python script.
    *   **Returns**:
        *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

*   `main()`
    *   **Description**: The main function orchestrates the Git operations and server startup.
    *   **Workflow**:
        1.  **Directory Setup**: Determines the `demoo` directory (parent of the script) and the project root (parent of `demoo`).
        2.  **Git Operations**:
            *   Changes the current directory to `demoo_dir`.
            *   Executes `git add .` to stage all changes.
            *   Executes `git commit` with an auto-generated timestamped message.
            *   Executes `git push` to push changes to the remote repository.
            *   Error messages are printed if any Git command fails.
        3.  **Server Startup**:
            *   Changes the current directory back to `project_root`.
            *   Imports `uvicorn` and starts a FastAPI server.
            *   The server is configured to run `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
            *   Prints a hardcoded webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
            *   Handles `KeyboardInterrupt` to gracefully stop the server.
            *   Prints an error if the server fails to start.
    *   **Parameters**: None
    *   **Returns**:
        *   `bool`: `True` if all operations complete successfully, `False` otherwise.

#### Usage Example

When executed as the main script, `start_server.py` will call `main()`:

```python
if __name__ == "__main__":
    main()
```

---

### File: `test_feature.py`

This module implements and tests a function to calculate Fibonacci numbers using dynamic programming.

#### Functions

*   `calculate_fibonacci(n)`
    *   **Description**: Calculate the nth Fibonacci number using dynamic programming.
    *   **Parameters**:
        *   `n` (`int`): The position in the Fibonacci sequence (0-indexed).
    *   **Returns**:
        *   `int`: The nth Fibonacci number. Returns `0` for `n <= 0`, `1` for `n = 1` or `n = 2`.
    *   **Implementation Details**:
        *   Uses a dynamic programming (DP) table `fib` to store computed Fibonacci numbers, preventing redundant calculations.
        *   Base cases `fib[0]=0`, `fib[1]=1`, `fib[2]=1` are initialized.
        *   The table is filled iteratively for `i` from `3` to `n`.

*   `test_fibonacci()`
    *   **Description**: Tests the `calculate_fibonacci` function with a predefined set of test cases.
    *   **Test Cases**: `[0, 1, 2, 3, 5, 8, 13, 21, 34]` correspond to `fib(0)` through `fib(8)`.
    *   **Parameters**: None
    *   **Returns**: None (Prints the results of each test case, indicating `✅ PASS` or `❌ FAIL`).

#### Usage Example

When executed as the main script, `test_feature.py` will call `test_fibonacci()`:

```python
if __name__ == "__main__":
    test_fibonacci()
```