# Project Documentation

This document provides a comprehensive overview of the Python codebase, detailing the purpose of each file, its functions, and their intended behavior, strictly based on the provided source code.

## Table of Contents
*   [Overview](#overview)
*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
*   [File: `main.py`](#file-mainpy)
*   [File: `math_utils.py`](#file-math_utilspy)
*   [File: `new_feature.py`](#file-new_featurepy)
*   [File: `start_server.py`](#file-start_serverpy)
*   [File: `test_feature.py`](#file-test_featurepy)
*   [Dependencies](#dependencies)
*   [Execution](#execution)

## Overview

This collection of Python scripts demonstrates various functionalities including basic mathematical operations, advanced calculations, string manipulation, Fibonacci sequence calculation, and a script for automating Git pushes followed by starting a FastAPI server.

## File: `demo_new_module.py`

This module provides a simple greeting function and a demonstration of its usage.

### Functions

#### `greet(name: str) -> str`
Returns a personalized greeting string.

*   **Parameters**:
    *   `name` (`str`): The name to greet.
*   **Returns**:
    *   `str`: A string in the format "Hello, {name}!".

#### `run_demo() -> None`
Prints a demonstration of the `greet` function.

*   **Parameters**:
    *   None
*   **Returns**:
    *   `None`

### Execution

When executed as the main script, it calls `run_demo()` which will print "Hello, AI Doc System!".

```python
if __name__ == "__main__":
    run_demo()
```

## File: `main.py`

This module contains basic arithmetic functions.

### Functions

#### `sum(a, b)`
Adds two numbers together.

*   **Parameters**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    *   The sum of `a` and `b`.

#### `sub(a, b)`
Subtracts `b` from `a`.

*   **Parameters**:
    *   `a`: The number to subtract from.
    *   `b`: The number to subtract.
*   **Returns**:
    *   The result of `a - b`.

#### `multiply(a, b)`
Multiplies two numbers together.

*   **Parameters**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    *   The product of `a` and `b`.

#### `divide(a, b)`
Divides `a` by `b` with a zero check.

*   **Parameters**:
    *   `a`: The numerator.
    *   `b`: The denominator.
*   **Returns**:
    *   The result of `a / b`.
*   **Raises**:
    *   `ValueError`: If `b` is `0`.

### Note

The file contains a comment indicating "Test with Gemini AI documentation - 2026-01-30".

## File: `math_utils.py`

This module provides mathematical utilities for basic operations.

### Functions

#### `multiply(a, b)`
Multiplies two numbers together.

*   **Parameters**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    *   The product of `a` and `b`.

#### `divide(a, b)`
Divides two numbers.

*   **Parameters**:
    *   `a`: The numerator.
    *   `b`: The denominator.
*   **Returns**:
    *   The result of `a / b`.
*   **Raises**:
    *   `ValueError`: If `b` is `0`.

#### `power(base, exponent)`
Calculates `base` raised to the power of `exponent`.

*   **Parameters**:
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns**:
    *   The result of `base ** exponent`.

## File: `new_feature.py`

This module defines an "advanced calculator" with various operations and includes a testing function.

### Functions

#### `advanced_calculator()`
This function defines a set of inner helper functions (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, `factorial`) that perform various mathematical operations. These functions are defined within the local scope of `advanced_calculator` and are not directly accessible as attributes of the `advanced_calculator` function itself from outside its scope.

**Inner Functions Defined within `advanced_calculator`**:

*   **`add(a, b)`**: Returns the sum of `a` and `b`.
*   **`subtract(a, b)`**: Returns the result of `a - b`.
*   **`multiply(a, b)`**: Returns the product of `a` and `b`.
*   **`divide(a, b)`**: Returns the result of `a / b`. Returns "Error: Division by zero" if `b` is `0`.
*   **`modulo(a, b)`**: Returns the remainder of `a % b`. Returns "Error: Modulo by zero" if `b` is `0`.
*   **`power(base, exponent)`**: Calculates `base` raised to `exponent` using a loop.
*   **`factorial(n)`**: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is less than `0`. Returns `1` if `n` is `0`.

#### `test_calculator()`
This function is designed to test the operations defined within `advanced_calculator`. It *attempts* to call these operations as attributes of `advanced_calculator` (e.g., `advanced_calculator.add(5, 3)`). It prints the results of these attempted operations along with a pass/fail status indicated by emojis.

*   **Operations tested**: Addition, Subtraction, Multiplication, Division, Power, Factorial.

### Execution

When executed as the main script, it calls `test_calculator()` which will attempt to run the various calculator tests and print their outcomes.

```python
if __name__ == "__main__":
    test_calculator()
```

## File: `start_server.py`

This script is designed to automate a Git commit and push, and then start a FastAPI server.

### Functions

#### `run_command(cmd, cwd=None)`
Runs a shell command, captures its output, and checks for errors.

*   **Parameters**:
    *   `cmd` (`str`): The command string to execute.
    *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`.
*   **Returns**:
    *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.
    *   Prints success/error messages and command output to `stdout`.

#### `main()`
The main function orchestrates the Git operations and server startup.

1.  **Directory Navigation**: Determines the current script's directory and the project root. Changes the current working directory to `demoo_dir` for Git operations.
2.  **Git Operations**:
    *   Adds all changes to the Git staging area (`git add .`).
    *   Commits staged changes with an auto-generated commit message including a timestamp (e.g., "Auto-update documentation - YYYY-MM-DD HH:MM:SS").
    *   Pushes committed changes to the remote repository (`git push`).
    *   Each step prints status messages indicating success or failure.
3.  **Server Startup**:
    *   Changes the current working directory back to `project_root`.
    *   Attempts to import `uvicorn` and starts a FastAPI server.
    *   The server is configured to run on `http://0.0.0.0:8000`.
    *   It also prints a hardcoded "Webhook URL: https://da3b21fd5fff.ngrok-free.app/webhook/git".
    *   The server runs in `reload` mode with `info` log level.
    *   It handles `KeyboardInterrupt` for graceful shutdown and catches other exceptions during server startup.

### Execution

When executed as the main script, it calls `main()`.

```python
if __name__ == "__main__":
    main()
```

## File: `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and includes a testing function for it.

### Functions

#### `calculate_fibonacci(n)`
Calculates the nth Fibonacci number using dynamic programming.

*   **Parameters**:
    *   `n` (`int`): The position in the Fibonacci sequence.
*   **Returns**:
    *   `int`: The nth Fibonacci number.
*   **Behavior**:
    *   Returns `0` for `n <= 0`.
    *   Returns `1` for `n == 1` or `n == 2`.
    *   Uses a dynamic programming (DP) table to store and compute Fibonacci numbers iteratively.

#### `test_fibonacci()`
Tests the `calculate_fibonacci` function with a predefined set of test cases.

*   **Behavior**:
    *   Iterates through a list of expected Fibonacci numbers, calling `calculate_fibonacci` for each index.
    *   Prints the input, calculated result, expected result, and a pass/fail status for each test case.

### Execution

When executed as the main script, it calls `test_fibonacci()` which will run the Fibonacci tests and print their outcomes.

```python
if __name__ == "__main__":
    test_fibonacci()
```

## Dependencies

The following Python libraries are used or implicitly required by the scripts:

*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib` (specifically `pathlib.Path`)
*   `uvicorn` (implicitly required by `start_server.py` for server functionality)

## Execution

To run any of the executable Python scripts (those containing `if __name__ == "__main__":` blocks), use the Python interpreter from your terminal.

**Example:**

To run the `demo_new_module.py`:
```bash
python demo_new_module.py
```

To run the `new_feature.py` tests:
```bash
python new_feature.py
```

To run the `start_server.py` (which includes Git operations and server startup):
```bash
python start_server.py
```
*(Note: Running `start_server.py` will attempt to perform `git add`, `git commit`, `git push`, and then start a `uvicorn` server. Ensure you have Git configured and `uvicorn` installed (`pip install uvicorn`) before running this script.)*

To run the `test_feature.py` tests:
```bash
python test_feature.py
```