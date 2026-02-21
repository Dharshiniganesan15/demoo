This document provides a comprehensive overview of the Python codebase, detailing the purpose and functionality of each file and its contained functions, strictly based on the provided source code.

---

# Codebase Overview

This repository contains various Python utilities, including basic mathematical operations, an advanced calculator feature, Fibonacci sequence calculation, and a script for automating Git operations and starting a server.

## File: `main.py`

This file defines a set of fundamental arithmetic operations.

### Functions

#### `sum(a, b)`

Adds two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

*   **Parameters:**
    *   `a`: The number to subtract from.
    *   `b`: The number to subtract.
*   **Returns:**
    The result of `a - b`.

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    The product of `a` and `b`.

#### `divide(a, b)`

Divides `a` by `b`, including a check for division by zero.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Raises:**
    *   `ValueError`: If `b` is `0`.
*   **Returns:**
    The result of `a / b`.

### Notes

*   A comment indicates this file was "Test with Gemini AI documentation - 2026-01-30".

---

## File: `math_utils.py`

This file provides a collection of mathematical utility functions for basic operations.

### Functions

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    The product of `a` and `b`.

#### `divide(a, b)`

Divides `a` by `b`. Includes a check to prevent division by zero.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Raises:**
    *   `ValueError`: If `b` is `0`.
*   **Returns:**
    The result of `a / b`.

#### `power(base, exponent)`

Calculates the `base` raised to the power of `exponent`.

*   **Parameters:**
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns:**
    The result of `base ** exponent`.

---

## File: `new_feature.py`

This file introduces an `advanced_calculator` function that encapsulates several arithmetic and mathematical operations, along with a testing utility.

### Functions

#### `advanced_calculator()`

This function serves as a container for several nested mathematical operation functions. When called, it defines these inner functions but does not execute them or return them directly.

*   **Supports:** Addition, subtraction, multiplication, division, modulo, power, and factorial.

##### Nested Functions defined within `advanced_calculator`:

*   **`add(a, b)`**: Returns the sum of `a` and `b`.
*   **`subtract(a, b)`**: Returns the difference of `a` and `b`.
*   **`multiply(a, b)`**: Returns the product of `a` and `b`.
*   **`divide(a, b)`**: Returns the result of `a / b`. If `b` is `0`, it returns the string `"Error: Division by zero"`.
*   **`modulo(a, b)`**: Returns the remainder of `a % b`. If `b` is `0`, it returns the string `"Error: Modulo by zero"`.
*   **`power(base, exponent)`**: Calculates `base` raised to the `exponent` using a loop.
*   **`factorial(n)`**: Calculates the factorial of `n`.
    *   Returns `"Error: Negative number"` if `n` is less than `0`.
    *   Returns `1` if `n` is `0`.
    *   Calculates the factorial using a loop for `n > 0`.

#### `test_calculator()`

Tests the functionality of the operations intended to be part of the `advanced_calculator`. This function attempts to call the nested functions (e.g., `advanced_calculator.add`), assuming they are accessible as attributes of the `advanced_calculator` function object. It prints the results of various test cases for addition, subtraction, multiplication, division, power, and factorial, indicating whether each test passed or failed.

### Script Execution

If `new_feature.py` is executed as the main script, `test_calculator()` will be called, performing and printing the results of the described tests.

---

## File: `start_server.py`

This script automates Git operations (add, commit, push) and subsequently starts a server using `uvicorn`.

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command, captures its output, and prints success or error messages.

*   **Parameters:**
    *   `cmd` (str): The command to execute.
    *   `cwd` (str, optional): The current working directory for the command. Defaults to `None`, meaning the current process's working directory.
*   **Returns:**
    *   `True` if the command executes successfully (return code 0).
    *   `False` if an error occurs during execution or the command returns a non-zero exit code.
*   **Prints:**
    *   "Error running {cmd}: {stderr}" on command failure.
    *   "Success: {cmd}" on command success.
    *   "Output: {stdout.strip()}" if the command produces standard output.
    *   "Exception running {cmd}: {e}" if an unexpected exception occurs.

#### `main()`

The primary function to execute the server startup process.

1.  **Directory Setup**: Determines the project root and the script's directory (`demoo_dir`).
2.  **Git Operations**:
    *   Changes the current directory to `demoo_dir`.
    *   Adds all changes to Git staging (`git add .`).
    *   Commits changes with a timestamped message (e.g., "Auto-update documentation - YYYY-MM-DD HH:MM:SS").
    *   Pushes committed changes to the remote repository (`git push`).
3.  **Server Startup**:
    *   Changes the current directory back to `project_root`.
    *   Imports `uvicorn`.
    *   Prints server information, including the local address (`http://localhost:8000`) and a webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Starts a `uvicorn` server by running `backend.app:app` on `0.0.0.0:8000` with `reload` enabled and `info` log level.
    *   Handles `KeyboardInterrupt` to gracefully stop the server.
    *   Catches general exceptions during server startup.

### Script Execution

If `start_server.py` is executed as the main script, `main()` will be called, which performs the Git operations and then starts the `uvicorn` server.

---

## File: `test_feature.py`

This file contains functions for calculating Fibonacci numbers using dynamic programming and a corresponding test suite.

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

*   **Parameters:**
    *   `n` (int): The position in the Fibonacci sequence (0-indexed or 1-indexed, based on the `test_fibonacci` behavior which tests `fib(0)` as 0, `fib(1)` as 1, etc.).
*   **Returns:**
    *   `int`: The nth Fibonacci number.
*   **Logic:**
    *   Returns `0` if `n <= 0`.
    *   Returns `1` if `n == 1` or `n == 2`.
    *   Initializes a DP table `fib` with `fib[0]=0`, `fib[1]=1`, `fib[2]=1`.
    *   Iteratively fills the `fib` table from `i=3` up to `n` using the recurrence `fib[i] = fib[i-1] + fib[i-2]`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases.

*   **Test Cases:** `[0, 1, 2, 3, 5, 8, 13, 21, 34]` for `fib(0)` to `fib(8)` respectively.
*   **Prints:** For each test case, it displays the input `n`, the calculated result, the expected result, and a `✅ PASS` or `❌ FAIL` status.

### Script Execution

If `test_feature.py` is executed as the main script, `test_fibonacci()` will be called, running the Fibonacci function tests and printing their outcomes.