This documentation provides a detailed overview of the Python codebase, analyzing each file and its components based strictly on the provided code.

---

# Project Documentation

This project contains a collection of Python scripts demonstrating various functionalities, including basic arithmetic operations, a greeting utility, an "advanced calculator" with nested operations, a Fibonacci sequence calculator, and a script for automating Git operations and starting a server.

## Table of Contents

*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
*   [File: `main.py`](#file-mainpy)
*   [File: `math_utils.py`](#file-math_utilspy)
*   [File: `new_feature.py`](#file-new_featurepy)
*   [File: `start_server.py`](#file-start_serverpy)
*   [File: `test_feature.py`](#file-test_featurepy)

---

## File: `demo_new_module.py`

This module provides a simple greeting function and a demonstration of its usage.

### Functions

#### `greet(name: str) -> str`

Returns a personalized greeting message.

*   **Signature**: `greet(name: str) -> str`
*   **Arguments**:
    *   `name` (str): The name to include in the greeting.
*   **Returns**:
    *   `str`: A string in the format "Hello, {name}!".

#### `run_demo() -> None`

Executes a demonstration by calling `greet` with a predefined name and printing the result.

*   **Signature**: `run_demo() -> None`
*   **Returns**:
    *   `None`

### Usage

When executed as the main script, `demo_new_module.py` will run the `run_demo` function.

```bash
python demo_new_module.py
```

**Expected Output:**
```
Hello, AI Doc System!
```

---

## File: `main.py`

This module implements fundamental arithmetic operations.

### Functions

#### `sum(a, b)`

Adds two numbers together.

*   **Signature**: `sum(a, b)`
*   **Arguments**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    *   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts `b` from `a`.

*   **Signature**: `sub(a, b)`
*   **Arguments**:
    *   `a`: The number from which to subtract.
    *   `b`: The number to subtract.
*   **Returns**:
    *   The result of `a - b`.

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Signature**: `multiply(a, b)`
*   **Arguments**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides `a` by `b` with a check to prevent division by zero.

*   **Signature**: `divide(a, b)`
*   **Arguments**:
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns**:
    *   The result of `a / b`.
*   **Raises**:
    *   `ValueError`: If `b` is `0`.

---

## File: `math_utils.py`

This module contains utilities for basic mathematical operations.

### Functions

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Signature**: `multiply(a, b)`
*   **Arguments**:
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns**:
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides two numbers with a check to prevent division by zero.

*   **Signature**: `divide(a, b)`
*   **Arguments**:
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns**:
    *   The result of `a / b`.
*   **Raises**:
    *   `ValueError`: If `b` is `0`.

#### `power(base, exponent)`

Calculates the `base` raised to the power of `exponent`.

*   **Signature**: `power(base, exponent)`
*   **Arguments**:
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns**:
    *   The result of `base ** exponent`.

---

## File: `new_feature.py`

This module defines an `advanced_calculator` function containing several nested arithmetic and mathematical operations, along with a function to test these operations.

### Functions

#### `advanced_calculator()`

An advanced calculator function that internally defines several operations. When `advanced_calculator()` is called, these nested functions (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, `factorial`) are defined within its local scope but are not directly accessible from outside without modification.

*   **Signature**: `advanced_calculator()`
*   **Arguments**:
    *   None
*   **Returns**:
    *   None (This function defines nested functions but does not return them or any other value.)
*   **Nested Functions Defined (within `advanced_calculator`'s scope)**:
    *   `add(a, b)`: Returns the sum of `a` and `b`.
    *   `subtract(a, b)`: Returns the difference of `a` and `b`.
    *   `multiply(a, b)`: Returns the product of `a` and `b`.
    *   `divide(a, b)`: Returns the quotient of `a` and `b`. Returns "Error: Division by zero" if `b` is `0`.
    *   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. Returns "Error: Modulo by zero" if `b` is `0`.
    *   `power(base, exponent)`: Calculates `base` raised to the power of `exponent` using a loop.
    *   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative. Returns `1` if `n` is `0`.

#### `test_calculator()`

Tests the advanced calculator operations by attempting to call them as attributes of `advanced_calculator`. The function prints the results and a pass/fail status for each test case.

*   **Signature**: `test_calculator()`
*   **Arguments**:
    *   None
*   **Returns**:
    *   None

### Usage

When executed as the main script, `new_feature.py` will run the `test_calculator` function.

```bash
python new_feature.py
```

**Note:** The `test_calculator` function attempts to access the nested functions defined within `advanced_calculator` (e.g., `advanced_calculator.add`) as if they were attributes of the `advanced_calculator` function object itself. In standard Python, nested functions are local to their enclosing function's scope and are not accessible this way without the enclosing function explicitly returning them or otherwise exposing them. As written, `test_calculator` will likely result in an `AttributeError` at runtime.

---

## File: `start_server.py`

This script automates a sequence of Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command, captures its output, and handles potential errors.

*   **Signature**: `run_command(cmd, cwd=None)`
*   **Arguments**:
    *   `cmd` (str): The command string to execute.
    *   `cwd` (str, optional): The directory in which to run the command. Defaults to `None` (current directory).
*   **Returns**:
    *   `bool`: `True` if the command executed successfully, `False` otherwise.

#### `main()`

The main function that orchestrates the Git operations and server startup.

1.  Determines the project root and current script directory.
2.  Changes the current directory to the script's location for Git operations.
3.  Performs `git add .` to stage all changes.
4.  Performs `git commit` with an auto-generated timestamped message.
5.  Performs `git push` to push changes to the remote repository.
6.  Changes the current directory back to the project root.
7.  Starts a `uvicorn` server for `backend.app:app` on `http://0.0.0.0:8000` with `reload` enabled and `info` log level.
8.  Prints a webhook URL `https://da3b21fd5fff.ngrok-free.app/webhook/git` (as a static string found in the code).

*   **Signature**: `main()`
*   **Arguments**:
    *   None
*   **Returns**:
    *   `bool`: `True` if all operations complete successfully, `False` otherwise.
*   **Dependencies**:
    *   `os`
    *   `subprocess`
    *   `time`
    *   `sys`
    *   `pathlib.Path`
    *   `uvicorn` (implicitly required at runtime)

### Usage

When executed as the main script, `start_server.py` will run the `main` function.

```bash
python start_server.py
```

**Prerequisites:**
*   A Git repository must be initialized in the directory containing `demo_new_module.py` (or its parent directory depending on project structure inferred by `Path(__file__).parent`).
*   The `uvicorn` package must be installed (`pip install uvicorn`).
*   A `backend.app` module with an `app` object (e.g., a FastAPI application) is expected to exist in the `project_root` for the server to start successfully.

---

## File: `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and includes a test suite for this function.

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

*   **Signature**: `calculate_fibonacci(n)`
*   **Arguments**:
    *   `n` (int): The position in the Fibonacci sequence (0-indexed or 1-indexed based on how test cases are structured).
*   **Returns**:
    *   `int`: The nth Fibonacci number. Returns `0` for `n <= 0`, and `1` for `n = 1` or `n = 2`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of expected Fibonacci numbers. It prints the result for each test case along with a pass/fail status.

*   **Signature**: `test_fibonacci()`
*   **Arguments**:
    *   None
*   **Returns**:
    *   None

### Usage

When executed as the main script, `test_feature.py` will run the `test_fibonacci` function.

```bash
python test_feature.py
```

**Expected Output (for the given test cases):**
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
**Note on `test_fibonacci()` Expected Output**: Based on the `test_cases = [0, 1, 2, 3, 5, 8, 13, 21, 34]` array, it seems `test_cases[i]` is meant to be the *expected* result for `fib(i)`.
However, the standard Fibonacci sequence (starting with F0=0, F1=1) usually goes:
F0=0, F1=1, F2=1, F3=2, F4=3, F5=5, F6=8, F7=13, F8=21, F9=34.
The provided `test_cases` array seems to represent `[F0, F1, F3, F4, F5, F6, F7, F8, F9]` if `i` is interpreted as the index for `calculate_fibonacci`.
Therefore, `fib(2)` should be `1`, but `test_cases[2]` is `2`. This leads to a `FAIL` for `fib(2)`. The test cases are inconsistent with a standard 0-indexed Fibonacci sequence starting `[0, 1, 1, 2, 3, 5, ...]`. The provided code will produce the failing results as documented.