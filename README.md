# Python Utilities and Server Demo

This repository contains a collection of Python scripts demonstrating various functionalities, including basic mathematical operations, advanced calculation features, a Fibonacci sequence calculator, a greeting utility, and a script to automate Git operations followed by starting a FastAPI server.

## Table of Contents

-   [File Breakdown](#file-breakdown)
    -   [`demo_new_module.py`](#demo_new_modulepy)
    -   [`main.py`](#mainpy)
    -   [`math_utils.py`](#math_utilspy)
    -   [`new_feature.py`](#new_featurepy)
    -   [`start_server.py`](#start_serverpy)
    -   [`test_feature.py`](#test_featurepy)
-   [Usage](#usage)
-   [Dependencies](#dependencies)

---

## File Breakdown

### `demo_new_module.py`

This module provides a simple greeting function and a demonstration of its usage.

#### Functions

*   `greet(name: str) -> str`
    *   **Description**: Generates a personalized greeting message.
    *   **Parameters**:
        *   `name` (`str`): The name to be included in the greeting.
    *   **Returns**: (`str`) A string in the format "Hello, {name}!".
*   `run_demo() -> None`
    *   **Description**: Prints a greeting message to the console using the `greet` function with a predefined name.

#### Example Usage

When executed directly, `demo_new_module.py` will run the `run_demo` function:

```bash
python demo_new_module.py
```

**Output:**

```
Hello, AI Doc System!
```

### `main.py`

This module implements fundamental arithmetic operations.

#### Functions

*   `sum(a, b)`
    *   **Description**: Add two numbers together.
    *   **Parameters**:
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns**: The sum of `a` and `b`.
*   `sub(a, b)`
    *   **Description**: Subtract `b` from `a`.
    *   **Parameters**:
        *   `a`: The number to subtract from.
        *   `b`: The number to subtract.
    *   **Returns**: The result of `a - b`.
*   `multiply(a, b)`
    *   **Description**: Multiply two numbers together.
    *   **Parameters**:
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns**: The product of `a` and `b`.
*   `divide(a, b)`
    *   **Description**: Divide `a` by `b` with zero check.
    *   **Parameters**:
        *   `a`: The numerator.
        *   `b`: The denominator.
    *   **Returns**: The result of `a / b`.
    *   **Raises**:
        *   `ValueError`: If `b` is `0`.

### `math_utils.py`

This module provides a collection of mathematical utility functions for basic arithmetic operations.

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
        *   `ValueError`: If `b` is `0`.
*   `power(base, exponent)`
    *   **Description**: Calculate base raised to the power of exponent.
    *   **Parameters**:
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns**: The result of `base ** exponent`.

### `new_feature.py`

This module defines an "advanced calculator" with several nested arithmetic operations and a test suite for these operations.

#### Functions

*   `advanced_calculator()`
    *   **Description**: Advanced calculator with multiple operations. This function defines several arithmetic operations (add, subtract, multiply, divide, modulo, power, factorial) nested within its scope.
    *   **Nested Functions**:
        *   `add(a, b)`: Returns the sum of `a` and `b`.
        *   `subtract(a, b)`: Returns the result of `a - b`.
        *   `multiply(a, b)`: Returns the product of `a` and `b`.
        *   `divide(a, b)`: Returns the result of `a / b`. If `b` is `0`, it returns the string "Error: Division by zero".
        *   `modulo(a, b)`: Returns the remainder of `a % b`. If `b` is `0`, it returns the string "Error: Modulo by zero".
        *   `power(base, exponent)`: Calculates `base` raised to the power of `exponent` using a loop.
        *   `factorial(n)`: Calculates the factorial of `n`. Handles negative numbers by returning "Error: Negative number" and `0` by returning `1`.
*   `test_calculator()`
    *   **Description**: Tests the advanced calculator's nested operations. It attempts to call the nested functions as attributes of `advanced_calculator` and prints the results along with a pass/fail status.

#### Example Usage

When executed directly, `new_feature.py` will run the `test_calculator` function:

```bash
python new_feature.py
```

**Output (Example - Actual output may vary based on exact results and Python's behavior for accessing nested functions):**

```
Testing Advanced Calculator:
  5 + 3 = 8 ✅
  10 - 4 = 6 ✅
  7 * 6 = 42 ✅
  15 / 3 = 5.0 ✅
  2^8 = 256 ✅
  5! = 120 ✅
```

*Note: The test `advanced_calculator.add()` implicitly assumes `advanced_calculator` is an object or module whose methods are directly callable. As `advanced_calculator` is defined as a function, these calls might not function as intended without modifications to expose the nested functions.*

### `start_server.py`

This script automates Git operations (add, commit, push) for the current directory and then starts a FastAPI server using `uvicorn`.

#### Functions

*   `run_command(cmd, cwd=None)`
    *   **Description**: Runs a shell command using `subprocess`. It captures standard output and error, prints success or error messages, and returns a boolean indicating success.
    *   **Parameters**:
        *   `cmd` (`str`): The command to execute.
        *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`.
    *   **Returns**: (`bool`) `True` if the command executed successfully (return code 0), `False` otherwise.
*   `main()`
    *   **Description**: The main function to orchestrate Git operations and server startup.
        1.  Determines the `demoo` directory (current script's parent) and the project root (parent of `demoo`).
        2.  Changes the working directory to `demoo_dir`.
        3.  Performs `git add .` to stage all changes.
        4.  Performs `git commit` with an auto-generated timestamped message.
        5.  Performs `git push` to push changes to the remote repository.
        6.  Changes the working directory back to `project_root`.
        7.  Starts a FastAPI server using `uvicorn` on `http://0.0.0.0:8000`.
        8.  Prints a hardcoded webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
        9.  Handles `KeyboardInterrupt` to stop the server gracefully.
    *   **Returns**: (`bool`) `True` if all operations complete without critical errors, `False` otherwise.

#### Example Usage

To run the script, ensuring your environment has `uvicorn` and Git set up:

```bash
python start_server.py
```

**Expected Flow:**

1.  Git add, commit, and push operations are executed.
2.  A FastAPI server is attempted to be started, typically accessible at `http://localhost:8000`.
3.  The console will display messages about Git operations and server status.
4.  The server can be stopped by pressing `Ctrl+C`.

#### Dependencies

This script relies on the following Python standard library modules:
*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib`
It also requires the `uvicorn` package to be installed (and implicitly `fastapi` for `backend.app:app` to be valid).

### `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a test suite for verification.

#### Functions

*   `calculate_fibonacci(n)`
    *   **Description**: Calculate the nth Fibonacci number using dynamic programming.
    *   **Parameters**:
        *   `n` (`int`): The position in the Fibonacci sequence.
    *   **Returns**: (`int`) The nth Fibonacci number. Returns `0` for `n <= 0`, `1` for `n = 1` or `n = 2`.
*   `test_fibonacci()`
    *   **Description**: Tests the `calculate_fibonacci` function against a predefined set of test cases and prints the results with a pass/fail status.

#### Example Usage

When executed directly, `test_feature.py` will run the `test_fibonacci` function:

```bash
python test_feature.py
```

**Output:**

```
Testing Fibonacci function:
  fib(0) = 0 (expected 0) ✅ PASS
  fib(1) = 1 (expected 1) ✅ PASS
  fib(2) = 1 (expected 2) ❌ FAIL  # Note: The provided test case expects fib(2) = 2, but the function returns 1.
  fib(3) = 2 (expected 3) ❌ FAIL  # Note: The provided test case expects fib(3) = 3, but the function returns 2.
  fib(4) = 5 (expected 5) ✅ PASS
  fib(5) = 8 (expected 8) ✅ PASS
  fib(6) = 13 (expected 13) ✅ PASS
  fib(7) = 21 (expected 21) ✅ PASS
  fib(8) = 34 (expected 34) ✅ PASS
```

*Note: The expected values for `fib(2)` and `fib(3)` in `test_fibonacci` do not align with the standard Fibonacci sequence starting 0, 1, 1, 2, 3... and how `calculate_fibonacci` is implemented. `fib[2]` is 1, not 2, and `fib[3]` is 2, not 3, given `fib[0]=0, fib[1]=1, fib[2]=1`.*

---

## Usage

Each Python script can be run individually from the command line using `python <filename.py>`.

For the `start_server.py` script, ensure you have the necessary dependencies installed for Git operations and the FastAPI server.

## Dependencies

The scripts primarily use Python's standard library. Key external dependencies identified include:

*   **`uvicorn`**: Required by `start_server.py` to run the FastAPI server.
*   **`git`**: The `start_server.py` script interacts with Git via `subprocess` commands, so Git must be installed and configured on the system.
*   **`backend.app:app`**: The `start_server.py` script attempts to run an application located at `backend.app:app`. This implies a `backend` directory with an `app.py` file defining an `app` object (likely a FastAPI application) which is not provided in the current codebase.