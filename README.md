# AI Documentation System

This repository hosts a collection of Python modules designed to demonstrate various features, including an automated documentation system powered by AI, general utility functions, and mathematical tools. The core of the system is a smart webhook processor that integrates with Git to analyze code changes and trigger AI-driven documentation updates, such as generating README files.

## Table of Contents
- [Features](#features)
- [Files Overview](#files-overview)
    - [`demo_new_module.py`](#demo_new_modulepy)
    - [`main.py`](#mainpy)
    - [`math_utils.py`](#math_utilspy)
    - [`new_feature.py`](#new_featurepy)
    - [`smart_webhook_feature.py`](#smart_webhook_featurepy)
    - [`start_server.py`](#start_serverpy)
    - [`test_feature.py`](#test_featurepy)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

*   **Automated Documentation Generation**: AI-powered system that analyzes code structure and generates documentation (e.g., `README.md`).
*   **Smart Webhook Integration**: Processes GitHub webhook payloads to detect relevant code changes.
*   **Git Integration**: Automates `git add`, `git commit`, and `git push` operations.
*   **FastAPI Server Launch**: Includes a script to start a FastAPI server, potentially for handling webhooks.
*   **General Utility Functions**: A suite of basic mathematical, string manipulation, and algorithmic functions.
*   **Advanced Calculator**: A module demonstrating a more comprehensive set of arithmetic and mathematical operations.
*   **Fibonacci Calculation**: Includes multiple implementations for calculating Fibonacci numbers.

## Files Overview

### `demo_new_module.py`

This module provides a simple greeting function and demonstrates its execution.

#### Functions

*   `greet(name: str) -> str`:
    Returns a personalized greeting message.
*   `run_demo() -> None`:
    Prints a greeting using the `greet` function.

#### Usage

When executed directly, it calls `run_demo()` to print "Hello, AI Doc System!".

```python
# Example:
# python demo_new_module.py
# Output: Hello, AI Doc System!
```

### `main.py`

This module contains a collection of basic mathematical, financial, string manipulation, and algorithmic functions.

#### Functions

*   `sum(a, b)`:
    Adds two numbers together.
*   `sub(a, b)`:
    Subtracts `b` from `a`.
*   `multiply(a, b)`:
    Multiplies two numbers together.
*   `divide(a, b)`:
    Divides `a` by `b` with a zero check. Raises `ValueError` if `b` is zero.
*   `calculate_tax(income: float) -> float`:
    Calculates tax on income at a fixed 10% rate.
*   `calculate_discount(price: float, discount_percent: float) -> float`:
    Calculates the discount amount on a given price. Raises `ValueError` if `discount_percent` is not between 0 and 100.
*   `average(a: float, b: float) -> float`:
    Returns the average of two numbers.
*   `max_of_two(a: float, b: float) -> float`:
    Returns the larger of two numbers.
*   `is_palindrome(text: str) -> bool`:
    Checks if a string is a palindrome (reads the same forwards and backwards), ignoring non-alphanumeric characters and case.
    *   `Args`:
        *   `text (str)`: The string to check.
    *   `Returns`:
        *   `bool`: `True` if the string is a palindrome, `False` otherwise.
*   `fibonacci(n: int) -> int`:
    Calculates the nth Fibonacci number using iteration (0-indexed). Raises `ValueError` if `n` is negative.
    *   `Args`:
        *   `n (int)`: The position in the Fibonacci sequence.
    *   `Returns`:
        *   `int`: The nth Fibonacci number.
*   `factorial(n: int) -> int`:
    Calculates the factorial of a non-negative integer. Raises `ValueError` if `n` is negative.
    *   `Args`:
        *   `n (int)`: A non-negative integer.
    *   `Returns`:
        *   `int`: The factorial of `n`.

### `math_utils.py`

This module provides basic mathematical utility functions.

#### Functions

*   `multiply(a, b)`:
    Multiplies two numbers together.
*   `divide(a, b)`:
    Divides two numbers. Raises `ValueError` if `b` is zero.
*   `power(base, exponent)`:
    Calculates `base` raised to the power of `exponent`.

### `new_feature.py`

This module demonstrates an advanced calculator concept with various arithmetic and mathematical operations, and includes a testing function.

#### Functions

*   `advanced_calculator()`:
    A function that defines several nested helper functions for arithmetic and mathematical operations:
    *   `add(a, b)`: Returns the sum of `a` and `b`.
    *   `subtract(a, b)`: Returns `a` minus `b`.
    *   `multiply(a, b)`: Returns the product of `a` and `b`.
    *   `divide(a, b)`: Returns `a` divided by `b`. Returns "Error: Division by zero" if `b` is zero.
    *   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. Returns "Error: Modulo by zero" if `b` is zero.
    *   `power(base, exponent)`: Calculates `base` raised to the power of `exponent` using a loop.
    *   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative, otherwise returns the factorial.
    *   *Note: The nested functions defined within `advanced_calculator` are not directly accessible from outside its scope in the provided code.*
*   `test_calculator()`:
    Tests the operations intended for the advanced calculator by attempting to call them as attributes of `advanced_calculator`. Prints the results and indicates pass/fail.
    *   *Note: As written, this function attempts to call methods like `advanced_calculator.add`, which would result in an `AttributeError` because `advanced_calculator` is a function, not an object with those attributes. This section of the code illustrates the intended testing scenario rather than functional execution.*

#### Usage

When executed directly, it runs `test_calculator()` to display test results for the calculator operations.

```python
# Example:
# python new_feature.py
# Output will show intended test results (but would fail at runtime due to AttributeErrors).
```

### `smart_webhook_feature.py`

This module implements the core logic for a smart webhook feature, designed to process GitHub webhooks and generate documentation updates based on code changes. It includes classes for webhook processing and documentation generation using AI analysis.

#### Classes

*   `WebhookProcessor`:
    Processes GitHub webhooks for automatic documentation updates.
    *   `__init__(self, webhook_secret: str)`:
        Initializes the processor with a webhook secret.
    *   `verify_webhook_signature(self, payload: str, signature: str) -> bool`:
        Verifies the GitHub webhook signature using HMAC-SHA256 for security.
        *   `Args`:
            *   `payload (str)`: The webhook payload body.
            *   `signature (str)`: The `X-Hub-Signature-256` header.
        *   `Returns`:
            *   `bool`: `True` if the signature is valid, `False` otherwise.
    *   `analyze_commit_changes(self, commit_data: Dict[str, Any]) -> Dict[str, Any]`:
        Analyzes commit changes to determine if a documentation update is needed. It checks for changes in files with common code extensions.
        *   `Args`:
            *   `commit_data (Dict[str, Any])`: GitHub commit information.
        *   `Returns`:
            *   `Dict[str, Any]`: Analysis results including `has_relevant_changes`, `relevant_files`, `total_changes`, and `analysis_timestamp`.
    *   `generate_documentation_update(self, repo_name: str, commit_hash: str) -> Dict[str, Any]`:
        Simulates the generation of a documentation update for a repository.
        *   `Args`:
            *   `repo_name (str)`: Name of the repository.
            *   `commit_hash (str)`: Git commit hash.
        *   `Returns`:
            *   `Dict[str, Any]`: Documentation update information, including status, AI analysis, confidence, and estimated quality.
    *   `process_webhook_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]`:
        Processes an incoming webhook payload, extracts repository and commit information, analyzes changes, and coordinates documentation updates.
        *   `Args`:
            *   `payload (Dict[str, Any])`: GitHub webhook payload.
        *   `Returns`:
            *   `Dict[str, Any]`: Processing results, including status, analysis, and documentation update details.
*   `DocumentationGenerator`:
    Generates documentation using AI analysis.
    *   `__init__(self, ai_model: str = "gemini-2.5-flash")`:
        Initializes the generator with an AI model name.
    *   `analyze_code_structure(self, file_paths: list) -> Dict[str, Any]`:
        Analyzes the code structure of provided file paths to determine documentation needs and complexity.
        *   `Args`:
            *   `file_paths (list)`: List of code file paths.
        *   `Returns`:
            *   `Dict[str, Any]`: Code structure analysis, including file types, complexity score, and identified documentation needs.
    *   `generate_readme_content(self, repo_name: str, structure: Dict[str, Any]) -> str`:
        Generates `README.md` content based on the repository name and code structure analysis.
        *   `Args`:
            *   `repo_name (str)`: Repository name.
            *   `structure (Dict[str, Any])`: Code structure analysis results.
        *   `Returns`:
            *   `str`: The generated README content in Markdown format.

#### Usage

When executed directly, it demonstrates the `WebhookProcessor` and `DocumentationGenerator` by processing an example webhook payload, analyzing code structure, and generating a sample README.

```python
# Example:
# python smart_webhook_feature.py
# Output:
# Webhook Processing Result: {...}
# Code Structure Analysis: {...}
# Generated README Content: # demoo ...
```

### `start_server.py`

This script automates Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

#### Functions

*   `run_command(cmd, cwd=None)`:
    Runs a shell command, captures its output, and prints success or error messages.
    *   `Args`:
        *   `cmd (str)`: The command to run.
        *   `cwd (str, optional)`: The current working directory for the command. Defaults to `None`.
    *   `Returns`:
        *   `bool`: `True` if the command succeeded, `False` otherwise.
*   `main()`:
    Main function to orchestrate the Git operations and server startup. It navigates to the project root, performs `git add .`, `git commit -m "Auto-update documentation..."`, and `git push`. Afterward, it attempts to start a `uvicorn` server for `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.

#### Usage

When executed directly, it performs the Git operations, prints their status, and then launches the FastAPI server. It also provides a sample webhook URL.

```bash
# Example:
# python start_server.py
# Output will show git operation logs and server startup messages.
# Example Webhook URL: https://da3b21fd5fff.ngrok-free.app/webhook/git
```

### `test_feature.py`

This module provides an implementation of the Fibonacci sequence calculation using dynamic programming and a function to test it.

#### Functions

*   `calculate_fibonacci(n)`:
    Calculates the nth Fibonacci number using a dynamic programming approach.
    *   `Args`:
        *   `n (int)`: The position in the Fibonacci sequence.
    *   `Returns`:
        *   `int`: The nth Fibonacci number. Returns 0 for `n <= 0`, 1 for `n = 1` or `n = 2`.
*   `test_fibonacci()`:
    Tests the `calculate_fibonacci` function against a predefined set of test cases, printing the results and indicating pass/fail.

#### Usage

When executed directly, it runs `test_fibonacci()` to display test results for the Fibonacci function.

```python
# Example:
# python test_feature.py
# Output:
# Testing Fibonacci function:
#   fib(0) = 0 (expected 0) ✅ PASS
#   fib(1) = 1 (expected 1) ✅ PASS
#   ...
```

## Installation

To set up and run this project, you will need Python 3.x.

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```
2.  **Install dependencies**:
    Based on the `start_server.py` file, `uvicorn` is a dependency for running the server. Other modules might imply standard Python libraries or specific third-party ones.
    ```bash
    pip install uvicorn # For the FastAPI server
    # Add other dependencies if they become apparent (e.g., FastAPI if this is a FastAPI app)
    ```
    *Note: The `smart_webhook_feature.py` uses `hashlib` and `datetime` from the standard library, and `typing` which are built-in or common. It attempts to use `hmac.compare_digest`, which implies the `hmac` module is also needed, although it's not explicitly imported at the top level of the file.*

## Usage

### Running the Automated Documentation System

To start the system, which includes performing a Git push and launching the FastAPI server:

```bash
python start_server.py
```

This command will:
1.  Add all local changes to Git.
2.  Commit changes with an auto-generated message.
3.  Push the commit to the remote repository.
4.  Start a `uvicorn` server on `http://localhost:8000`.

### Testing Individual Features

You can run individual demo or test files directly:

*   **Demo Greeting**:
    ```bash
    python demo_new_module.py
    ```
*   **Test Advanced Calculator (Conceptual)**:
    ```bash
    python new_feature.py
    ```
    *(Note: This script demonstrates intended usage but contains calls that would result in runtime errors due to how nested functions are defined and accessed.)*
*   **Test Fibonacci Calculation**:
    ```bash
    python test_feature.py
    ```

## Contributing

1.  Fork the repository.
2.  Create a feature branch.
3.  Make your changes.
4.  Submit a pull request.

## License

MIT License - see LICENSE file for details

---
*This documentation was automatically generated by the AI Documentation System.*