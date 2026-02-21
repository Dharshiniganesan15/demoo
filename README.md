This document provides a comprehensive overview of the Python codebase, analyzing each file and its contents as provided.

---

# Python Codebase Documentation

This documentation details the functionality, structure, and usage of the Python modules present in this repository. The codebase includes utilities for basic arithmetic, advanced calculations, Fibonacci sequence computation, a greeting demonstration, and a script for automating Git operations and starting a FastAPI server.

## Table of Contents

*   [File: `demo_new_module.py`](#file-demo_new_modulepy)
*   [File: `main.py`](#file-mainpy)
*   [File: `math_utils.py`](#file-math_utilspy)
*   [File: `new_feature.py`](#file-new_featurepy)
*   [File: `start_server.py`](#file-start_serverpy)
*   [File: `test_feature.py`](#file-test_featurepy)

---

## File: `demo_new_module.py`

This module contains a simple greeting function and a demonstration runner.

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

Returns a personalized greeting string.

*   **Arguments:**
    *   `name` (`str`): The name to be included in the greeting.
*   **Returns:**
    *   `str`: A formatted greeting string, e.g., "Hello, [name]!".

#### `run_demo() -> None`

Executes a demonstration of the `greet` function by printing a greeting to the console.

*   **Returns:**
    *   `None`

### Usage

When executed directly, this script calls `run_demo()` which prints "Hello, AI Doc System!".

```bash
python demo_new_module.py
```

---

## File: `main.py`

This module provides a collection of basic arithmetic operations.

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

Adds two numbers together.

*   **Arguments:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The sum of `a` and `b`.

#### `sub(a, b)`

Subtracts the second number (`b`) from the first number (`a`).

*   **Arguments:**
    *   `a`: The number to subtract from.
    *   `b`: The number to subtract.
*   **Returns:**
    *   The result of `a - b`.

#### `multiply(a, b)`

Multiplies two numbers together.

*   **Arguments:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

*   **Arguments:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The result of `a / b`.
*   **Raises:**
    *   `ValueError`: If `b` is `0`, indicating division by zero.

---

## File: `math_utils.py`

This module provides basic mathematical utility functions.

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

Multiplies two numbers together.

*   **Arguments:**
    *   `a`: The first number.
    *   `b`: The second number.
*   **Returns:**
    *   The product of `a` and `b`.

#### `divide(a, b)`

Divides the first number (`a`) by the second number (`b`), including a check for division by zero.

*   **Arguments:**
    *   `a`: The dividend.
    *   `b`: The divisor.
*   **Returns:**
    *   The result of `a / b`.
*   **Raises:**
    *   `ValueError`: If `b` is `0`, indicating division by zero.

#### `power(base, exponent)`

Calculates the `base` raised to the power of the `exponent`.

*   **Arguments:**
    *   `base`: The base number.
    *   `exponent`: The exponent.
*   **Returns:**
    *   The result of `base` to the `exponent` power.

---

## File: `new_feature.py`

This module defines an `advanced_calculator` function containing several nested mathematical operations and a `test_calculator` function to demonstrate their usage (though the test function's approach to calling nested functions is not standard Python practice).

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

An outer function intended to encapsulate various mathematical operations. The operations are defined as nested functions within `advanced_calculator()`. These nested functions are local to `advanced_calculator()` and are not directly accessible from outside its scope.

*   **Nested Functions:**
    *   `add(a, b)`: Returns the sum of `a` and `b`.
    *   `subtract(a, b)`: Returns `a - b`.
    *   `multiply(a, b)`: Returns the product of `a` and `b`.
    *   `divide(a, b)`: Returns `a / b`. If `b` is `0`, it returns the string "Error: Division by zero".
    *   `modulo(a, b)`: Returns `a % b`. If `b` is `0`, it returns the string "Error: Modulo by zero".
    *   `power(base, exponent)`: Calculates `base` raised to the `exponent` using an iterative loop.
    *   `factorial(n)`: Calculates the factorial of `n`. Returns `1` for `n=0`. If `n` is negative, it returns the string "Error: Negative number".

#### `test_calculator()`

This function is designed to test the operations defined within `advanced_calculator()`. It attempts to call the nested functions (e.g., `add`, `subtract`) as attributes of the `advanced_calculator` function (e.g., `advanced_calculator.add`). In standard Python, functions do not have attributes derived from their nested functions in this manner, and such calls would typically result in an `AttributeError` at runtime. The function prints the results of these attempted operations and indicates success or failure based on expected values.

*   **Returns:**
    *   `None`

### Usage

When executed directly, this script calls `test_calculator()`. The calls within `test_calculator()` (e.g., `advanced_calculator.add`) will likely fail at runtime due to `AttributeError` because the nested functions are not attributes of `advanced_calculator`.

```bash
python new_feature.py
```

---

## File: `start_server.py`

This script automates common Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

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

*   `os`: For interacting with the operating system, like changing directories.
*   `subprocess`: For running external commands (e.g., Git commands).
*   `time`: For generating timestamps in commit messages.
*   `sys`: Standard system module (not explicitly used in the main logic, but imported).
*   `pathlib.Path`: For object-oriented filesystem paths.
*   `uvicorn`: A lightning-fast ASGI server, used to run the FastAPI application (`backend.app:app`). This module is dynamically imported within `main()`.

### Functions

#### `run_command(cmd, cwd=None)`

Executes a shell command and captures its output. It prints success or error messages and returns a boolean indicating the command's success.

*   **Arguments:**
    *   `cmd` (`str`): The command string to execute.
    *   `cwd` (`str`, optional): The current working directory for the command. Defaults to `None`, meaning the current directory of the script.
*   **Returns:**
    *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.

#### `main()`

The main function orchestrates the Git operations and server startup.

1.  **Determines Project Paths**: Identifies the script's directory (`demoo_dir`) and its parent directory (`project_root`).
2.  **Git Operations**:
    *   Changes the current working directory to `demoo_dir`.
    *   Executes `git add .` to stage all changes.
    *   Executes `git commit` with an auto-generated timestamped message.
    *   Executes `git push` to push committed changes to the remote repository.
3.  **Server Startup**:
    *   Changes the current working directory back to `project_root`.
    *   Attempts to import `uvicorn`.
    *   Prints server information, including a local host URL and a placeholder "Webhook URL".
    *   Starts the `uvicorn` server for the FastAPI application `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
    *   Handles `KeyboardInterrupt` to gracefully stop the server.
    *   Handles other exceptions during server startup.

*   **Returns:**
    *   `bool`: `True` if all operations complete successfully, `False` if any step (Git command, server startup) fails.

### Usage

When executed directly, this script will:
1.  Print current project and demo directory paths.
2.  Perform `git add .`, `git commit`, and `git push` from the script's directory.
3.  Then, it will attempt to start a `uvicorn` server for `backend.app:app` on `http://localhost:8000`. This requires `uvicorn` to be installed and for `backend/app.py` to exist relative to the project root and define an `app` object.

```bash
python start_server.py
```

---

## File: `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a test function to verify its correctness.

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

Calculates the nth Fibonacci number using a dynamic programming approach.

*   **Arguments:**
    *   `n` (`int`): The position in the Fibonacci sequence (0-indexed where fib(0)=0, fib(1)=1, fib(2)=1).
*   **Returns:**
    *   `int`: The nth Fibonacci number.
*   **Logic:**
    *   Handles base cases for `n <= 0`, `n == 1`, and `n == 2`.
    *   Initializes a DP table `fib` of size `n + 1`.
    *   Fills the table iteratively from `i = 3` up to `n`, where `fib[i] = fib[i-1] + fib[i-2]`.

#### `test_fibonacci()`

Tests the `calculate_fibonacci` function against a predefined set of expected Fibonacci numbers. It iterates through test cases, calls the function, and prints the result along with a "PASS" or "FAIL" status.

*   **Returns:**
    *   `None`

### Usage

When executed directly, this script calls `test_fibonacci()` which runs various tests for the `calculate_fibonacci` function and prints their outcomes.

```bash
python test_feature.py
```