# Project Documentation

This repository contains various Python scripts for mathematical operations, an advanced calculator feature, and a utility script for automating Git operations and starting a server.

## Files

### `main.py`

This file provides a collection of fundamental arithmetic functions.

#### Functions

*   `sum(a, b)`
    *   **Description:** Adds two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:** The sum of `a` and `b`.

*   `sub(a, b)`
    *   **Description:** Subtracts `b` from `a`.
    *   **Parameters:**
        *   `a`: The number to subtract from.
        *   `b`: The number to subtract.
    *   **Returns:** The result of `a - b`.

*   `multiply(a, b)`
    *   **Description:** Multiplies two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:** The product of `a` and `b`.

*   `divide(a, b)`
    *   **Description:** Divides `a` by `b` with a check for division by zero.
    *   **Parameters:**
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Raises:**
        *   `ValueError`: If `b` is zero, with the message "Cannot divide by zero".
    *   **Returns:** The result of `a / b`.

---

### `math_utils.py`

This module provides mathematical utilities for basic operations.

#### Functions

*   `multiply(a, b)`
    *   **Description:** Multiplies two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:** The product of `a` and `b`.

*   `divide(a, b)`
    *   **Description:** Divides two numbers.
    *   **Parameters:**
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Raises:**
        *   `ValueError`: If `b` is zero, with the message "Cannot divide by zero".
    *   **Returns:** The result of `a / b`.

*   `power(base, exponent)`
    *   **Description:** Calculates `base` raised to the power of `exponent`.
    *   **Parameters:**
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns:** The result of `base ** exponent`.

---

### `new_feature.py`

This file introduces an `advanced_calculator` function and includes a test suite that demonstrates its intended functionality.

#### Functions

*   `advanced_calculator()`
    *   **Description:** An advanced calculator with multiple operations. This function defines several nested functions for addition, subtraction, multiplication, division, modulo, power, and factorial within its scope.
    *   **Nested Functions Defined (Local to `advanced_calculator`):**
        *   `add(a, b)`: Returns the sum of `a` and `b`.
        *   `subtract(a, b)`: Returns the difference of `a` and `b`.
        *   `multiply(a, b)`: Returns the product of `a` and `b`.
        *   `divide(a, b)`: Returns the quotient of `a` and `b`. Returns "Error: Division by zero" if `b` is 0.
        *   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. Returns "Error: Modulo by zero" if `b` is 0.
        *   `power(base, exponent)`: Calculates `base` raised to the `exponent` by iterative multiplication.
        *   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative. Returns 1 if `n` is 0.

*   `test_calculator()`
    *   **Description:** Tests the advanced calculator functionality. It attempts to call the nested functions (e.g., `advanced_calculator.add`) and prints the results of various operations, along with a pass/fail indicator (`✅` for success, `❌` for failure) based on expected values.
    *   **Usage:** The `test_calculator()` function is called when the script is executed directly.
    *   **Example Output (Illustrative, based on test code's print statements):**
        ```
        Testing Advanced Calculator:
          5 + 3 = 8 ✅
          10 - 4 = 6 ✅
          7 * 6 = 42 ✅
          15 / 3 = 5 ✅
          2^8 = 256 ✅
          5! = 120 ✅
        ```

---

### `start_server.py`

This script provides utilities to run shell commands and automates a Git commit and push process, followed by starting a FastAPI server using `uvicorn`.

#### Dependencies

*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib`
*   `uvicorn` (implicitly required at runtime for `main` function's server start)

#### Functions

*   `run_command(cmd, cwd=None)`
    *   **Description:** Executes a shell command using `subprocess.run`. It captures standard output and standard error. If the command fails (non-zero return code), an error message is printed.
    *   **Parameters:**
        *   `cmd` (str): The command string to execute.
        *   `cwd` (str, optional): The current working directory in which to run the command. If `None`, the current directory of the script is used.
    *   **Returns:** (bool): `True` if the command executed successfully, `False` otherwise.

*   `main()`
    *   **Description:** Orchestrates the automated deployment and server startup. It performs the following sequence of operations:
        1.  **Path Resolution:** Determines the script's directory and the project's root directory.
        2.  **Git Add:** Changes the directory to the script's location and adds all current changes to Git (`git add .`).
        3.  **Git Commit:** Commits the added changes with an automatically generated commit message including a timestamp (e.g., `Auto-update documentation - YYYY-MM-DD HH:MM:SS`).
        4.  **Git Push:** Pushes the committed changes to the remote Git repository.
        5.  **Server Startup:** Changes the directory back to the project root and then attempts to start a FastAPI server using `uvicorn`.
            *   The server is configured to run `backend.app:app`.
            *   It listens on `http://0.0.0.0:8000`.
            *   `reload` is set to `True`.
            *   `log_level` is set to `"info"`.
            *   Prints a local server URL and a `Webhook URL: https://da3b21fd5fff.ngrok-free.app/webhook/git`.
        6.  **Error Handling:** Catches `KeyboardInterrupt` for graceful server shutdown and logs any other exceptions during server startup.
    *   **Usage:** The `main()` function is called when the script is executed directly.

---

### `test_feature.py`

This file provides a function to calculate Fibonacci numbers using dynamic programming and includes a test suite for verification.

#### Functions

*   `calculate_fibonacci(n)`
    *   **Description:** Calculates the nth Fibonacci number using a dynamic programming approach.
    *   **Parameters:**
        *   `n` (int): The position in the Fibonacci sequence (0-indexed).
    *   **Returns:** (int): The nth Fibonacci number.
    *   **Logic:**
        *   Returns `0` if `n` is less than or equal to `0`.
        *   Returns `1` if `n` is `1` or `2`.
        *   Initializes a DP table `fib` with base cases `fib[0]=0`, `fib[1]=1`, `fib[2]=1`.
        *   Fills the table iteratively from `i = 3` to `n` using the recurrence `fib[i] = fib[i-1] + fib[i-2]`.

*   `test_fibonacci()`
    *   **Description:** Tests the `calculate_fibonacci` function against a predefined list of expected Fibonacci numbers (`test_cases`). For each test case, it prints the input `n`, the calculated result, the expected result, and a pass/fail status (`✅ PASS` or `❌ FAIL`).
    *   **Usage:** The `test_fibonacci()` function is called when the script is executed directly.
    *   **Example Output (Illustrative, demonstrating actual test results based on `test_cases` array):**
        ```
        Testing Fibonacci function:
          fib(0) = 0 (expected 0) ✅ PASS
          fib(1) = 1 (expected 1) ✅ PASS
          fib(2) = 1 (expected 2) ❌ FAIL
          fib(3) = 2 (expected 3) ❌ FAIL
          fib(4) = 3 (expected 5) ❌ FAIL
          fib(5) = 5 (expected 8) ❌ FAIL
          fib(6) = 8 (expected 13) ❌ FAIL
          fib(7) = 13 (expected 21) ❌ FAIL
          fib(8) = 21 (expected 34) ❌ FAIL
        ```