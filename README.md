This document provides a comprehensive overview of the provided Python codebase, detailing the purpose, functionalities, and usage of each file and its constituent functions. The documentation strictly adheres to the provided code, without inventing or assuming features not explicitly present.

---

# Project Overview

This repository contains a collection of Python scripts demonstrating various functionalities, including basic mathematical operations, string manipulation, an advanced calculator, Fibonacci sequence calculation, and a script for automating Git operations and starting a server.

---

## Table of Contents

*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
    *   [`greet(name: str)`](#greetname-str)
    *   [`run_demo()`](#run_demo)
*   [File: `main.py`](#file-mainpy)
    *   [`sum(a, b)`](#suma-b)
    *   [`sub(a, b)`](#suba-b)
    *   [`multiply(a, b)`](#multiplya-b)
    *   [`divide(a, b)`](#dividea-b)
    *   [`calculate_tax(income: float)`](#calculate_taxincome-float)
    *   [`calculate_discount(price: float, discount_percent: float)`](#calculate_discountprice-float-discount_percent-float)
    *   [`average(a: float, b: float)`](#averagea-float-b-float)
    *   [`max_of_two(a: float, b: float)`](#max_of_twoa-float-b-float)
    *   [`is_palindrome(text: str)`](#is_palindrometext-str)
    *   [`fibonacci(n: int)`](#fibonaccin-int)
    *   [`factorial(n: int)`](#factorialn-int)
*   [File: `math_utils.py`](#file-math_utilspy)
    *   [`multiply(a, b)`](#multiplya-b-1)
    *   [`divide(a, b)`](#dividea-b-1)
    *   [`power(base, exponent)`](#powerbase-exponent)
*   [File: `new_feature.py`](#file-new_featurepy)
    *   [`advanced_calculator()`](#advanced_calculator)
    *   [`test_calculator()`](#test_calculator)
*   [File: `start_server.py`](#file-start_serverpy)
    *   [`run_command(cmd, cwd=None)`](#run_commandcmd-cwdnone)
    *   [`main()`](#main)
*   [File: `test_feature.py`](#file-test_featurepy)
    *   [`calculate_fibonacci(n)`](#calculate_fibonaccin)
    *   [`test_fibonacci()`](#test_fibonacci)
*   [Dependencies](#dependencies)
*   [How to Run](#how-to-run)

---

## File: `demo_new_module.py`

This file demonstrates a simple greeting function and how to run a demo of it.

### `greet(name: str) -> str`

Returns a personalized greeting message.

**Parameters:**

*   `name` (str): The name to greet.

**Returns:**

*   `str`: A greeting string, formatted as "Hello, `name`!".

**Example:**

```python
greet("AI Doc System") # Returns "Hello, AI Doc System!"
```

### `run_demo() -> None`

Prints a greeting message by calling the `greet` function with the specific input "AI Doc System".

**Example:**

When `demo_new_module.py` is executed directly, it will perform the `run_demo` action:

```bash
python demo_new_module.py
# Output: Hello, AI Doc System!
```

---

## File: `main.py`

This file contains a collection of general-purpose utility functions for basic arithmetic, financial calculations, string manipulation, and sequence generation.

### `sum(a, b)`

Adds two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The sum of `a` and `b`.

### `sub(a, b)`

Subtracts `b` from `a`.

**Parameters:**

*   `a`: The minuend.
*   `b`: The subtrahend.

**Returns:**

*   The difference of `a` and `b`.

### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

### `divide(a, b)`

Divides `a` by `b` with a check for division by zero.

**Parameters:**

*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**

*   The quotient of `a` divided by `b`.

**Raises:**

*   `ValueError`: If `b` is zero, with the message "Cannot divide by zero".

### `calculate_tax(income: float) -> float`

Calculates tax on a given income at a fixed 10% rate.

**Parameters:**

*   `income` (float): The income amount.

**Returns:**

*   `float`: The calculated tax amount (10% of income).

### `calculate_discount(price: float, discount_percent: float) -> float`

Calculates the discount amount based on a price and a discount percentage.

**Parameters:**

*   `price` (float): The original price.
*   `discount_percent` (float): The discount percentage, expected to be between 0 and 100.

**Returns:**

*   `float`: The calculated discount amount.

**Raises:**

*   `ValueError`: If `discount_percent` is less than 0 or greater than 100.

### `average(a: float, b: float) -> float`

Returns the arithmetic average of two numbers.

**Parameters:**

*   `a` (float): The first number.
*   `b` (float): The second number.

**Returns:**

*   `float`: The average of `a` and `b`.

### `max_of_two(a: float, b: float) -> float`

Returns the larger of two numbers.

**Parameters:**

*   `a` (float): The first number.
*   `b` (float): The second number.

**Returns:**

*   `float`: The larger value between `a` and `b`.

### `is_palindrome(text: str) -> bool`

Checks if a string is a palindrome. The check is case-insensitive and ignores non-alphanumeric characters.

**Parameters:**

*   `text` (str): The string to check.

**Returns:**

*   `bool`: `True` if the string is a palindrome, `False` otherwise.

**Examples:**

```python
is_palindrome("racecar")                 # Returns True
is_palindrome("hello")                   # Returns False
is_palindrome("A man a plan a canal Panama") # Returns True
```

### `fibonacci(n: int) -> int`

Calculates the nth Fibonacci number using an iterative approach. The sequence is 0-indexed (e.g., `fibonacci(0)` is 0, `fibonacci(1)` is 1).

**Parameters:**

*   `n` (int): The position in the Fibonacci sequence (0-indexed).

**Returns:**

*   `int`: The nth Fibonacci number.

**Raises:**

*   `ValueError`: If `n` is negative, with the message "Fibonacci number is not defined for negative numbers".

**Examples:**

```python
fibonacci(0)  # Returns 0
fibonacci(1)  # Returns 1
fibonacci(10) # Returns 55
```

### `factorial(n: int) -> int`

Calculates the factorial of a non-negative integer.

**Parameters:**

*   `n` (int): A non-negative integer.

**Returns:**

*   `int`: The factorial of `n`.

**Raises:**

*   `ValueError`: If `n` is negative, with the message "Factorial is not defined for negative numbers".

**Examples:**

```python
factorial(0)   # Returns 1
factorial(5)   # Returns 120
factorial(10)  # Returns 3628800
```

---

## File: `math_utils.py`

This module provides utility functions for basic mathematical operations.

### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

### `divide(a, b)`

Divides two numbers.

**Parameters:**

*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**

*   The quotient of `a` divided by `b`.

**Raises:**

*   `ValueError`: If `b` is zero, with the message "Cannot divide by zero".

### `power(base, exponent)`

Calculates `base` raised to the power of `exponent`.

**Parameters:**

*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**

*   The result of `base` raised to `exponent`.

---

## File: `new_feature.py`

This file defines an `advanced_calculator` function, which encapsulates several arithmetic and mathematical operations, and includes a `test_calculator` function to demonstrate their usage.

### `advanced_calculator()`

This function is intended to define an advanced calculator with multiple operations. It internally defines the following operations as nested functions:

*   **`add(a, b)`**: Returns the sum of `a` and `b`.
*   **`subtract(a, b)`**: Returns the difference of `a` and `b`.
*   **`multiply(a, b)`**: Returns the product of `a` and `b`.
*   **`divide(a, b)`**: Returns the quotient of `a` divided by `b`. If `b` is 0, it returns the string "Error: Division by zero".
*   **`modulo(a, b)`**: Returns the remainder of `a` divided by `b`. If `b` is 0, it returns the string "Error: Modulo by zero".
*   **`power(base, exponent)`**: Calculates `base` raised to the `exponent` using an iterative loop.
*   **`factorial(n)`**: Calculates the factorial of `n`. If `n` is negative, it returns "Error: Negative number". If `n` is 0, it returns 1.

**Note on Accessibility:** The internal functions (e.g., `add`, `subtract`) are defined within the scope of `advanced_calculator()` and are not directly accessible from outside this function unless `advanced_calculator` were to return them or an object containing them.

### `test_calculator()`

This function tests the operations intended to be part of the `advanced_calculator`. It prints the results of several test cases for addition, subtraction, multiplication, division, power, and factorial. For each test, it indicates whether the result matches the expected value with a "✅" for pass or "❌" for fail.

**Example:**

When `new_feature.py` is executed directly:

```bash
python new_feature.py
# Output will display test results for each calculator operation.
```

**Important Note:** As written in the `new_feature.py` file, the `test_calculator()` function attempts to call the operations using dot notation, e.g., `advanced_calculator.add(5, 3)`. This syntax would typically be used if `advanced_calculator` was an object or a module exporting these functions. Given that `advanced_calculator` is defined as a regular function containing nested functions, these calls will result in an `AttributeError` at runtime because nested functions are not attributes of the outer function object itself. The documentation strictly reflects the code as provided.

---

## File: `start_server.py`

This script automates common Git operations (add, commit, push) and then proceeds to start a FastAPI server using `uvicorn`.

### `run_command(cmd, cwd=None)`

Executes a shell command using `subprocess.run`. It captures the command's output and standard error, printing them to the console. It reports success or failure and returns a boolean value.

**Parameters:**

*   `cmd` (str): The shell command string to be executed.
*   `cwd` (str, optional): The current working directory in which to run the command. If `None`, the current process's working directory is used.

**Returns:**

*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise (due to non-zero return code or an exception).

### `main()`

This is the main execution function of the script. It performs the following sequence of operations:

1.  **Directory Identification:** Determines the current script's directory (referred to as "demoo directory") and its parent directory (referred to as "project root").
2.  **Git Operations Preparation:** Changes the current working directory to the "demoo directory".
3.  **Add Changes:** Executes `git add .` to stage all local changes.
4.  **Commit Changes:** Attempts to commit the staged changes with an auto-generated, timestamped commit message "Auto-update documentation - YYYY-MM-DD HH:MM:SS". If there are no changes or the commit fails, a message is printed, but the script continues.
5.  **Push to Git:** Executes `git push` to push the committed changes to the remote repository.
6.  **Server Startup Preparation:** Changes the current working directory back to the "project root".
7.  **Start FastAPI Server:**
    *   Prints informational messages, including the server's expected address (`http://localhost:8000`) and a static webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   Starts a `uvicorn` server instance targeting the FastAPI application `"backend.app:app"`.
    *   The server is configured to listen on `0.0.0.0` at port `8000`.
    *   `reload=True` is enabled, and `log_level="info"` is set for `uvicorn`.
    *   The server runs until a `KeyboardInterrupt` (e.g., Ctrl+C) is received.

**Dependencies:**

This script imports:
*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib.Path`
It implicitly relies on `uvicorn` being installed in the environment for `uvicorn.run()` to function.

**Example:**

When `start_server.py` is executed directly:

```bash
python start_server.py
# (Outputs status for Git operations, then starts the uvicorn server,
# displaying server logs and the mentioned URLs.)
```

**Note:** For the server portion to function, a `uvicorn`-compatible FastAPI application is expected to be present at the `backend.app:app` module path relative to the "project root".

---

## File: `test_feature.py`

This file implements a function for calculating Fibonacci numbers using dynamic programming and includes a test suite for this implementation.

### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming. It handles edge cases for `n <= 0`, `n = 1`, and `n = 2` explicitly before using a DP table for `n >= 3`.

**Parameters:**

*   `n` (int): The position in the Fibonacci sequence.

**Returns:**

*   `int`: The nth Fibonacci number. Returns 0 for `n <= 0`, and 1 for `n = 1` or `n = 2`.

**Example:**

```python
calculate_fibonacci(5) # Returns 5
calculate_fibonacci(8) # Returns 21
```

### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined list of Fibonacci numbers (0, 1, 1, 2, 3, 5, 8, 13, 21, 34). It iterates through these test cases, calls `calculate_fibonacci` for the corresponding index, and prints whether each test case passed or failed.

**Example:**

When `test_feature.py` is executed directly:

```bash
python test_feature.py
# (Outputs test results for fib(0) through fib(8) with pass/fail indicators.)
```

---

## Dependencies

This project primarily uses Python 3. The following modules and libraries are explicitly imported or implied by the code provided:

*   **Python Standard Library Modules:**
    *   `os`
    *   `subprocess`
    *   `time`
    *   `sys`
    *   `pathlib`
*   **Third-party Library (implicitly used by `start_server.py`):**
    *   `uvicorn`: Required for running the web server in `start_server.py`.

To install `uvicorn`, you would typically use pip:
```bash
pip install uvicorn
```
(Note: While `start_server.py` references `backend.app:app`, implying a FastAPI application, `FastAPI` itself is not explicitly imported in any of the provided code files. Therefore, it's not listed as a direct dependency of the provided code.)

---

## How to Run

Each Python file can be executed directly using a Python interpreter.

To run individual scripts:

```bash
# Runs a simple greeting demo
python demo_new_module.py

# This file contains functions but does not have a direct execution block
# that calls its functions, so running it directly will produce no visible output.
python main.py

# This file contains functions but does not have a direct execution block
# that calls its functions, so running it directly will produce no visible output.
python math_utils.py

# Runs the test suite for the advanced calculator functions.
python new_feature.py

# Performs Git add/commit/push and then starts a uvicorn server.
# Requires 'uvicorn' to be installed and potentially a FastAPI app at 'backend.app:app'.
python start_server.py

# Runs the test suite for the Fibonacci calculation.
python test_feature.py
```