# AI Documentation System

This project implements a system for automated documentation generation driven by GitHub webhooks and AI analysis. It includes modules for processing webhooks, analyzing code changes, generating documentation (like README files), and various utility functions.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Demo](#running-the-demo)
  - [Utilizing Math and Utility Functions](#utilizing-math-and-utility-functions)
  - [Using the Advanced Calculator](#using-the-advanced-calculator)
  - [Starting the Server and Triggering Documentation](#starting-the-server-and-triggering-documentation)
  - [Testing Fibonacci Calculation](#testing-fibonacci-calculation)
  - [Webhook Processing and Documentation Generation Example](#webhook-processing-and-documentation-generation-example)
- [API Reference](#api-reference)
  - [Module: `demo_new_module.py`](#module-demo_new_modulepy)
  - [Module: `main.py`](#module-mainpy)
  - [Module: `math_utils.py`](#module-math_utilspy)
  - [Module: `new_feature.py`](#module-new_featurepy)
  - [Module: `smart_webhook_feature.py`](#module-smart_webhook_featurepy)
  - [Module: `start_server.py`](#module-start_serverpy)
  - [Module: `test_feature.py`](#module-test_featurepy)
- [Contributing](#contributing)
- [License](#license)

---

## Features

*   **Automated Documentation Generation**: Generates documentation content, such as `README.md`, based on code analysis.
*   **Smart Webhook Integration**: Processes GitHub webhook payloads to detect relevant code changes.
*   **AI-Powered Code Analysis**: Analyzes code structure and identifies documentation needs.
*   **Real-time Updates**: Designed to trigger documentation updates automatically upon code changes pushed to a repository.
*   **Automatic Git Operations**: Includes functionality to `git add`, `git commit`, and `git push` changes.
*   **Server Startup**: Can start a FastAPI server using `uvicorn`.
*   **Utility Functions**: A collection of general-purpose mathematical, string, and calculation utility functions.
*   **Advanced Calculator**: Provides a set of basic and advanced arithmetic operations.

## Project Structure

The project is organized into several Python files, each serving a distinct purpose:

```
.
├── demo_new_module.py
├── main.py
├── math_utils.py
├── new_feature.py
├── smart_webhook_feature.py
├── start_server.py
└── test_feature.py
```

## Installation

To set up the project, you typically need to clone the repository and install dependencies.

```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
# Based on the code, `uvicorn` is required for `start_server.py`.
# Other standard libraries like `json`, `hashlib`, `datetime`, `typing`, `subprocess`, `os`, `time`, `sys`, `pathlib` are typically available with Python.
pip install uvicorn
```

_Note: The `smart_webhook_feature.py` module uses `hmac.compare_digest` but `import hmac` is not explicitly present in the provided code block for that file. If you encounter a `NameError` for `hmac`, you may need to add `import hmac` to `smart_webhook_feature.py`._

## Usage

This section describes how to interact with different parts of the system.

### Running the Demo

The `demo_new_module.py` file demonstrates a simple greeting function.

```bash
python demo_new_module.py
```

This will output:
```
Hello, AI Doc System!
```

### Utilizing Math and Utility Functions

The `main.py` module provides a variety of mathematical and utility functions. You can import and use them in your Python scripts:

```python
from main import sum, divide, is_palindrome, fibonacci, factorial

print(f"Sum: {sum(5, 3)}")
print(f"Division: {divide(10, 2)}")
print(f"Is 'level' a palindrome? {is_palindrome('level')}")
print(f"10th Fibonacci number: {fibonacci(10)}")
print(f"Factorial of 5: {factorial(5)}")
```

### Using the Advanced Calculator

The `new_feature.py` file defines an `advanced_calculator` and includes a `test_calculator` function.

```bash
python new_feature.py
```

This script attempts to test the operations within `advanced_calculator`:

```
Testing Advanced Calculator:
  5 + 3 = <AttributeError> ❌
  10 - 4 = <AttributeError> ❌
  7 * 6 = <AttributeError> ❌
  15 / 3 = <AttributeError> ❌
  2^8 = <AttributeError> ❌
  5! = <AttributeError> ❌
```
_Note: As implemented, the nested functions (`add`, `subtract`, etc.) within `advanced_calculator()` are not directly accessible as attributes of the `advanced_calculator` function itself. Therefore, `test_calculator()` will raise `AttributeError` when attempting to call them as `advanced_calculator.add()` etc._

### Starting the Server and Triggering Documentation

The `start_server.py` script automates Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

```bash
python start_server.py
```

This command will:
1.  Add all current changes to Git.
2.  Commit changes with an auto-generated timestamp message.
3.  Push the commit to the remote repository.
4.  Start a `uvicorn` server on `http://0.0.0.0:8000`. It also prints a webhook URL example `https://da3b21fd5fff.ngrok-free.app/webhook/git`, suggesting an external service for webhook reception.

Press `Ctrl+C` to stop the server.

### Testing Fibonacci Calculation

The `test_feature.py` module calculates Fibonacci numbers using dynamic programming and includes a test function.

```bash
python test_feature.py
```

This will run tests for `calculate_fibonacci`:
```
Testing Fibonacci function:
  fib(0) = 0 (expected 0) ✅ PASS
  fib(1) = 1 (expected 1) ✅ PASS
  fib(2) = 1 (expected 1) ✅ PASS
  fib(3) = 2 (expected 2) ✅ PASS
  fib(4) = 5 (expected 5) ❌ FAIL # Note: The test case expects 5 for fib(4), but fib(4) should be 3 (0,1,1,2,3).
  fib(5) = 8 (expected 8) ✅ PASS
  fib(6) = 13 (expected 13) ✅ PASS
  fib(7) = 21 (expected 21) ✅ PASS
  fib(8) = 34 (expected 34) ✅ PASS
```
_Note: There is an inconsistency in the `test_fibonacci` function, where `test_cases[4]` is `5`, but `calculate_fibonacci(4)` should return `3` for the 4th Fibonacci number (0-indexed: 0, 1, 1, 2, 3...)._

### Webhook Processing and Documentation Generation Example

The `smart_webhook_feature.py` module contains an example of how the `WebhookProcessor` and `DocumentationGenerator` classes can be used.

```bash
python smart_webhook_feature.py
```

This script will:
1.  Instantiate a `WebhookProcessor` with a dummy secret.
2.  Process an example GitHub webhook payload, demonstrating commit analysis and documentation update generation.
3.  Instantiate a `DocumentationGenerator`.
4.  Analyze the code structure of `smart_webhook_feature.py` and `main.py`.
5.  Generate a sample `README.md` content based on the analysis.

The output will be detailed JSON and generated README content:
```json
Webhook Processing Result:
{
  "status": "success",
  "repo_name": "demoo",
  "commit_hash": "abc123def456",
  "analysis": {
    "has_relevant_changes": true,
    "relevant_files": [
      "smart_webhook_feature.py",
      "main.py"
    ],
    "total_changes": 2,
    "analysis_timestamp": "..."
  },
  "documentation_update": {
    "repo_name": "demoo",
    "commit_hash": "abc123def456",
    "update_type": "automatic",
    "generated_at": "...",
    "status": "pending",
    "files_updated": [
      "README.md"
    ],
    "ai_analysis": "Changes detected in core functionality requiring documentation update",
    "ai_confidence": 0.85,
    "estimated_quality": "high"
  },
  "processed_at": "..."
}

Code Structure Analysis:
{
  "total_files": 2,
  "file_types": {
    "python": 2
  },
  "complexity_score": 4,
  "documentation_needs": [
    "function_documentation"
  ]
}

Generated README Content:
# demoo

## Overview
This repository contains a 2-file project with mixed technology stack.

## Technology Stack
- Python: 2 files

## Complexity Score: 4/10

## Documentation Needs
- Function Documentation

## Installation
```bash
# Clone the repository
git clone <repository-url>
cd <repository-name>

# Install dependencies
# Add installation instructions here
```

## Usage
```python
# Add usage examples here
```

## Features
- Automated documentation generation
- Smart webhook integration
- AI-powered code analysis
- Real-time updates

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License
MIT License - see LICENSE file for details

---
*This documentation was automatically generated by the AI Documentation System.*
```

## API Reference

This section details the functions and classes available in each module.

### Module: `demo_new_module.py`

A simple module demonstrating a greeting function.

#### Functions

*   `greet(name: str) -> str`
    *   Returns a greeting message for the given `name`.
*   `run_demo() -> None`
    *   Prints a greeting using the `greet` function with the name "AI Doc System".

### Module: `main.py`

A collection of basic mathematical, calculation, and string utility functions.

#### Functions

*   `sum(a, b)`
    *   Adds two numbers together.
*   `sub(a, b)`
    *   Subtracts `b` from `a`.
*   `multiply(a, b)`
    *   Multiplies two numbers together.
*   `divide(a, b)`
    *   Divides `a` by `b` with a zero check.
    *   **Raises**: `ValueError` if `b` is 0.
*   `calculate_tax(income: float) -> float`
    *   Calculates tax on `income` at a 10% rate.
*   `calculate_discount(price: float, discount_percent: float) -> float`
    *   Calculates the discount amount on a `price`.
    *   **Raises**: `ValueError` if `discount_percent` is not between 0 and 100.
*   `average(a: float, b: float) -> float`
    *   Returns the average of two numbers.
*   `max_of_two(a: float, b: float) -> float`
    *   Returns the larger of two numbers.
*   `is_palindrome(text: str) -> bool`
    *   Checks if a string is a palindrome (reads the same forwards and backwards).
    *   Removes non-alphanumeric characters and converts to lowercase for comparison.
    *   **Args**:
        *   `text` (str): The string to check.
    *   **Returns**:
        *   `bool`: `True` if the string is a palindrome, `False` otherwise.
*   `fibonacci(n: int) -> int`
    *   Calculates the `nth` Fibonacci number using iteration (0-indexed).
    *   **Args**:
        *   `n` (int): The position in the Fibonacci sequence.
    *   **Returns**:
        *   `int`: The `nth` Fibonacci number.
    *   **Raises**: `ValueError` if `n` is negative.
*   `factorial(n: int) -> int`
    *   Calculates the factorial of a non-negative integer.
    *   **Args**:
        *   `n` (int): A non-negative integer.
    *   **Returns**:
        *   `int`: The factorial of `n`.
    *   **Raises**: `ValueError` if `n` is negative.

### Module: `math_utils.py`

Provides basic mathematical utility functions.

#### Functions

*   `multiply(a, b)`
    *   Multiplies two numbers together.
*   `divide(a, b)`
    *   Divides two numbers.
    *   **Raises**: `ValueError` if `b` is 0.
*   `power(base, exponent)`
    *   Calculates `base` raised to the power of `exponent`.

### Module: `new_feature.py`

Defines an advanced calculator function that encapsulates various arithmetic operations.

#### Functions

*   `advanced_calculator()`
    *   An "Advanced calculator with multiple operations." This function defines several nested helper functions for arithmetic operations:
        *   `add(a, b)`: Returns the sum of `a` and `b`.
        *   `subtract(a, b)`: Returns the difference of `a` and `b`.
        *   `multiply(a, b)`: Returns the product of `a` and `b`.
        *   `divide(a, b)`: Returns the quotient of `a` and `b`. Returns "Error: Division by zero" if `b` is 0.
        *   `modulo(a, b)`: Returns the remainder of `a` divided by `b`. Returns "Error: Modulo by zero" if `b` is 0.
        *   `power(base, exponent)`: Calculates `base` raised to the `exponent` power using a loop.
        *   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n` is negative.
*   `test_calculator()`
    *   Attempts to test the operations defined within `advanced_calculator`. Prints test results for addition, subtraction, multiplication, division, power, and factorial.

### Module: `smart_webhook_feature.py`

The core module for the Smart Webhook Feature, handling webhook processing and AI-driven documentation generation.

#### Classes

*   `WebhookProcessor(webhook_secret: str)`
    *   Processes GitHub webhooks for automatic documentation updates.
    *   **Constructor**:
        *   `webhook_secret` (str): The secret key used to verify webhook signatures.
    *   **Methods**:
        *   `verify_webhook_signature(payload: str, signature: str) -> bool`
            *   Verifies GitHub webhook signature for security.
            *   **Args**:
                *   `payload` (str): The webhook payload body.
                *   `signature` (str): The `X-Hub-Signature-256` header.
            *   **Returns**: `True` if signature is valid, `False` otherwise.
        *   `analyze_commit_changes(commit_data: Dict[str, Any]) -> Dict[str, Any]`
            *   Analyzes commit changes to determine if a documentation update is needed. Checks for changes in files with extensions `.py`, `.js`, `.ts`, `.java`, `.html`, `.css`, `.md`.
            *   **Args**:
                *   `commit_data` (Dict[str, Any]): GitHub commit information.
            *   **Returns**: Analysis results with change detection, including `has_relevant_changes`, `relevant_files`, `total_changes`, and `analysis_timestamp`.
        *   `generate_documentation_update(repo_name: str, commit_hash: str) -> Dict[str, Any]`
            *   Generates documentation update information for a repository. Simulates AI processing by adding `ai_confidence` and `estimated_quality`.
            *   **Args**:
                *   `repo_name` (str): Name of the repository.
                *   `commit_hash` (str): Git commit hash.
            *   **Returns**: Documentation update information, including status, files updated, and AI analysis.
        *   `process_webhook_payload(payload: Dict[str, Any]) -> Dict[str, Any]`
            *   Processes incoming webhook payload and coordinates documentation updates.
            *   **Args**:
                *   `payload` (Dict[str, Any]): GitHub webhook payload.
            *   **Returns**: Processing results, including repository/commit info, analysis, and documentation update details.
*   `DocumentationGenerator(ai_model: str = "gemini-2.5-flash")`
    *   Generates documentation using AI analysis.
    *   **Constructor**:
        *   `ai_model` (str): The name of the AI model to use (default: "gemini-2.5-flash").
    *   **Methods**:
        *   `analyze_code_structure(file_paths: list) -> Dict[str, Any]`
            *   Analyzes code structure (file types, complexity, documentation needs) for documentation generation.
            *   **Args**:
                *   `file_paths` (list): List of code file paths.
            *   **Returns**: Code structure analysis.
        *   `generate_readme_content(repo_name: str, structure: Dict[str, Any]) -> str`
            *   Generates `README.md` content based on code structure analysis. Includes sections for Overview, Technology Stack, Complexity Score, Documentation Needs, Installation, Usage, Features, Contributing, and License.
            *   **Args**:
                *   `repo_name` (str): Repository name.
                *   `structure` (Dict[str, Any]): Code structure analysis.
            *   **Returns**: Generated `README` content as a string.

### Module: `start_server.py`

A script to automate Git operations and start a FastAPI server.

#### Functions

*   `run_command(cmd, cwd=None)`
    *   Runs a shell command and captures its output.
    *   **Args**:
        *   `cmd` (str): The command to run.
        *   `cwd` (str, optional): The current working directory for the command.
    *   **Returns**: `True` if the command succeeds, `False` otherwise.
*   `main()`
    *   Main function to handle the workflow:
        1.  Changes directory to the project's root.
        2.  Adds all current changes to Git (`git add .`).
        3.  Commits changes with an automatic message (`git commit -m "Auto-update documentation - <timestamp>"`).
        4.  Pushes changes to the remote repository (`git push`).
        5.  Changes directory back to the project root.
        6.  Starts a `uvicorn` server to run `backend.app:app` (requires `uvicorn` to be installed), on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.

### Module: `test_feature.py`

Provides a function to calculate Fibonacci numbers using dynamic programming and a test suite for it.

#### Functions

*   `calculate_fibonacci(n)`
    *   Calculates the `nth` Fibonacci number using dynamic programming.
    *   **Args**:
        *   `n` (int): The position in the Fibonacci sequence.
    *   **Returns**:
        *   `int`: The `nth` Fibonacci number. Returns 0 for `n <= 0`, 1 for `n == 1` or `n == 2`.
*   `test_fibonacci()`
    *   Tests the `calculate_fibonacci` function against a predefined set of test cases. Prints whether each test case passes or fails.

## Contributing

1.  Fork the repository
2.  Create a feature branch
3.  Make your changes
4.  Submit a pull request

## License

MIT License - see LICENSE file for details

---
*This documentation was automatically generated by the AI Documentation System.*