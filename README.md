This document provides comprehensive documentation for the provided Python codebase, adhering strictly to the code's content without inventing or assuming any features.

---

# Codebase Documentation

This repository contains various Python utilities for mathematical operations, a sophisticated calculator feature, and a script for managing Git operations and starting a FastAPI server.

## Codebase Overview

The codebase is organized into several Python files, each serving a distinct purpose:

*   **`main.py`**: Contains fundamental arithmetic functions like addition, subtraction, multiplication, and division.
*   **`math_utils.py`**: Provides additional mathematical utilities, including multiplication, division, and power calculations.
*   **`new_feature.py`**: Introduces an `advanced_calculator` concept with a suite of arithmetic, modulo, power, and factorial operations, alongside a testing function.
*   **`start_server.py`**: A utility script designed to automate Git operations (add, commit, push) and subsequently start a FastAPI server using `uvicorn`.
*   **`test_feature.py`**: Implements a function to calculate Fibonacci numbers using dynamic programming and includes a dedicated test function.

## API Reference

This section details the functions available in each Python file.

### `main.py`

This file provides basic arithmetic operations.

#### `sum(a, b)`

Adds two numbers together.

```python
sum(a, b)
```

*   **Parameters**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts `b` from `a`.

```python
sub(a, b)
```

*   **Parameters**:
    *   `a`: The number from which to subtract.
    *   `b`: The number to subtract.
*   **Returns**:
    The result of `a - b`.

#### `multiply(a, b)`

Multiplies two numbers together.

```python
multiply(a, b)
```

*   **Parameters**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    The product of `a` and `b`.

#### `divide(a, b)`

Divides `a` by `b` with a zero check.

```python
divide(a, b)
```

*   **Parameters**:
    *   `a`: The numerator.
    *   `b`: The denominator.
*   **Returns**:
    The result of `a / b`.
*   **Raises**:
    *   `ValueError`: If `b` is `0`.

### `math_utils.py`

This file offers mathematical utilities for basic operations.

#### `multiply(a, b)`

Multiplies two numbers together.

```python
multiply(a, b)
```

*   **Parameters**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    The product of `a` and `b`.

#### `divide(a, b)`

Divides two numbers.

```python
divide(a, b)
```

*   **Parameters**:
    *   `a`: The numerator.
    *   `b`: The denominator.
*   **Returns**:
    The result of `a / b`.
*   **Raises**:
    *   `ValueError`: If `b` is `0`.

#### `power(base, exponent)`

Calculates `base` raised to the power of `exponent`.

```python
power(base, exponent)
```

*   **Parameters**:
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns**:
    The result of `base ** exponent`.

### `new_feature.py`

This file defines an `advanced_calculator` function that contains several nested arithmetic functions, and a `test_calculator` function that attempts to utilize them.

#### `advanced_calculator()`

An `advanced_calculator` function that internally defines multiple arithmetic operations. The docstring indicates it supports addition, subtraction, multiplication, and division. Note that the functions defined within `advanced_calculator` are local to its scope and, as implemented, are not directly callable as attributes of the `advanced_calculator` function object from external code.

```python
advanced_calculator()
```

This function contains the following nested definitions:

*   **`add(a, b)`**: Adds two numbers.
    *   **Returns**: The sum of `a` and `b`.
*   **`subtract(a, b)`**: Subtracts `b` from `a`.
    *   **Returns**: The result of `a - b`.
*   **`multiply(a, b)`**: Multiplies two numbers.
    *   **Returns**: The product of `a` and `b`.
*   **`divide(a, b)`**: Divides `a` by `b`.
    *   **Returns**: The result of `a / b`. If `b` is `0`, returns the string `"Error: Division by zero"`.
*   **`modulo(a, b)`**: Calculates the remainder of `a` divided by `b`.
    *   **Returns**: The result of `a % b`. If `b` is `0`, returns the string `"Error: Modulo by zero"`.
*   **`power(base, exponent)`**: Calculates `base` raised to the power of `exponent` using a loop.
    *   **Returns**: The calculated power.
*   **`factorial(n)`**: Calculates the factorial of `n`.
    *   **Returns**: The factorial of `n`. If `n` is negative, returns the string `"Error: Negative number"`. If `n` is `0`, returns `1`.

#### `test_calculator()`

This function is designed to test the operations defined within the `advanced_calculator`. It attempts to call the nested functions (e.g., `add`, `subtract`) by accessing them as attributes of the `advanced_calculator` function itself. The results of these test calls are printed to the console, along with a pass/fail indicator.

```python
test_calculator()
```

*   **Functionality**:
    *   Prints a header "Testing Advanced Calculator:".
    *   Attempts to test addition: `5 + 3`.
    *   Attempts to test subtraction: `10 - 4`.
    *   Attempts to test multiplication: `7 * 6`.
    *   Attempts to test division: `15 / 3`.
    *   Attempts to test power: `2^8`.
    *   Attempts to test factorial: `5!`.
    *   Each test prints the operation, result, expected value, and a "✅" for pass or "❌" for fail.

### `start_server.py`

This script is responsible for automating Git operations and initiating a FastAPI server.

#### `run_command(cmd, cwd=None)`

Executes a shell command and captures its output.

```python
run_command(cmd, cwd=None)
```

*   **Parameters**:
    *   `cmd` (`str`): The command string to execute.
    *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`.
*   **Returns**:
    `True` if the command executes successfully (return code 0), `False` otherwise.
    Prints success messages or error details to `stdout`/`stderr`.

#### `main()`

The main function orchestrates the Git operations and server startup.

```python
main()
```

*   **Functionality**:
    1.  Determines the project root and current script directory.
    2.  Changes the working directory to `demoo_dir` for Git operations.
    3.  **Git Operations**:
        *   Adds all changes to the Git staging area (`git add .`).
        *   Commits changes with an automatically generated message including a timestamp (e.g., `Auto-update documentation - YYYY-MM-DD HH:MM:SS`).
        *   Pushes committed changes to the remote Git repository (`git push`).
    4.  Changes the working directory back to `project_root`.
    5.  **Server Startup**:
        *   Attempts to import `uvicorn`.
        *   Starts a `uvicorn` server to run the FastAPI application located at `backend.app:app`.
        *   The server is configured to listen on `http://0.0.0.0:8000`.
        *   `reload` is set to `True`, and `log_level` to `"info"`.
        *   Prints a static webhook URL: `https://da3b21fd5fff.ngrok-free.app/webhook/git`.
        *   The server can be stopped by pressing `Ctrl+C`.
*   **Returns**:
    `True` if all operations complete successfully, `False` if any step fails.

### `test_feature.py`

This file contains a function for calculating Fibonacci numbers and a corresponding test function.

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

```python
calculate_fibonacci(n)
```

*   **Parameters**:
    *   `n` (`int`): The position in the Fibonacci sequence.
*   **Returns**:
    `int`: The nth Fibonacci number.
*   **Behavior**:
    *   If `n <= 0`, returns `0`.
    *   If `n == 1`, returns `1`.
    *   If `n == 2`, returns `1`.
    *   For `n > 2`, it calculates the number using a DP table: `fib[i] = fib[i-1] + fib[i-2]`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function with a predefined set of test cases.

```python
test_fibonacci()
```

*   **Functionality**:
    *   Prints a header "Testing Fibonacci function:".
    *   Iterates through a list of expected Fibonacci numbers: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`. (Note: The `test_cases` list provided in the code is `[0, 1, 2, 3, 5, 8, 13, 21, 34]` which actually corresponds to fib(0) to fib(8) respectively, with fib(2) being 1, but the list shows 2. This seems to be a slight mismatch in the expected values array vs. the true Fibonacci sequence.)
    *   For each index `i` and expected value, it calls `calculate_fibonacci(i)` and prints whether the result matches the expected value, marking it "✅ PASS" or "❌ FAIL".