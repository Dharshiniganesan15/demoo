# Python Project Documentation

This document provides a comprehensive overview of the Python files within this project, detailing their functionalities, usage, and internal structures based strictly on the provided code.

## Project Structure

The project is organized into several Python modules, each serving a distinct purpose:

*   `demo_new_module.py`: Contains a simple greeting function and a demonstration runner.
*   `main.py`: Provides fundamental arithmetic operations.
*   `math_utils.py`: Offers basic mathematical utility functions.
*   `new_feature.py`: Implements an advanced calculator with various operations and an associated test suite.
*   `start_server.py`: A utility script to perform Git operations (add, commit, push) and then start a FastAPI server.
*   `test_feature.py`: Includes a function for calculating Fibonacci numbers and a testing mechanism for it.

---

## Modules

Detailed documentation for each Python file:

### `demo_new_module.py`

This module defines a basic greeting function and demonstrates its usage.

**Functions:**

*   `greet(name: str) -> str`
    *   **Description:** Generates a personalized greeting message.
    *   **Arguments:**
        *   `name` (`str`): The name to be included in the greeting.
    *   **Returns:**
        *   `str`: A string in the format "Hello, {name}!".
    *   **Example:**
        ```python
        greet("World") # Returns "Hello, World!"
        ```
*   `run_demo() -> None`
    *   **Description:** Executes a demonstration of the `greet` function by printing a greeting for "AI Doc System".
    *   **Arguments:** None
    *   **Returns:** None

**Usage:**

When executed as the main script, `run_demo()` will be called.

```bash
python demo_new_module.py
```

### `main.py`

This module provides a collection of fundamental arithmetic functions.

**Functions:**

*   `sum(a, b)`
    *   **Description:** Add two numbers together.
    *   **Arguments:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The sum of `a` and `b`.
*   `sub(a, b)`
    *   **Description:** Subtract b from a.
    *   **Arguments:**
        *   `a`: The number to subtract from.
        *   `b`: The number to subtract.
    *   **Returns:**
        *   The result of `a - b`.
*   `multiply(a, b)`
    *   **Description:** Multiply two numbers together.
    *   **Arguments:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The product of `a` and `b`.
*   `divide(a, b)`
    *   **Description:** Divide a by b with zero check.
    *   **Arguments:**
        *   `a`: The numerator.
        *   `b`: The denominator.
    *   **Returns:**
        *   The result of `a / b`.
    *   **Raises:**
        *   `ValueError`: If `b` is `0`.

### `math_utils.py`

This module serves as a collection of basic mathematical utility functions.

**Functions:**

*   `multiply(a, b)`
    *   **Description:** Multiply two numbers together.
    *   **Arguments:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The product of `a` and `b`.
*   `divide(a, b)`
    *   **Description:** Divide two numbers.
    *   **Arguments:**
        *   `a`: The numerator.
        *   `b`: The denominator.
    *   **Returns:**
        *   The result of `a / b`.
    *   **Raises:**
        *   `ValueError`: If `b` is `0`.
*   `power(base, exponent)`
    *   **Description:** Calculate base raised to the power of exponent.
    *   **Arguments:**
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns:**
        *   The result of `base` raised to the `exponent`.

### `new_feature.py`

This module defines an "advanced calculator" and a testing function for its operations.

**Functions:**

*   `advanced_calculator()`
    *   **Description:** Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, and division.
    *   **Internal Functions (defined within `advanced_calculator`):**
        *   `add(a, b)`: Returns `a + b`.
        *   `subtract(a, b)`: Returns `a - b`.
        *   `multiply(a, b)`: Returns `a * b`.
        *   `divide(a, b)`: Returns `a / b`. If `b` is `0`, returns the string `"Error: Division by zero"`.
        *   `modulo(a, b)`: Returns `a % b`. If `b` is `0`, returns the string `"Error: Modulo by zero"`.
        *   `power(base, exponent)`: Calculates `base` raised to `exponent` using a loop.
        *   `factorial(n)`: Calculates the factorial of `n`. Returns `1` if `n` is `0`. If `n` is negative, returns the string `"Error: Negative number"`.
    *   **Note:** The internal functions defined within `advanced_calculator()` are scoped locally to that function and are not directly accessible from outside its execution context as attributes (e.g., `advanced_calculator.add`).
*   `test_calculator()`
    *   **Description:** Tests the operations intended for the advanced calculator. It attempts to call `add`, `subtract`, `multiply`, `divide`, `power`, and `factorial` as attributes of `advanced_calculator`. The test results are printed to the console, indicating `✅` for pass and `❌` for fail based on expected values.
    *   **Arguments:** None
    *   **Returns:** None

**Usage:**

When executed as the main script, `test_calculator()` will be called.

```bash
python new_feature.py
```

### `start_server.py`

This script is designed to automate a Git commit and push process, and subsequently start a FastAPI server.

**Dependencies:**

*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib.Path`
*   `uvicorn` (implicitly imported and used at runtime for starting the server)

**Functions:**

*   `run_command(cmd, cwd=None)`
    *   **Description:** Runs a shell command and captures its output and error. It prints success or error messages to the console.
    *   **Arguments:**
        *   `cmd` (`str`): The command string to execute.
        *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None` (current directory).
    *   **Returns:**
        *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.
*   `main()`
    *   **Description:** Main function to start server with single git push. This function orchestrates the entire process:
        1.  **Directory Setup:** Determines the `demoo_dir` (directory of this script) and `project_root` (parent of `demoo_dir`).
        2.  **Git Operations:**
            *   Changes to `demoo_dir`.
            *   Adds all changes to Git (`git add .`).
            *   Commits changes with an auto-generated timestamped message (`git commit -m "Auto-update documentation - {YYYY-MM-DD HH:MM:SS}"`). If no changes are present or commit fails, it prints a message but attempts to proceed to push.
            *   Pushes changes to the remote repository (`git push`).
        3.  **Server Start:**
            *   Changes back to `project_root`.
            *   Prints server information including the local URL (`http://localhost:8000`) and a specific webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
            *   Starts a `uvicorn` server using the application `"backend.app:app"` on host `0.0.0.0`, port `8000`, with `reload` enabled and `info` log level.
            *   Handles `KeyboardInterrupt` to gracefully stop the server.
    *   **Arguments:** None
    *   **Returns:**
        *   `bool`: `True` if the overall process completes successfully, `False` if any critical step (Git add, Git push, server start) fails.

**Usage:**

When executed as the main script, `main()` will be called.

```bash
python start_server.py
```

### `test_feature.py`

This module provides a function to calculate Fibonacci numbers and a self-contained test suite for it.

**Functions:**

*   `calculate_fibonacci(n)`
    *   **Description:** Calculate the nth Fibonacci number using dynamic programming.
    *   **Arguments:**
        *   `n` (`int`): The position in the Fibonacci sequence.
    *   **Returns:**
        *   `int`: The nth Fibonacci number. Returns `0` for `n <= 0`, `1` for `n == 1` or `n == 2`. Uses a dynamic programming approach for `n > 2`.
*   `test_fibonacci()`
    *   **Description:** Tests the `calculate_fibonacci` function against a predefined set of test cases (Fibonacci numbers from 0 to 8). It prints the results for each test case, indicating `✅ PASS` or `❌ FAIL`.
    *   **Arguments:** None
    *   **Returns:** None

**Usage:**

When executed as the main script, `test_fibonacci()` will be called.

```bash
python test_feature.py
```