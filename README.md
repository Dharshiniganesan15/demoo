# Project Documentation

This documentation describes the Python modules provided, detailing their purpose, functions, and usage based strictly on the provided code.

---

## Table of Contents

*   [Overview](#overview)
*   [Module: `demo_new_module.py`](#module-demo_new_modulepy)
    *   [`greet(name: str)`](#greetname-str)
    *   [`run_demo()`](#run_demo)
*   [Module: `main.py`](#module-mainpy)
    *   [`sum(a, b)`](#suma-b)
    *   [`sub(a, b)`](#suba-b)
    *   [`multiply(a, b)`](#multiplya-b)
    *   [`divide(a, b)`](#dividea-b)
*   [Module: `math_utils.py`](#module-math_utilspy)
    *   [`multiply(a, b)`](#multiplya-b-1)
    *   [`divide(a, b)`](#dividea-b-1)
    *   [`power(base, exponent)`](#powerbase-exponent)
*   [Module: `new_feature.py`](#module-new_featurepy)
    *   [`advanced_calculator()`](#advanced_calculator)
    *   [`test_calculator()`](#test_calculator)
*   [Module: `start_server.py`](#module-start_serverpy)
    *   [`run_command(cmd, cwd=None)`](#run_commandcmd-cwdnone)
    *   [`main()`](#main)
*   [Module: `test_feature.py`](#module-test_featurepy)
    *   [`calculate_fibonacci(n)`](#calculate_fibonaccin)
    *   [`test_fibonacci()`](#test_fibonacci)

---

## Overview

This collection of Python scripts demonstrates various functionalities including basic arithmetic operations, a greeting utility, a Fibonacci sequence calculator, and a utility for automating Git operations and starting a FastAPI server.

## Module: `demo_new_module.py`

This module provides a simple greeting function and a demonstration of its use.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"


def run_demo() -> None:
    print(greet("AI Doc System"))


if __name__ == "__main__":
    run_demo()

```

### `greet(name: str)`

Returns a personalized greeting message.

**Parameters:**

*   `name` (`str`): The name to be included in the greeting.

**Returns:**

*   `str`: A string in the format "Hello, {name}!".

### `run_demo()`

Prints a demonstration of the `greet` function with the name "AI Doc System".

**Returns:**

*   `None`

**Usage:**

When executed directly (`python demo_new_module.py`), it will call `run_demo()` which prints "Hello, AI Doc System!".

---

## Module: `main.py`

This module contains fundamental arithmetic functions.

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

### `sum(a, b)`

Adds two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The sum of `a` and `b`.

### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

**Parameters:**

*   `a`: The number from which to subtract.
*   `b`: The number to subtract.

**Returns:**

*   The result of `a - b`.

### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

**Parameters:**

*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**

*   The result of `a / b`.

**Raises:**

*   `ValueError`: If `b` is `0`.

---

## Module: `math_utils.py`

This module provides utility functions for basic mathematical operations.

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

### `multiply(a, b)`

Multiplies two numbers together.

**Parameters:**

*   `a`: The first number.
*   `b`: The second number.

**Returns:**

*   The product of `a` and `b`.

### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

**Parameters:**

*   `a`: The numerator.
*   `b`: The denominator.

**Returns:**

*   The result of `a / b`.

**Raises:**

*   `ValueError`: If `b` is `0`.

### `power(base, exponent)`

Calculates the `base` raised to the power of `exponent`.

**Parameters:**

*   `base`: The base number.
*   `exponent`: The exponent.

**Returns:**

*   The result of `base ** exponent`.

---

## Module: `new_feature.py`

This module defines an `advanced_calculator` function containing several nested arithmetic operations and a function to test these operations.

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

### `advanced_calculator()`

This function contains definitions for several arithmetic operations: `add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, and `factorial`. These nested functions are defined locally within `advanced_calculator()` and are not directly accessible from outside this function's scope.

The docstring indicates it "Supports addition, subtraction, multiplication, and division." The function body additionally defines `modulo`, `power`, and `factorial`.

### `test_calculator()`

This function attempts to test the operations described within `advanced_calculator`. It tries to access `add`, `subtract`, `multiply`, `divide`, `power`, and `factorial` as attributes of the `advanced_calculator` function (e.g., `advanced_calculator.add`).

**Note on Usage:**

As `advanced_calculator` is defined as a standard Python function, its nested functions (`add`, `subtract`, etc.) are local to its scope and not exposed as attributes. Direct calls like `advanced_calculator.add(5, 3)` will result in an `AttributeError` if executed as written, because `advanced_calculator` is a function object, not a module or an object instance exposing these operations as methods. The `test_calculator` function, as provided, demonstrates an intended usage pattern but will not execute successfully with the current structure of `advanced_calculator`.

**Usage:**

When executed directly (`python new_feature.py`), it will call `test_calculator()`.

---

## Module: `start_server.py`

This script automates Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

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

### `run_command(cmd, cwd=None)`

Executes a shell command and prints its output and status.

**Parameters:**

*   `cmd` (`str`): The command string to execute.
*   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`, meaning the current process's working directory.

**Returns:**

*   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

### `main()`

The main function that orchestrates the Git operations and server startup.

**Workflow:**

1.  **Determine Directories:** Identifies the current script's parent directory (`demoo_dir`) and its parent (`project_root`).
2.  **Git Operations:**
    *   Changes the current directory to `demoo_dir`.
    *   Adds all changes (`git add .`).
    *   Commits changes with an auto-generated timestamp message (e.g., "Auto-update documentation - YYYY-MM-DD HH:MM:SS").
    *   Pushes changes to the remote repository (`git push`).
3.  **Server Startup:**
    *   Changes the current directory to `project_root`.
    *   Attempts to import `uvicorn`.
    *   Starts a `uvicorn` server for `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Prints a placeholder Webhook URL.
    *   Handles `KeyboardInterrupt` to gracefully stop the server.

**Returns:**

*   `bool`: `True` if all operations complete, `False` if any step fails.

**Dependencies:**

*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `pathlib.Path`
*   `uvicorn` (implicitly required at runtime for server functionality)

**Usage:**

When executed directly (`python start_server.py`), it performs the described Git operations and then attempts to start a `uvicorn` server.

---

## Module: `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a function to test its correctness.

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

### `calculate_fibonacci(n)`

Calculates the nth Fibonacci number using dynamic programming.

**Parameters:**

*   `n` (`int`): The position in the Fibonacci sequence (0-indexed).

**Returns:**

*   `int`: The nth Fibonacci number.
    *   Returns `0` for `n <= 0`.
    *   Returns `1` for `n = 1` or `n = 2`.

### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of test cases and prints the results.

**Test Cases:**

| n | Expected Fibonacci |
|---|--------------------|
| 0 | 0                  |
| 1 | 1                  |
| 2 | 2                  |
| 3 | 3                  |
| 4 | 5                  |
| 5 | 8                  |
| 6 | 13                 |
| 7 | 21                 |
| 8 | 34                 |

**Usage:**

When executed directly (`python test_feature.py`), it will call `test_fibonacci()` and print the results of the Fibonacci calculations.