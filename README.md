# AI-Powered Automated Documentation System

This project contains a collection of Python modules demonstrating various functionalities related to automated documentation, utility functions, and system automation. It showcases a smart webhook processing system for intelligent documentation updates, general-purpose mathematical and string manipulation utilities, and a script to automate Git operations and server startup.

## Modules Overview

The project is structured into several distinct Python files, each serving a specific purpose:

*   **`demo_new_module.py`**: A simple module demonstrating basic function definition and execution.
*   **`main.py`**: A comprehensive collection of utility functions covering arithmetic, finance, string manipulation, and mathematical sequences (Fibonacci, Factorial).
*   **`math_utils.py`**: Provides fundamental mathematical operations like multiplication, division, and exponentiation.
*   **`new_feature.py`**: Implements an "advanced calculator" defining multiple nested arithmetic and mathematical functions, along with a test runner.
*   **`smart_webhook_feature.py`**: The core module for the automated documentation system, featuring webhook processing, signature verification, commit analysis, and AI-driven documentation generation.
*   **`start_server.py`**: A utility script to perform automated Git add/commit/push operations and start a FastAPI server.
*   **`test_feature.py`**: Focuses on calculating Fibonacci numbers using dynamic programming and includes a dedicated test function.

---

## Module Documentation

### `demo_new_module.py`

This module provides a basic greeting function and a simple demo runner.

#### Functions

*   **`greet(name: str) -> str`**
    *   Returns a personalized greeting message.
    *   **Parameters:**
        *   `name` (`str`): The name to be greeted.
    *   **Returns:**
        *   `str`: A string in the format "Hello, {name}!".
*   **`run_demo() -> None`**
    *   Executes a demonstration of the `greet` function by printing a greeting to "AI Doc System".

---

### `main.py`

This module contains a variety of utility functions for general-purpose mathematical, financial, string, and sequence operations.

#### Functions

*   **`sum(a, b)`**
    *   Adds two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The sum of `a` and `b`.
*   **`sub(a, b)`**
    *   Subtracts `b` from `a`.
    *   **Parameters:**
        *   `a`: The number to subtract from.
        *   `b`: The number to subtract.
    *   **Returns:**
        *   The result of `a - b`.
*   **`multiply(a, b)`**
    *   Multiply two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The product of `a` and `b`.
*   **`divide(a, b)`**
    *   Divide `a` by `b` with zero check.
    *   **Parameters:**
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Returns:**
        *   The result of `a / b`.
    *   **Raises:**
        *   `ValueError`: If `b` is 0.
*   **`calculate_tax(income: float) -> float`**
    *   Calculate tax on income at 10% rate.
    *   **Parameters:**
        *   `income` (`float`): The income amount.
    *   **Returns:**
        *   `float`: The calculated tax amount.
*   **`calculate_discount(price: float, discount_percent: float) -> float`**
    *   Calculate discount amount on price.
    *   **Parameters:**
        *   `price` (`float`): The original price.
        *   `discount_percent` (`float`): The discount percentage (between 0 and 100).
    *   **Returns:**
        *   `float`: The calculated discount amount.
    *   **Raises:**
        *   `ValueError`: If `discount_percent` is not between 0 and 100.
*   **`average(a: float, b: float) -> float`**
    *   Return the average of two numbers.
    *   **Parameters:**
        *   `a` (`float`): The first number.
        *   `b` (`float`): The second number.
    *   **Returns:**
        *   `float`: The average of `a` and `b`.
*   **`max_of_two(a: float, b: float) -> float`**
    *   Return the larger of two numbers.
    *   **Parameters:**
        *   `a` (`float`): The first number.
        *   `b` (`float`): The second number.
    *   **Returns:**
        *   `float`: The larger of `a` and `b`.
*   **`is_palindrome(text: str) -> bool`**
    *   Check if a string is a palindrome (reads the same forwards and backwards).
    *   **Parameters:**
        *   `text` (`str`): The string to check.
    *   **Returns:**
        *   `bool`: `True` if the string is a palindrome, `False` otherwise.
    *   **Examples:**
        ```python
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome("A man a plan a canal Panama")
        True
        ```
*   **`fibonacci(n: int) -> int`**
    *   Calculate the nth Fibonacci number using iteration.
    *   **Parameters:**
        *   `n` (`int`): The position in the Fibonacci sequence (0-indexed).
    *   **Returns:**
        *   `int`: The nth Fibonacci number.
    *   **Raises:**
        *   `ValueError`: If `n` is negative.
    *   **Examples:**
        ```python
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        ```
*   **`factorial(n: int) -> int`**
    *   Calculate the factorial of a non-negative integer.
    *   **Parameters:**
        *   `n` (`int`): A non-negative integer.
    *   **Returns:**
        *   `int`: The factorial of `n`.
    *   **Raises:**
        *   `ValueError`: If `n` is negative.
    *   **Examples:**
        ```python
        >>> factorial(0)
        1
        >>> factorial(5)
        120
        >>> factorial(10)
        3628800
        ```

---

### `math_utils.py`

This module provides basic mathematical utilities for common operations.

#### Module Docstring

```
Math utilities for basic operations
```

#### Functions

*   **`multiply(a, b)`**
    *   Multiply two numbers together.
    *   **Parameters:**
        *   `a`: The first number.
        *   `b`: The second number.
    *   **Returns:**
        *   The product of `a` and `b`.
*   **`divide(a, b)`**
    *   Divide two numbers.
    *   **Parameters:**
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Returns:**
        *   The result of `a / b`.
    *   **Raises:**
        *   `ValueError`: If `b` is 0.
*   **`power(base, exponent)`**
    *   Calculate base raised to the power of exponent.
    *   **Parameters:**
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns:**
        *   The result of `base ** exponent`.

---

### `new_feature.py`

This module defines an "advanced calculator" function that encapsulates multiple arithmetic and mathematical operations as nested functions, and includes a testing utility.

#### Functions

*   **`advanced_calculator()`**
    *   Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, division, modulo, power, and factorial.
    *   This function defines the following nested functions:
        *   **`add(a, b)`**: Returns the sum of `a` and `b`.
        *   **`subtract(a, b)`**: Returns the result of `a - b`.
        *   **`multiply(a, b)`**: Returns the product of `a` and `b`.
        *   **`divide(a, b)`**: Returns the result of `a / b`. If `b` is 0, returns the string "Error: Division by zero".
        *   **`modulo(a, b)`**: Returns the remainder of `a % b`. If `b` is 0, returns the string "Error: Modulo by zero".
        *   **`power(base, exponent)`**: Calculates `base` raised to `exponent` using iteration.
        *   **`factorial(n)`**: Calculates the factorial of `n`. If `n` is negative, returns "Error: Negative number". If `n` is 0, returns 1.
*   **`test_calculator()`**
    *   Tests the operations defined within `advanced_calculator`. It attempts to call the nested functions as attributes of `advanced_calculator` (e.g., `advanced_calculator.add(5, 3)`), printing the results and indicating pass/fail for various test cases.

---

### `smart_webhook_feature.py`

This module implements a Smart Webhook Feature for processing GitHub webhooks to trigger automatic documentation updates. It includes classes for webhook processing and AI-driven documentation generation.

#### Module Docstring

```
Smart Webhook Feature Module
This module demonstrates the webhook-based documentation system functionality.
```

#### Classes

*   **`WebhookProcessor`**
    *   Processes GitHub webhooks for automatic documentation updates.
    *   **`__init__(self, webhook_secret: str)`**
        *   Initializes the `WebhookProcessor` instance.
        *   **Parameters:**
            *   `webhook_secret` (`str`): The secret used to verify webhook signatures.
    *   **`verify_webhook_signature(self, payload: str, signature: str) -> bool`**
        *   Verifies GitHub webhook signature for security using `sha256` hashing and `hmac.compare_digest`.
        *   **Parameters:**
            *   `payload` (`str`): The webhook payload body.
            *   `signature` (`str`): The `X-Hub-Signature-256` header value.
        *   **Returns:**
            *   `bool`: `True` if the signature is valid, `False` otherwise.
        *   **Note:** This method uses `hmac.compare_digest`, implying a dependency on the `hmac` module, which is not explicitly imported in the provided code snippet.
    *   **`analyze_commit_changes(self, commit_data: Dict[str, Any]) -> Dict[str, Any]`**
        *   Analyzes commit changes to determine if a documentation update is needed. It checks for changes in files with common code extensions (`.py`, `.js`, `.ts`, `.java`, `.html`, `.css`, `.md`).
        *   **Parameters:**
            *   `commit_data` (`Dict[str, Any]`): GitHub commit information (e.g., containing 'added', 'modified', 'removed' file lists).
        *   **Returns:**
            *   `Dict[str, Any]`: Analysis results including `has_relevant_changes`, `relevant_files`, `total_changes`, and `analysis_timestamp`.
    *   **`generate_documentation_update(self, repo_name: str, commit_hash: str) -> Dict[str, Any]`**
        *   Generates a simulated documentation update for a repository.
        *   **Parameters:**
            *   `repo_name` (`str`): Name of the repository.
            *   `commit_hash` (`str`): Git commit hash.
        *   **Returns:**
            *   `Dict[str, Any]`: Documentation update information, including simulated AI analysis results like `ai_confidence` and `estimated_quality`.
    *   **`process_webhook_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]`**
        *   Processes an incoming webhook payload to coordinate documentation updates. It extracts repository and commit information, analyzes changes, and generates a documentation update if relevant changes are found.
        *   **Parameters:**
            *   `payload` (`Dict[str, Any]`): GitHub webhook payload.
        *   **Returns:**
            *   `Dict[str, Any]`: Processing results including status, repository/commit info, analysis, and documentation update details.
*   **`DocumentationGenerator`**
    *   Generates documentation using AI analysis.
    *   **`__init__(self, ai_model: str = "gemini-2.5-flash")`**
        *   Initializes the `DocumentationGenerator` with an AI model name.
        *   **Parameters:**
            *   `ai_model` (`str`, optional): The name of the AI model to use (default: "gemini-2.5-flash").
    *   **`analyze_code_structure(self, file_paths: list) -> Dict[str, Any]`**
        *   Analyzes the structure of code files to inform documentation generation. It categorizes file types, calculates a complexity score, and identifies documentation needs.
        *   **Parameters:**
            *   `file_paths` (`list`): List of code file paths.
        *   **Returns:**
            *   `Dict[str, Any]`: Code structure analysis including `total_files`, `file_types`, `complexity_score`, and `documentation_needs`.
    *   **`generate_readme_content(self, repo_name: str, structure: Dict[str, Any]) -> str`**
        *   Generates `README.md` content based on the provided repository name and code structure analysis. It includes sections for overview, technology stack, complexity, documentation needs, installation, usage, features, contributing, and license.
        *   **Parameters:**
            *   `repo_name` (`str`): Repository name.
            *   `structure` (`Dict[str, Any]`): Code structure analysis data from `analyze_code_structure`.
        *   **Returns:**
            *   `str`: The generated Markdown content for `README.md`.

---

### `start_server.py`

This script automates a sequence of Git operations (add, commit, push) and then starts a FastAPI server using `uvicorn`.

#### Module Docstring

```
Start server with single automatic git push
```

#### Functions

*   **`run_command(cmd, cwd=None)`**
    *   Runs a shell command and returns the result. It captures standard output and error, and prints messages regarding success or failure.
    *   **Parameters:**
        *   `cmd` (`str`): The command string to execute.
        *   `cwd` (`str`, optional): The current working directory for the command.
    *   **Returns:**
        *   `bool`: `True` if the command executed successfully (return code 0), `False` otherwise.
*   **`main()`**
    *   The main function to orchestrate the Git operations and server startup.
    *   It identifies the project root and current script directory.
    *   **Git Operations:**
        1.  Changes directory to the demoo directory.
        2.  Adds all current changes to Git (`git add .`).
        3.  Commits changes with an auto-generated timestamp message (`git commit -m "Auto-update documentation - YYYY-MM-DD HH:MM:SS"`).
        4.  Pushes committed changes to the remote repository (`git push`).
    *   **Server Startup:**
        1.  Changes directory back to the project root.
        2.  Starts a `uvicorn` server for `backend.app:app` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
        3.  Prints the server URL (`http://localhost:8000`) and a sample webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
        4.  Handles `KeyboardInterrupt` to gracefully stop the server.
    *   **Returns:**
        *   `bool`: `True` if the process completes without critical errors, `False` otherwise.
    *   **Dependencies:** Uses `uvicorn` which is imported dynamically within this function, implying it must be installed in the environment.

---

### `test_feature.py`

This module provides a function to calculate Fibonacci numbers using dynamic programming and a testing utility for it.

#### Functions

*   **`calculate_fibonacci(n)`**
    *   Calculate the nth Fibonacci number using dynamic programming.
    *   **Parameters:**
        *   `n` (`int`): The position in the Fibonacci sequence.
    *   **Returns:**
        *   `int`: The nth Fibonacci number.
    *   **Logic:**
        *   Returns 0 for `n <= 0`.
        *   Returns 1 for `n = 1` or `n = 2`.
        *   Initializes a DP table `fib` and iteratively fills it up to `n`.
*   **`test_fibonacci()`**
    *   Tests the `calculate_fibonacci` function against a predefined set of test cases (0, 1, 2, 3, 5, 8, 13, 21, 34 corresponding to fib(0) through fib(8)). It prints the calculated result versus the expected result and indicates pass/fail.

---

## Getting Started

To get started with this project, you'll need Python 3 installed.

### Installation

The project uses several external Python libraries. You can install them using pip:

```bash
# Required for running the server and processing webhooks
pip install uvicorn
pip install python-dotenv # Often used with uvicorn applications, though not explicitly imported
```

The `smart_webhook_feature.py` module uses `json`, `hashlib`, `datetime`, and `typing`, which are part of Python's standard library. The `start_server.py` script uses `os`, `subprocess`, `time`, `sys`, and `pathlib`, also standard.

### Usage

Each module with an `if __name__ == "__main__":` block can be run directly to see its demonstration or tests.

#### Running Demos and Tests

*   **Greeting Demo:**
    ```bash
    python demo_new_module.py
    ```
*   **Advanced Calculator Tests:**
    ```bash
    python new_feature.py
    ```
*   **Webhook Feature Example:**
    ```bash
    python smart_webhook_feature.py
    ```
*   **Fibonacci Tests:**
    ```bash
    python test_feature.py
    ```

#### Starting the Server with Git Automation

The `start_server.py` script automates Git operations (add, commit, push) and then starts a local FastAPI server.

```bash
python start_server.py
```

This will perform the Git actions, then start the server at `http://localhost:8000`. It will also print a placeholder webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`) for reference.

## Features

The project, particularly through the `smart_webhook_feature.py` module, highlights the following capabilities:

*   **Automated documentation generation**: Generating `README.md` content based on code analysis.
*   **Smart webhook integration**: Processing GitHub webhook payloads to react to code changes.
*   **AI-powered code analysis**: Analyzing code structure to determine complexity and documentation needs.
*   **Real-time updates**: Facilitating dynamic documentation updates in response to repository activity.

## Contributing

To contribute to this project:

1.  Fork the repository
2.  Create a feature branch
3.  Make your changes
4.  Submit a pull request

## License

MIT License - see LICENSE file for details

---
*This documentation was automatically generated by the AI Documentation System.*