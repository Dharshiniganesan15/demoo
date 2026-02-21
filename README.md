# Project Documentation

This document provides comprehensive and accurate documentation for the provided Python codebase, adhering strictly to the given code and avoiding any assumptions or inventions beyond what is explicitly present.

---

## Table of Contents

*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
*   [File: `main.py`](#file-mainpy)
*   [File: `math_utils.py`](#file-math_utilspy)
*   [File: `new_feature.py`](#file-new_featurepy)
*   [File: `start_server.py`](#file-start_serverpy)
*   [File: `test_feature.py`](#file-test_featurepy)

---

## File: `demo_new_module.py`

This module contains a simple greeting function and a demonstration of its usage.

### Functions

#### `greet(name: str) -> str`

Generates a personalized greeting message.

*   **Parameters:**
    *   `name` (`str`): The name to be included in the greeting.
*   **Returns:**
    *   (`str`): A string formatted as "Hello, {name}!".

#### `run_demo() -> None`

Calls the `greet` function with a hardcoded name "AI Doc System" and prints the returned greeting.

*   **Parameters:** None
*   **Returns:**
    *   (`None`)

### Script Execution

When this script is executed directly (`if __name__ == "__main__":`), the `run_demo()` function is called, which in turn prints a greeting message to the console.

---

## File: `main.py`

This module provides a collection of fundamental arithmetic operations.

### Functions

#### `sum(a, b)`

Adds two numbers together.

*   **Description:** Add two numbers together.
*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts `b` from `a`.

*   **Description:** Subtract b from a.
*   **Parameters:**
    *   `a`: The minuend.
    *   `b`: The subtrahend.
*   **Returns:**
    *   The difference of `a` and `b`.

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Description:** Multiply two numbers together.
*   **Parameters:**
    *   `a`: The first factor.
    *   `b`: The second factor.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides `a` by `b` with a check to prevent division by zero.

*   **Description:** Divide a by b with zero check.
*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The quotient of `a` divided by `b`.
*   **Raises:**
    *   `ValueError`: If `b` is 0, indicating an attempt to divide by zero.

### Comments

The file includes a comment indicating "Test with Gemini AI documentation - 2026-01-30".

---

## File: `math_utils.py`

This module provides a collection of basic mathematical utility functions.

*   **Description:** Math utilities for basic operations

### Functions

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Description:** Multiply two numbers together.
*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides two numbers with a check to prevent division by zero.

*   **Description:** Divide two numbers.
*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The quotient of `a` divided by `b`.
*   **Raises:**
    *   `ValueError`: If `b` is 0, indicating an attempt to divide by zero.

#### `power(base, exponent)`

Calculates the result of raising a base number to a specified exponent.

*   **Description:** Calculate base raised to the power of exponent.
*   **Parameters:**
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns:**
    *   The result of `base` raised to the power of `exponent` (`base ** exponent`).

---

## File: `new_feature.py`

This module defines an `advanced_calculator` function containing several arithmetic operations as nested functions, and a `test_calculator` function designed to test these operations.

### Functions

#### `advanced_calculator()`

Defines several arithmetic and mathematical operations internally.

*   **Description:** Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, and division.
*   **Internal Functions (Local Scope):**
    *   `add(a, b)`: Returns the sum of `a` and `b`.
    *   `subtract(a, b)`: Returns the difference of `a` and `b`.
    *   `multiply(a, b)`: Returns the product of `a` and `b`.
    *   `divide(a, b)`: Returns the quotient of `a` divided by `b`. If `b` is 0, it returns the string "Error: Division by zero".
    *   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. If `b` is 0, it returns the string "Error: Modulo by zero".
    *   `power(base, exponent)`: Calculates `base` raised to the `exponent` using a loop.
    *   `factorial(n)`: Calculates the factorial of `n`. If `n` is negative, it returns "Error: Negative number". If `n` is 0, it returns 1. Otherwise, it calculates the product of integers from 1 to `n`.
*   **Note:** The operations defined within `advanced_calculator` are local to that function's scope and are not directly accessible from outside the `advanced_calculator` function itself. The function `advanced_calculator` itself does not return these nested functions or any object that exposes them.

#### `test_calculator()`

Attempts to test the operations defined within `advanced_calculator`.

*   **Description:** Test the advanced calculator
*   **Logic:** This function attempts to call the nested operations of `advanced_calculator` using the syntax `advanced_calculator.operation_name`. Given the scope of the nested functions, these calls will result in `AttributeError` exceptions at runtime because the internal functions are not attributes of the `advanced_calculator` function object. The function includes `print` statements to display the expected calculations and a pass/fail status for each attempted operation.
*   **Parameters:** None
*   **Returns:**
    *   (`None`)

### Script Execution

When this script is executed directly (`if __name__ == "__main__":`), the `test_calculator()` function is called. This will initiate attempts to test the advanced calculator operations, which will likely lead to runtime errors due to the incorrect method of accessing the nested functions.

---

## File: `start_server.py`

This module provides functionality to automate a Git commit and push, followed by starting a FastAPI server using Uvicorn.

*   **Description:** Start server with single automatic git push

### Shebang

The script begins with `#!/usr/bin/env python3`, indicating it is intended to be executed as a Python 3 script.

### Imports

The module imports the following standard Python libraries:
*   `os`: For interacting with the operating system, like changing directories.
*   `subprocess`: For running external commands, such as Git commands.
*   `time`: For time-related operations, specifically for generating commit messages.
*   `sys`: For system-specific parameters and functions (though not explicitly used in the provided code logic).
*   `pathlib.Path`: For object-oriented filesystem paths.

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command and captures its output and return status.

*   **Description:** Run a command and return the result.
*   **Parameters:**
    *   `cmd` (`str`): The command string to execute in the shell.
    *   `cwd` (`str`, optional): The current working directory in which to run the command. If `None`, the command is run in the current directory of the Python script.
*   **Returns:**
    *   (`bool`): `True` if the command executes successfully (i.g., returns with an exit code of 0); `False` otherwise. Prints error messages to `stderr` and success messages/output to `stdout`.

#### `main()`

The main function orchestrates the Git operations and server startup.

*   **Description:** Main function to start server with single git push.
*   **Workflow:**
    1.  **Directory Setup:** Determines the script's directory (`demoo_dir`) and its parent directory (`project_root`).
    2.  **Git Operations:**
        *   Changes the current working directory to `demoo_dir`.
        *   **Add Changes:** Executes `git add .` to stage all changes in the `demoo_dir`.
        *   **Commit Changes:** Executes `git commit` with an auto-generated, timestamped commit message (e.g., "Auto-update documentation - YYYY-MM-DD HH:MM:SS"). Prints a message if there are no changes to commit or if the commit fails.
        *   **Push Changes:** Executes `git push` to upload the committed changes to the remote repository. This is explicitly noted as a "once" operation.
    3.  **Server Startup:**
        *   Changes the current working directory back to `project_root`.
        *   Attempts to start a FastAPI server using `uvicorn`. It expects an application at `backend.app:app`.
        *   The server is configured to listen on `http://0.0.0.0:8000`, with `reload=True` enabled and `log_level="info"`.
        *   Prints information about the server's expected address and a webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
        *   Includes error handling for `KeyboardInterrupt` (to stop the server gracefully) and general exceptions during server startup.
*   **Parameters:** None
*   **Returns:**
    *   (`bool`): `True` if all Git operations succeed and the server starts successfully; `False` if any critical step (adding, pushing git changes, or server startup) fails.

### Script Execution

When this script is executed directly (`if __name__ == "__main__":`), the `main()` function is called, initiating the sequence of Git operations and the Uvicorn server startup.

---

## File: `test_feature.py`

This module provides a function for calculating Fibonacci numbers using dynamic programming and includes a test suite for verifying its correctness.

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using a dynamic programming approach.

*   **Description:** Calculate the nth Fibonacci number using dynamic programming.
*   **Parameters:**
    *   `n` (`int`): The position in the Fibonacci sequence (0-indexed or 1-indexed based on the sequence `0, 1, 1, 2, 3...`).
*   **Returns:**
    *   (`int`): The nth Fibonacci number.
*   **Logic:**
    *   For `n <= 0`, returns 0.
    *   For `n == 1` or `n == 2`, returns 1.
    *   For `n > 2`, it initializes a list `fib` of size `n+1`. It sets `fib[0]=0`, `fib[1]=1`, `fib[2]=1`, and then iteratively computes `fib[i] = fib[i-1] + fib[i-2]` for `i` from 3 to `n`. Finally, it returns `fib[n]`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases.

*   **Description:** Test the Fibonacci function
*   **Logic:** Iterates through a list of expected Fibonacci values (`[0, 1, 2, 3, 5, 8, 13, 21, 34]`). For each index `i` and its corresponding expected value, it calls `calculate_fibonacci(i)` and prints the result, along with a "✅ PASS" or "❌ FAIL" status indicator.
*   **Parameters:** None
*   **Returns:**
    *   (`None`)

### Script Execution

When this script is executed directly (`if __name__ == "__main__":`), the `test_fibonacci()` function is called, which runs the test suite for the Fibonacci calculation.