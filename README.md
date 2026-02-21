# Project Documentation

This document provides a comprehensive overview of the Python modules present in this project, detailing their functionalities, usage, and internal logic based strictly on the provided source code.

---

## Files

### `demo_new_module.py`

This module contains a simple greeting function and a demonstration of its use.

#### Functions

*   **`greet(name: str) -> str`**
    *   **Description:** Generates a personalized greeting message.
    *   **Parameters:**
        *   `name` (`str`): The name to be included in the greeting.
    *   **Returns:**
        *   `str`: A string in the format "Hello, {name}!".

*   **`run_demo() -> None`**
    *   **Description:** Calls the `greet` function with a specific name ("AI Doc System") and prints the returned greeting to the console.
    *   **Parameters:** None
    *   **Returns:** None

#### Usage

When executed as the main program, `demo_new_module.py` calls the `run_demo` function.

```bash
python demo_new_module.py
```

This will print:
```
Hello, AI Doc System!
```

---

### `main.py`

This module provides fundamental arithmetic operations.

#### Functions

*   **`sum(a, b)`**
    *   **Description:** Add two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The sum of `a` and `b`.

*   **`sub(a, b)`**
    *   **Description:** Subtract b from a.
    *   **Parameters:**
        *   `a`: The number to subtract from.
        *   `b`: The number to subtract.
    *   **Returns:**
        *   The result of `a - b`.

*   **`multiply(a, b)`**
    *   **Description:** Multiply two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The product of `a` and `b`.

*   **`divide(a, b)`**
    *   **Description:** Divide a by b with zero check.
    *   **Parameters:**
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Returns:**
        *   The result of `a / b`.
    *   **Raises:**
        *   `ValueError`: If `b` is `0`.

#### Notes

The file contains a comment: `# Test with Gemini AI documentation - 2026-01-30`. This is a code comment and does not affect runtime behavior or functionality.

---

### `math_utils.py`

This module provides various mathematical utility functions for basic operations.

#### Functions

*   **`multiply(a, b)`**
    *   **Description:** Multiply two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The product of `a` and `b`.

*   **`divide(a, b)`**
    *   **Description:** Divide two numbers.
    *   **Parameters:**
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Returns:**
        *   The result of `a / b`.
    *   **Raises:**
        *   `ValueError`: If `b` is `0`.

*   **`power(base, exponent)`**
    *   **Description:** Calculate base raised to the power of exponent.
    *   **Parameters:**
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns:**
        *   The result of `base ** exponent`.

---

### `new_feature.py`

This module defines an `advanced_calculator` function that encapsulates several arithmetic and mathematical operations as nested functions. It also includes a `test_calculator` function to demonstrate the intended use of these operations.

#### Functions

*   **`advanced_calculator()`**
    *   **Description:** Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, and division.
    *   **Parameters:** None
    *   **Returns:** None
    *   **Internal Functions:** This function defines the following nested functions, which are scoped within `advanced_calculator` and are not directly accessible from outside its definition context:
        *   **`add(a, b)`**: Returns `a + b`.
        *   **`subtract(a, b)`**: Returns `a - b`.
        *   **`multiply(a, b)`**: Returns `a * b`.
        *   **`divide(a, b)`**: Returns `a / b`. If `b` is `0`, it returns the string `"Error: Division by zero"`.
        *   **`modulo(a, b)`**: Returns `a % b`. If `b` is `0`, it returns the string `"Error: Modulo by zero"`.
        *   **`power(base, exponent)`**: Calculates `base` raised to the `exponent` using an iterative loop.
        *   **`factorial(n)`**: Calculates the factorial of `n`. If `n` is negative, it returns the string `"Error: Negative number"`. If `n` is `0`, it returns `1`.

*   **`test_calculator()`**
    *   **Description:** Attempts to test the `advanced_calculator` operations by calling them as `advanced_calculator.<operation_name>(...)` and printing the results along with a `✅` (PASS) or `❌` (FAIL) indicator based on hardcoded expected values.
    *   **Parameters:** None
    *   **Returns:** None

#### Usage

When executed as the main program, `new_feature.py` calls `test_calculator()`.

```bash
python new_feature.py
```

This will print a series of test results for addition, subtraction, multiplication, division, power, and factorial. Note that the tests attempt to call the nested functions from `advanced_calculator` directly as attributes, which will lead to runtime errors as written because `advanced_calculator` is a function that doesn't return an object with these methods. The output shown by the code, if it were to run without the `AttributeError`, would be:

```
Testing Advanced Calculator:
  5 + 3 = 8 ✅
  10 - 4 = 6 ✅
  7 * 6 = 42 ✅
  15 / 3 = 5.0 ✅
  2^8 = 256 ✅
  5! = 120 ✅
```

---

### `start_server.py`

This script is designed to automate a Git commit and push sequence, followed by starting a FastAPI server using `uvicorn`.

#### Functions

*   **`run_command(cmd, cwd=None)`**
    *   **Description:** Executes a shell command using `subprocess`. It captures standard output and standard error, prints them, and checks the return code.
    *   **Parameters:**
        *   `cmd`: The command string to execute.
        *   `cwd` (`str`, optional): The working directory in which to run the command. Defaults to `None` (current directory).
    *   **Returns:**
        *   `True`: If the command executed successfully (return code 0).
        *   `False`: If the command failed or an exception occurred.

*   **`main()`**
    *   **Description:** Main function to start the server with a single Git push.
        1.  Determines the `demoo` directory (current script's parent) and the `project_root` (parent of `demoo_dir`).
        2.  Changes the current working directory to `demoo_dir`.
        3.  Performs Git operations:
            *   `git add .`: Stages all changes in the `demoo_dir`.
            *   `git commit -m "Auto-update documentation - <timestamp>"`: Commits the staged changes with an auto-generated timestamped message. Prints "No changes to commit or commit failed" if the commit command fails.
            *   `git push`: Pushes the committed changes to the remote repository.
        4.  Changes the current working directory back to `project_root`.
        5.  Attempts to start a FastAPI server:
            *   Imports `uvicorn`.
            *   Starts `uvicorn` to run `backend.app:app` on host `0.0.0.0` and port `8000`.
            *   Enables `reload` mode and sets `log_level` to `"info"`.
            *   Prints instructions for stopping the server and a hardcoded webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
            *   Handles `KeyboardInterrupt` to gracefully stop the server.
            *   Catches other exceptions during server startup.
    *   **Parameters:** None
    *   **Returns:**
        *   `True`: If all operations (Git push and server start) were attempted without fatal errors.
        *   `False`: If any Git operation or server startup failed.

#### Usage

When executed as the main program, `start_server.py` calls the `main` function.

```bash
python start_server.py
```

This script is designed for environments where `uvicorn` and Git are configured. It will first attempt to add, commit, and push all changes in the `demoo` directory to a Git repository, then it will launch a `uvicorn` server.

#### Dependencies

*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib.Path`
*   `uvicorn` (implicitly, as it attempts to import it)

---

### `test_feature.py`

This module implements a function to calculate Fibonacci numbers using dynamic programming and includes a test suite for it.

#### Functions

*   **`calculate_fibonacci(n)`**
    *   **Description:** Calculate the nth Fibonacci number using dynamic programming.
    *   **Parameters:**
        *   `n` (`int`): The position in the Fibonacci sequence.
    *   **Returns:**
        *   `int`: The nth Fibonacci number.
    *   **Logic:**
        *   Returns `0` for `n <= 0`.
        *   Returns `1` for `n == 1` or `n == 2`.
        *   For `n > 2`, it initializes a DP table `fib` of size `n + 1`, sets `fib[0]=0`, `fib[1]=1`, `fib[2]=1`.
        *   It then iteratively fills the table from `i = 3` to `n` using the recurrence `fib[i] = fib[i-1] + fib[i-2]`.
        *   Finally, it returns `fib[n]`.

*   **`test_fibonacci()`**
    *   **Description:** Tests the `calculate_fibonacci` function against a predefined list of Fibonacci numbers. It prints the input `n`, the calculated result, the expected value, and a `✅ PASS` or `❌ FAIL` status.
    *   **Parameters:** None
    *   **Returns:** None

#### Usage

When executed as the main program, `test_feature.py` calls `test_fibonacci()`.

```bash
python test_feature.py
```

This will print the results of the Fibonacci function tests:
```
Testing Fibonacci function:
  fib(0) = 0 (expected 0) ✅ PASS
  fib(1) = 1 (expected 1) ✅ PASS
  fib(2) = 1 (expected 1) ✅ PASS
  fib(3) = 2 (expected 3) ❌ FAIL
  fib(4) = 3 (expected 5) ❌ FAIL
  fib(5) = 5 (expected 8) ❌ FAIL
  fib(6) = 8 (expected 13) ❌ FAIL
  fib(7) = 13 (expected 21) ❌ FAIL
  fib(8) = 21 (expected 34) ❌ FAIL
```
*(Note: The `test_cases` list in `test_fibonacci` starts with `[0, 1, 2, 3, 5, 8, 13, 21, 34]` which are Fibonacci numbers for indices 0, 1, 2, 3, 4, 5, 6, 7, 8 respectively. The test loop `for i, expected in enumerate(test_cases)` will pass `i` (0 to 8) as `n` to `calculate_fibonacci`, and compare the result against `expected`. The provided `test_cases` are actually `fib(0)` through `fib(8)`, not `fib(0)` through `fib(8)` but with `test_cases[3]=3` where `fib(3)=2`, etc. This means some tests are expected to fail based on the `test_cases` values versus the `calculate_fibonacci` output.)*