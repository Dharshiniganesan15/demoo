This document provides a comprehensive overview of the provided Python codebase, detailing each file, its functions, and execution behavior based strictly on the provided code.

## Project Overview

This repository contains a collection of Python scripts demonstrating various functionalities, including basic mathematical operations, an advanced calculator, Fibonacci sequence calculation, a simple greeting module, and a script for automating Git operations before starting a FastAPI server.

## Code Structure

The project is organized into several Python files, each serving a distinct purpose:

*   `demo_new_module.py`: A simple module demonstrating a greeting function.
*   `main.py`: Provides fundamental arithmetic functions.
*   `math_utils.py`: Offers common mathematical utility functions.
*   `new_feature.py`: Implements an advanced calculator with multiple operations and includes a testing suite.
*   `start_server.py`: A utility script for performing Git commits and pushes, then starting a `uvicorn` server.
*   `test_feature.py`: Contains a function to calculate Fibonacci numbers using dynamic programming and a corresponding test function.

---

## File: `demo_new_module.py`

This module provides basic greeting functionality and a demonstration function.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


def run_demo() -> None:
    print(greet("AI Doc System"))


if __name__ == "__main__":
    run_demo()

```

### Functions

#### `greet(name: str) -> str`

Returns a formatted greeting string.

*   **Parameters:**
    *   `name` (`str`): The name to be included in the greeting.
*   **Returns:**
    *   `str`: A string in the format "Hello, {name}!".

#### `run_demo() -> None`

Prints a greeting message using the `greet` function with the fixed name "AI Doc System".

*   **Parameters:**
    *   None
*   **Returns:**
    *   `None`

### Script Execution

When `demo_new_module.py` is executed directly, it calls `run_demo()`, which in turn prints "Hello, AI Doc System!" to the console.

---

## File: `main.py`

This file defines a set of basic arithmetic operations.

```python
def sum(a, b):
    """Add two numbers together."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers together."""
    return a * b

def divide(a, b):
    """Divide a by b with zero check."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Test with Gemini AI documentation - 2026-01-30
```

### Functions

#### `sum(a, b)`

Adds two numbers.

*   **Parameters:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

*   **Parameters:**
    *   `a`: The minuend.
    *   `b`: The subtrahend.
*   **Returns:**
    *   The difference `a - b`.

#### `multiply(a, b)`

Multiplies two numbers.

*   **Parameters:**
    *   `a`: The first factor.
    *   `b`: The second factor.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`). Includes a check to prevent division by zero.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The quotient `a / b`.
*   **Raises:**
    *   `ValueError`: If `b` is `0`, with the message "Cannot divide by zero".

### Notes

The file contains a comment: `# Test with Gemini AI documentation - 2026-01-30`. This is a non-executable comment.

---

## File: `math_utils.py`

This file provides a collection of mathematical utility functions for basic operations.

```python
"""
Math utilities for basic operations
"""

def multiply(a, b):
    """Multiply two numbers together."""
    return a * b

def divide(a, b):
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    return base ** exponent

```

### Functions

#### `multiply(a, b)`

Multiplies two numbers.

*   **Parameters:**
    *   `a`: The first factor.
    *   `b`: The second factor.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`). Includes a check to prevent division by zero.

*   **Parameters:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The quotient `a / b`.
*   **Raises:**
    *   `ValueError`: If `b` is `0`, with the message "Cannot divide by zero".

#### `power(base, exponent)`

Calculates the `base` raised to the power of the `exponent`.

*   **Parameters:**
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns:**
    *   The result of `base` to the power of `exponent`.

---

## File: `new_feature.py`

This file defines an `advanced_calculator` function which contains several nested arithmetic operations, and a `test_calculator` function to demonstrate their usage.

```python
def advanced_calculator():
    """
    Advanced calculator with multiple operations.
    Supports addition, subtraction, multiplication, and division.
    """

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def modulo(a, b):
        if b == 0:
            return "Error: Modulo by zero"
        return a % b

    def power(base, exponent):
        result = 1
        for _ in range(exponent):
            result *= base
        return result

    def factorial(n):
        if n < 0:
            return "Error: Negative number"
        elif n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def test_calculator():
    """Test the advanced calculator"""
    print("Testing Advanced Calculator:")

    # Test addition
    result = advanced_calculator.add(5, 3)
    print(f"  5 + 3 = {result} {'✅' if result == 8 else '❌'}")

    # Test subtraction
    result = advanced_calculator.subtract(10, 4)
    print(f"  10 - 4 = {result} {'✅' if result == 6 else '❌'}")

    # Test multiplication
    result = advanced_calculator.multiply(7, 6)
    print(f"  7 * 6 = {result} {'✅' if result == 42 else '❌'}")

    # Test division
    result = advanced_calculator.divide(15, 3)
    print(f"  15 / 3 = {result} {'✅' if result == 5 else '❌'}")

    # Test power
    result = advanced_calculator.power(2, 8)
    print(f"  2^8 = {result} {'✅' if result == 256 else '❌'}")

    # Test factorial
    result = advanced_calculator.factorial(5)
    print(f"  5! = {result} {'✅' if result == 120 else '❌'}")

if __name__ == "__main__":
    test_calculator()

```

### Functions

#### `advanced_calculator()`

This function's primary purpose, as indicated by its docstring, is to provide an advanced calculator. It defines several nested functions for various arithmetic operations. As written, the `advanced_calculator` function itself does not return these nested functions or an object containing them.

##### Nested Functions (defined within `advanced_calculator`)

*   `add(a, b)`: Adds two numbers.
    *   **Returns:** The sum of `a` and `b`.
*   `subtract(a, b)`: Subtracts `b` from `a`.
    *   **Returns:** The difference `a - b`.
*   `multiply(a, b)`: Multiplies two numbers.
    *   **Returns:** The product of `a` and `b`.
*   `divide(a, b)`: Divides `a` by `b`.
    *   **Returns:** The quotient `a / b`. If `b` is `0`, returns the string "Error: Division by zero".
*   `modulo(a, b)`: Calculates the modulo of `a` by `b`.
    *   **Returns:** The remainder `a % b`. If `b` is `0`, returns the string "Error: Modulo by zero".
*   `power(base, exponent)`: Calculates `base` raised to the power of `exponent` using a loop.
    *   **Returns:** The result of the power calculation.
*   `factorial(n)`: Calculates the factorial of `n`.
    *   **Returns:** The factorial of `n`. If `n` is negative, returns "Error: Negative number". If `n` is `0`, returns `1`.

#### `test_calculator()`

This function is intended to test the operations provided by `advanced_calculator`. It attempts to access and call the nested functions (e.g., `add`, `subtract`) as attributes of the `advanced_calculator` function itself (e.g., `advanced_calculator.add`). It prints the results of these test cases along with a pass/fail indicator.

*   **Note on Usage:** As written, calling `advanced_calculator.add`, `advanced_calculator.subtract`, etc., will result in an `AttributeError` because `advanced_calculator` is a function that defines inner functions but does not return an object or module that exposes them as attributes. The `test_calculator` function demonstrates the *intended* usage pattern, but this pattern is not supported by the current definition of `advanced_calculator`.

### Script Execution

When `new_feature.py` is executed directly, it calls `test_calculator()`, which then attempts to run the defined tests and print their outcomes.

---

## File: `start_server.py`

This script automates a sequence of Git operations (add, commit, push) and then proceeds to start a `uvicorn` server.

```python
#!/usr/bin/env python3
"""
Start server with single automatic git push
"""

import os
import subprocess
import time
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    try:
        result = subprocess.run(cmd, shell=True, cwd=cwd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Error running {cmd}: {result.stderr}")
            return False
        print(f"Success: {cmd}")
        if result.stdout:
            print(f"Output: {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"Exception running {cmd}: {e}")
        return False

def main():
    """Main function to start server with single git push."""
    # Get the demoo directory
    demoo_dir = Path(__file__).parent
    project_root = demoo_dir.parent

    print(f"Project root: {project_root}")
    print(f"Demoo directory: {demoo_dir}")

    # Change to demoo directory for git operations
    os.chdir(demoo_dir)

    # 1. Add all changes
    print("\n=== Adding changes to git ===")
    if not run_command("git add ."):
        print("Failed to add changes")
        return False

    # 2. Commit changes
    print("\n=== Committing changes ===")
    commit_message = f"Auto-update documentation - {time.strftime('%Y-%m-%d %H:%M:%S')}"
    if not run_command(f'git commit -m "{commit_message}"'):
        print("No changes to commit or commit failed")

    # 3. Push to git (only once!)
    print("\n=== Pushing to git (once) ===")
    if not run_command("git push"):
        print("Failed to push to git")
        return False

    print("\n=== Git push completed successfully! ===")

    # 4. Start the server
    print("\n=== Starting FastAPI server ===")
    os.chdir(project_root)

    # Start the server
    try:
        import uvicorn
        print("Starting server on http://localhost:8000")
        print("Webhook URL: https://da3b21fd5fff.ngrok-free.app/webhook/git")
        print("Press Ctrl+C to stop the server")

        # Run the server
        uvicorn.run(
            "backend.app:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
            log_level="info"
        )

    except KeyboardInterrupt:
        print("\nServer stopped by user")
    except Exception as e:
        print(f"Error starting server: {e}")
        return False

    return True

if __name__ == "__main__":
    main()

```

### Dependencies

*   `os`: For interacting with the operating system, particularly changing directories.
*   `subprocess`: For running external shell commands (e.g., Git commands).
*   `time`: For generating timestamps in commit messages.
*   `sys`: Standard system module (though not explicitly used in the main logic shown).
*   `pathlib.Path`: For object-oriented filesystem paths.
*   `uvicorn`: Imported at runtime to start the server. This module must be installed in the environment for the server to start successfully.

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command. It captures standard output and standard error, and prints messages indicating success, errors, or exceptions.

*   **Parameters:**
    *   `cmd` (`str`): The command string to execute.
    *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`, meaning the current Python process's working directory.
*   **Returns:**
    *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

#### `main()`

The main function orchestrates the script's operations:

1.  **Directory Resolution:** Determines the script's directory and the project root directory.
2.  **Git Operations:**
    *   Changes the current working directory to the script's directory (`demoo_dir`).
    *   Executes `git add .` to stage all changes.
    *   Executes `git commit -m "{commit_message}"` with an auto-generated timestamped message. It reports "No changes to commit or commit failed" if the commit command fails.
    *   Executes `git push` to push committed changes to the remote repository.
3.  **Server Startup:**
    *   Changes the current working directory back to the `project_root`.
    *   Imports `uvicorn` and attempts to start a `uvicorn` server for `backend.app:app`.
    *   The server is configured to listen on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Prints expected server URL (`http://localhost:8000`) and a `Webhook URL` (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
    *   The server can be stopped by pressing `Ctrl+C` (handled by `KeyboardInterrupt`).
    *   Reports errors if `uvicorn` fails to start.

*   **Returns:**
    *   `bool`: `True` if all operations (Git and server start) are successful, `False` otherwise.

### Script Execution

When `start_server.py` is executed directly, the `main()` function is called. This sequence of operations first attempts to add, commit, and push any Git changes, and then starts a `uvicorn` server.

---

## File: `test_feature.py`

This file provides a function to calculate Fibonacci numbers using dynamic programming and a testing utility for it.

```python
def calculate_fibonacci(n):
    """
    Calculate the nth Fibonacci number using dynamic programming.

    Args:
        n (int): The position in the Fibonacci sequence

    Returns:
        int: The nth Fibonacci number
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1

    # Initialize DP table
    fib = [0] * (n + 1)
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1

    # Fill DP table
    for i in range(3, n + 1):
        fib[i] = fib[i-1] + fib[i-2]

    return fib[n]

def test_fibonacci():
    """Test the Fibonacci function"""
    test_cases = [0, 1, 2, 3, 5, 8, 13, 21, 34]

    print("Testing Fibonacci function:")
    for i, expected in enumerate(test_cases):
        result = calculate_fibonacci(i)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        print(f"  fib({i}) = {result} (expected {expected}) {status}")

if __name__ == "__main__":
    test_fibonacci()

```

### Functions

#### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using a dynamic programming approach. It handles base cases for `n <= 0`, `n == 1`, and `n == 2` explicitly.

*   **Parameters:**
    *   `n` (`int`): The position in the Fibonacci sequence (0-indexed where fib(0)=0).
*   **Returns:**
    *   `int`: The nth Fibonacci number.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases. It iterates through expected Fibonacci numbers, calls `calculate_fibonacci` for the corresponding index, and prints whether the test passed or failed.

*   **Parameters:**
    *   None
*   **Returns:**
    *   `None` (prints results to console).

### Script Execution

When `test_feature.py` is executed directly, it calls `test_fibonacci()`, which runs the tests and prints the results to the console.