# Project Documentation

This document provides a detailed overview of the provided Python code, describing its structure, functions, and their intended usage based strictly on the code itself.

---

## `demo_new_module.py`

This module contains basic demonstration functions, primarily for greeting users.

### Functions

#### `greet(name: str) -> str`

Returns a greeting message including the provided name.

**Parameters:**

*   `name` (`str`): The name to be included in the greeting.

**Returns:**

*   `str`: A formatted greeting string.

**Example Usage (from `run_demo`):**

```python
greet("AI Doc System")
# Expected Output: "Hello, AI Doc System!"
```

#### `run_demo() -> None`

Executes a demonstration by printing a greeting message using the `greet` function.

**Parameters:**

*   None

**Returns:**

*   `None`

**Execution:**

When `demo_new_module.py` is run directly, the `run_demo()` function is called, which in turn calls `greet("AI Doc System")` and prints its result to the console.

---

## `main.py`

This module provides a collection of utility functions for basic arithmetic, financial calculations, and numerical comparisons.

### Functions

#### `sum(a, b)`

Adds two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

**Parameters:**

*   `a`: The number to subtract from.
*   `b`: The number to subtract.

**Returns:**

*   The result of `a - b`.

#### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

**Parameters:**

*   `a`: The numerator.
*   `b`: The denominator.

**Raises:**

*   `ValueError`: If `b` is `0`.

**Returns:**

*   The result of `a / b`.

#### `calculate_tax(income: float) -> float`

Calculates tax on a given income at a fixed rate of 10%.

**Parameters:**

*   `income` (`float`): The income amount.

**Returns:**

*   `float`: The calculated tax amount.

#### `calculate_discount(price: float, discount_percent: float) -> float`

Calculates the discount amount based on a price and a discount percentage.

**Parameters:**

*   `price` (`float`): The original price.
*   `discount_percent` (`float`): The discount percentage (must be between 0 and 100).

**Raises:**

*   `ValueError`: If `discount_percent` is less than 0 or greater than 100.

**Returns:**

*   `float`: The calculated discount amount.

#### `average(a: float, b: float) -> float`

Returns the average of two numbers.

**Parameters:**

*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**

*   `float`: The average of `a` and `b`.

#### `max_of_two(a: float, b: float) -> float`

Returns the larger of two numbers.

**Parameters:**

*   `a` (`float`): The first number.
*   `b` (`float`): The second number.

**Returns:**

*   `float`: The larger of `a` and `b`.

---

## `math_utils.py`

This module provides a set of basic mathematical utility functions.

### Functions

#### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), with a check for division by zero.

**Parameters:**

*   `a`: The numerator.
*   `b`: The denominator.

**Raises:**

*   `ValueError`: If `b` is `0`.

**Returns:**

*   The result of `a / b`.

#### `power(base, exponent)`

Calculates the `base` raised to the power of `exponent`.

**Parameters:**

*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**

*   The result of `base ** exponent`.

---

## `new_feature.py`

This module defines an `advanced_calculator` function that internally implements several arithmetic and mathematical operations, and a `test_calculator` function that attempts to test these operations.

### Functions

#### `advanced_calculator()`

This function, when called, defines several arithmetic and mathematical operations as local, nested functions. These nested functions are not directly accessible from outside `advanced_calculator`'s scope without explicit return or other mechanisms.

**Internal Functions Defined (not directly callable externally):**

*   `add(a, b)`: Returns the sum of `a` and `b`.
*   `subtract(a, b)`: Returns the result of `a - b`.
*   `multiply(a, b)`: Returns the product of `a` and `b`.
*   `divide(a, b)`: Returns the result of `a / b`. Returns `"Error: Division by zero"` if `b` is `0`.
*   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. Returns `"Error: Modulo by zero"` if `b` is `0`.
*   `power(base, exponent)`: Calculates `base` raised to the `exponent` using a loop.
*   `factorial(n)`: Calculates the factorial of `n`. Returns `"Error: Negative number"` if `n` is negative, and `1` if `n` is `0`.

**Parameters:**

*   None

**Returns:**

*   None (The function defines internal operations but does not return them or make them externally accessible in its current form).

#### `test_calculator()`

This function is designed to test the operations provided by the `advanced_calculator`. It attempts to call the internal functions of `advanced_calculator` (e.g., `advanced_calculator.add(5, 3)`). This access pattern would result in an `AttributeError` if executed as written, as the internal functions are not attributes of the `advanced_calculator` function object itself.

**Parameters:**

*   None

**Returns:**

*   None (Prints test results to the console).

**Execution:**

When `new_feature.py` is run directly, `test_calculator()` is called, which prints various test cases and their results, attempting to exercise the operations.

---

## `start_server.py`

This script provides utilities to run commands, manage Git operations (add, commit, push), and start a FastAPI server.

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command and captures its output. It prints success or error messages and returns `True` on success, `False` otherwise.

**Parameters:**

*   `cmd` (`str`): The command string to execute.
*   `cwd` (`str`, optional): The working directory for the command. Defaults to `None` (current directory).

**Returns:**

*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

#### `main()`

The main function orchestrates a sequence of operations:

1.  Determines the project root and current script's directory.
2.  Changes the working directory to the script's parent (`demoo_dir`).
3.  Performs Git operations:
    *   Adds all changes (`git add .`).
    *   Commits changes with an auto-generated timestamp message (`git commit -m "Auto-update documentation - YYYY-MM-DD HH:MM:SS"`).
    *   Pushes changes to the remote repository (`git push`).
4.  Changes the working directory back to the `project_root`.
5.  Starts a FastAPI server using `uvicorn` on `http://0.0.0.0:8000` with `reload=True` and `log_level="info"`. It also prints a hardcoded webhook URL: `https://da3b21fd5fff.ngrok-free.app/webhook/git`.
6.  Handles `KeyboardInterrupt` to gracefully stop the server.

**Parameters:**

*   None

**Returns:**

*   `bool`: `True` if all operations complete successfully, `False` if any Git command or server startup fails.

**Execution:**

When `start_server.py` is run directly, the `main()` function is executed, performing the described Git operations and starting the server.

### Dependencies

*   `os`: For path manipulation and changing directories.
*   `subprocess`: For running shell commands.
*   `time`: For generating timestamps for commit messages.
*   `sys`: For system-specific parameters and functions (though not explicitly used beyond standard library import).
*   `pathlib`: For object-oriented filesystem paths.
*   `uvicorn`: (Runtime dependency) For serving the FastAPI application.

---

## `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a testing function for it.

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using a dynamic programming approach.

**Parameters:**

*   `n` (`int`): The position in the Fibonacci sequence (non-negative integer).

**Returns:**

*   `int`: The nth Fibonacci number.

**Logic:**

*   Returns `0` for `n <= 0`.
*   Returns `1` for `n == 1` or `n == 2`.
*   For `n > 2`, it initializes a DP table `fib` and iteratively fills it using the recurrence `fib[i] = fib[i-1] + fib[i-2]`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases (0th to 8th Fibonacci numbers). It prints the input, calculated result, expected result, and a pass/fail status for each test case.

**Parameters:**

*   None

**Returns:**

*   `None` (Prints test results to the console).

**Execution:**

When `test_feature.py` is run directly, `test_fibonacci()` is called, which prints the test results for the `calculate_fibonacci` function.