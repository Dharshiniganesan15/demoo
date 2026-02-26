# AI-Powered Documentation System

## Overview
This repository contains a collection of Python modules demonstrating functionality for an AI-powered documentation system. Key aspects include automated documentation updates triggered by GitHub webhooks, AI analysis of code structure for README generation, and a suite of general-purpose utility functions. It also includes scripts for automated Git operations and starting a local server.

## Project Structure

The project is organized into several Python files, each serving a specific purpose:

*   `demo_new_module.py`: A simple demonstration module with basic greeting functionality.
*   `main.py`: A comprehensive collection of fundamental mathematical, financial, string manipulation, and sequence calculation utilities.
*   `math_utils.py`: Provides basic mathematical operations.
*   `new_feature.py`: Demonstrates an "advanced calculator" with nested functions and a self-contained testing mechanism.
*   `smart_webhook_feature.py`: The core module for webhook processing and AI-driven documentation generation.
*   `start_server.py`: A utility script to automate Git operations (add, commit, push) and start a FastAPI server.
*   `test_feature.py`: Contains a dynamic programming implementation for calculating Fibonacci numbers and a test function.

## Detailed Documentation

### Module: `demo_new_module.py`
This module provides a basic example of a Python script with a greeting function and a demo runner.

#### Functions

*   `greet(name: str) -> str`
    *   **Description**: Returns a personalized greeting string.
    *   **Parameters**:
        *   `name` (str): The name to greet.
    *   **Returns**: (str) A greeting message in the format "Hello, {name}!".
    *   **Example Usage**:
        ```python
        print(greet("AI Doc System")) # Output: Hello, AI Doc System!
        ```

*   `run_demo() -> None`
    *   **Description**: Executes a demonstration of the `greet` function by printing a greeting to "AI Doc System".
    *   **Parameters**: None
    *   **Returns**: None
    *   **Execution**: When the script is run directly, this function is called.

### Module: `main.py`
This module contains a diverse set of utility functions for common mathematical, financial, and string operations, along with examples for sequence generation.

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
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Returns**: The result of `a / b`.
    *   **Raises**: `ValueError` if `b` is 0.

*   `calculate_tax(income: float) -> float`
    *   **Description**: Calculate tax on income at a fixed 10% rate.
    *   **Parameters**:
        *   `income` (float): The income amount.
    *   **Returns**: (float) The calculated tax amount.

*   `calculate_discount(price: float, discount_percent: float) -> float`
    *   **Description**: Calculate the discount amount on a given price.
    *   **Parameters**:
        *   `price` (float): The original price.
        *   `discount_percent` (float): The discount percentage (0-100).
    *   **Returns**: (float) The calculated discount amount.
    *   **Raises**: `ValueError` if `discount_percent` is not between 0 and 100.

*   `average(a: float, b: float) -> float`
    *   **Description**: Return the average of two numbers.
    *   **Parameters**:
        *   `a` (float): The first number.
        *   `b` (float): The second number.
    *   **Returns**: (float) The average of `a` and `b`.

*   `max_of_two(a: float, b: float) -> float`
    *   **Description**: Return the larger of two numbers.
    *   **Parameters**:
        *   `a` (float): The first number.
        *   `b` (float): The second number.
    *   **Returns**: (float) The larger of `a` and `b`.

*   `is_palindrome(text: str) -> bool`
    *   **Description**: Check if a string is a palindrome (reads the same forwards and backwards).
    *   **Parameters**:
        *   `text` (str): The string to check.
    *   **Returns**: (bool) `True` if the string is a palindrome, `False` otherwise.
    *   **Examples**:
        ```python
        is_palindrome("racecar") # True
        is_palindrome("hello")   # False
        is_palindrome("A man a plan a canal Panama") # True
        ```

*   `fibonacci(n: int) -> int`
    *   **Description**: Calculate the nth Fibonacci number using iteration.
    *   **Parameters**:
        *   `n` (int): The position in the Fibonacci sequence (0-indexed).
    *   **Returns**: (int) The nth Fibonacci number.
    *   **Raises**: `ValueError` if `n` is negative.
    *   **Examples**:
        ```python
        fibonacci(0)  # 0
        fibonacci(1)  # 1
        fibonacci(10) # 55
        ```

*   `factorial(n: int) -> int`
    *   **Description**: Calculate the factorial of a non-negative integer.
    *   **Parameters**:
        *   `n` (int): A non-negative integer.
    *   **Returns**: (int) The factorial of `n`.
    *   **Raises**: `ValueError` if `n` is negative.
    *   **Examples**:
        ```python
        factorial(0)  # 1
        factorial(5)  # 120
        factorial(10) # 3628800
        ```

### Module: `math_utils.py`
This module provides basic mathematical operations.

#### Module Docstring
```
Math utilities for basic operations
```

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
        *   `a`: The dividend.
        *   `b`: The divisor.
    *   **Returns**: The result of `a / b`.
    *   **Raises**: `ValueError` if `b` is 0.

*   `power(base, exponent)`
    *   **Description**: Calculate `base` raised to the power of `exponent`.
    *   **Parameters**:
        *   `base`: The base number.
        *   `exponent`: The exponent.
    *   **Returns**: The result of `base ** exponent`.

### Module: `new_feature.py`
This module defines an `advanced_calculator` function which encapsulates several arithmetic operations as nested functions, and includes a `test_calculator` function to demonstrate their *intended* usage.

#### Functions

*   `advanced_calculator()`
    *   **Description**: Advanced calculator with multiple operations. Supports addition, subtraction, multiplication, and division.
    *   **Note**: This function defines several helper functions (`add`, `subtract`, `multiply`, `divide`, `modulo`, `power`, `factorial`) within its scope. These nested functions are not directly accessible from outside `advanced_calculator()` in standard Python execution unless `advanced_calculator()` were to return them (e.g., in a dictionary or class instance). The `test_calculator()` function *attempts* to call these as attributes of `advanced_calculator`, which would result in an `AttributeError` in the current implementation.

    *   **Nested Functions (as defined locally within `advanced_calculator`)**:
        *   `add(a, b)`: Returns `a + b`.
        *   `subtract(a, b)`: Returns `a - b`.
        *   `multiply(a, b)`: Returns `a * b`.
        *   `divide(a, b)`: Returns `a / b`. If `b` is 0, returns "Error: Division by zero".
        *   `modulo(a, b)`: Returns `a % b`. If `b` is 0, returns "Error: Modulo by zero".
        *   `power(base, exponent)`: Calculates `base` raised to `exponent` iteratively.
        *   `factorial(n)`: Calculates the factorial of `n`. Returns "Error: Negative number" if `n < 0`, returns 1 if `n == 0`.

*   `test_calculator()`
    *   **Description**: Attempts to test the `advanced_calculator`'s operations by directly accessing its nested functions as attributes (e.g., `advanced_calculator.add`).
    *   **Note**: As per the explanation above for `advanced_calculator()`, this function's attempts to call `advanced_calculator.add`, `advanced_calculator.subtract`, etc., will result in an `AttributeError` because `advanced_calculator` does not expose these as attributes in its current form. The provided code includes print statements indicating expected and actual results based on this assumed access pattern.
    *   **Execution**: When the script is run directly, this function is called.

### Module: `smart_webhook_feature.py`
This module implements the core functionality for a smart webhook-based documentation system. It includes classes for processing GitHub webhooks and for generating documentation based on code analysis.

#### Module Docstring
```
Smart Webhook Feature Module
This module demonstrates the webhook-based documentation system functionality.
```

#### Dependencies (explicitly imported)
*   `json`
*   `hashlib`
*   `datetime` from `datetime`
*   `Dict`, `Any`, `Optional` from `typing`

#### Classes

*   `class WebhookProcessor`
    *   **Description**: Processes GitHub webhooks for automatic documentation updates.
    *   `__init__(self, webhook_secret: str)`
        *   **Description**: Initializes the WebhookProcessor with a secret.
        *   **Parameters**:
            *   `webhook_secret` (str): The secret used to verify webhook signatures.
    *   `verify_webhook_signature(self, payload: str, signature: str) -> bool`
        *   **Description**: Verifies GitHub webhook signature for security.
        *   **Parameters**:
            *   `payload` (str): The webhook payload body.
            *   `signature` (str): The `X-Hub-Signature-256` header.
        *   **Returns**: (bool) `True` if the signature is valid, `False` otherwise.
        *   **Note**: This method attempts to use `hmac.compare_digest` but the `hmac` module is not explicitly imported in the provided code, which would lead to a `NameError` if this method were called.
    *   `analyze_commit_changes(self, commit_data: Dict[str, Any]) -> Dict[str, Any]`
        *   **Description**: Analyzes commit changes to determine if a documentation update is needed. It checks for changes in files with common code extensions (`.py`, `.js`, `.ts`, `.java`, `.html`, `.css`, `.md`).
        *   **Parameters**:
            *   `commit_data` (Dict[str, Any]): GitHub commit information (e.g., 'added', 'modified', 'removed' files).
        *   **Returns**: (Dict[str, Any]) Analysis results including `has_relevant_changes`, `relevant_files`, `total_changes`, and `analysis_timestamp`.
    *   `generate_documentation_update(self, repo_name: str, commit_hash: str) -> Dict[str, Any]`
        *   **Description**: Simulates generating documentation update information for a repository.
        *   **Parameters**:
            *   `repo_name` (str): Name of the repository.
            *   `commit_hash` (str): Git commit hash.
        *   **Returns**: (Dict[str, Any]) Documentation update details including repository name, commit hash, update type, generation timestamp, status, files updated, AI analysis, AI confidence, and estimated quality.
    *   `process_webhook_payload(self, payload: Dict[str, Any]) -> Dict[str, Any]`
        *   **Description**: Processes an incoming webhook payload to coordinate documentation updates. Extracts repository and commit info, analyzes changes, and triggers documentation generation if relevant changes are found.
        *   **Parameters**:
            *   `payload` (Dict[str, Any]): GitHub webhook payload.
        *   **Returns**: (Dict[str, Any]) Processing results including status, repository name, commit hash, analysis, documentation update information (if generated), and processing timestamp. Handles exceptions during processing.

*   `class DocumentationGenerator`
    *   **Description**: Generates documentation using AI analysis.
    *   `__init__(self, ai_model: str = "gemini-2.5-flash")`
        *   **Description**: Initializes the DocumentationGenerator with an AI model name.
        *   **Parameters**:
            *   `ai_model` (str): The name of the AI model to use (default: "gemini-2.5-flash").
    *   `analyze_code_structure(self, file_paths: list) -> Dict[str, Any]`
        *   **Description**: Analyzes the structure of code files to inform documentation generation. It categorizes files by type and assigns a simple complexity score.
        *   **Parameters**:
            *   `file_paths` (list): A list of code file paths to analyze.
        *   **Returns**: (Dict[str, Any]) Code structure analysis including total files, file types count, complexity score, and identified documentation needs.
    *   `generate_readme_content(self, repo_name: str, structure: Dict[str, Any]) -> str`
        *   **Description**: Generates content for a `README.md` file based on the repository name and the analyzed code structure.
        *   **Parameters**:
            *   `repo_name` (str): The name of the repository.
            *   `structure` (Dict[str, Any]): The code structure analysis results from `analyze_code_structure`.
        *   **Returns**: (str) The generated Markdown content for `README.md`, including sections for Overview, Technology Stack, Complexity Score, Documentation Needs, Installation, Usage, Features, Contributing, and License.

#### Example Usage (`if __name__ == "__main__":`)
The script demonstrates creating a `WebhookProcessor` and `DocumentationGenerator` instance, processing an example webhook payload, analyzing code structure, and generating README content.

### Module: `start_server.py`
This script automates the process of adding, committing, and pushing Git changes, and then starts a local FastAPI server using Uvicorn.

#### Module Docstring
```
Start server with single automatic git push
```

#### Dependencies (explicitly imported)
*   `os`
*   `subprocess`
*   `time`
*   `sys`
*   `Path` from `pathlib`
*   `uvicorn` (dynamically imported within `main()`)

#### Functions

*   `run_command(cmd, cwd=None)`
    *   **Description**: Runs a shell command and captures its output and errors.
    *   **Parameters**:
        *   `cmd` (str): The command string to execute.
        *   `cwd` (str, optional): The current working directory for the command. Defaults to `None`.
    *   **Returns**: (bool) `True` if the command executes successfully (return code 0), `False` otherwise. Prints command output and errors.

*   `main()`
    *   **Description**: The main function to perform Git operations and start the server.
        1.  **Git Add**: Adds all changes (`git add .`) in the script's directory.
        2.  **Git Commit**: Commits changes with an auto-generated timestamped message. Prints "No changes to commit" if the commit fails (e.g., no changes detected).
        3.  **Git Push**: Pushes committed changes to the remote repository. This is intended to be a single push.
        4.  **Start Server**: Changes directory to the project root and attempts to start a FastAPI server using `uvicorn`.
            *   It imports `uvicorn` dynamically.
            *   It configures Uvicorn to run `"backend.app:app"` on `0.0.0.0:8000` with `reload=True` and `log_level="info"`.
            *   **Note**: The `"backend.app:app"` path indicates an expectation of a `backend` package containing an `app.py` file with an `app` object (presumably a FastAPI application), which is not provided in the current set of files.
            *   Prints the expected server URL (`http://localhost:8000`) and a sample webhook URL (`https://da3b21fd5fff.ngrok-free.app/webhook/git`).
            *   Handles `KeyboardInterrupt` to gracefully stop the server.
    *   **Parameters**: None
    *   **Returns**: (bool) `True` if all operations (git and server start) are successful, `False` if any step fails.
    *   **Execution**: When the script is run directly, this function is called.

### Module: `test_feature.py`
This module provides an implementation for calculating Fibonacci numbers using dynamic programming and includes a dedicated test function.

#### Functions

*   `calculate_fibonacci(n)`
    *   **Description**: Calculate the nth Fibonacci number using dynamic programming.
    *   **Parameters**:
        *   `n` (int): The position in the Fibonacci sequence.
    *   **Returns**: (int) The nth Fibonacci number.
    *   **Logic**: Handles base cases `n <= 0`, `n == 1`, `n == 2`. For `n > 2`, it initializes a DP table `fib` and iteratively fills it using `fib[i] = fib[i-1] + fib[i-2]`.

*   `test_fibonacci()`
    *   **Description**: Tests the `calculate_fibonacci` function against a predefined set of test cases.
    *   **Parameters**: None
    *   **Returns**: None. Prints the results of each test case indicating PASS or FAIL.
    *   **Execution**: When the script is run directly, this function is called.

## Installation & Setup

This project uses Python. To get started:

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name> # Navigate to the project root
    ```

2.  **Install Python**: Ensure you have Python 3.x installed.

3.  **Install Dependencies**:
    The `start_server.py` script dynamically imports `uvicorn`, suggesting it's a runtime dependency for the server component.
    ```bash
    pip install uvicorn
    ```
    If you intend to run the `smart_webhook_feature.py` module and use the `verify_webhook_signature` method in `WebhookProcessor`, the `hmac` module would need to be imported at the top of that file. It is a standard library module so no `pip install` is needed, but an `import hmac` statement would be required.

## Usage

### Running Demo and Utility Scripts

Individual demonstration and utility scripts can be run directly:

*   **Demo Greeting**:
    ```bash
    python demo_new_module.py
    ```

*   **Core Utility Functions**:
    ```bash
    python main.py
    ```
    (Note: This file does not have a top-level execution block other than the comment, so running it directly will not produce output unless its functions are explicitly called in the `if __name__ == "__main__":` block, which is absent for `main.py`'s functions.)

*   **Advanced Calculator Test**:
    ```bash
    python new_feature.py
    ```
    (Note: This will output test results for the `advanced_calculator`'s nested functions, which as noted, would result in `AttributeError` in the current implementation.)

*   **Fibonacci Test**:
    ```bash
    python test_feature.py
    ```

### Starting the Server and Automating Git

The `start_server.py` script provides an integrated workflow for Git operations and server startup:

```bash
python start_server.py
```
This script will:
1.  Add all local changes to Git.
2.  Commit changes with an auto-generated message.
3.  Push changes to the remote Git repository *once*.
4.  Attempt to start a Uvicorn server, serving `backend.app:app` on `http://localhost:8000`.

**Note on Server**: The `start_server.py` script expects a `backend.app:app` to be present, which is not included in the provided code. If running `start_server.py` without this external component, the server startup will fail.

### Webhook and Documentation Generation Demo

The `smart_webhook_feature.py` module includes example usage when run directly:

```bash
python smart_webhook_feature.py
```
This will:
1.  Simulate processing an example GitHub webhook payload.
2.  Perform a code structure analysis on `smart_webhook_feature.py` and `main.py`.
3.  Generate a sample `README.md` content based on the analysis.

## Features

*   Automated documentation generation
*   Smart webhook integration for automatic updates
*   AI-powered code analysis to determine documentation needs
*   Git automation for seamless updates (add, commit, push)
*   Basic and advanced mathematical utility functions
*   String and sequence manipulation tools

## Contributing

1.  Fork the repository.
2.  Create a feature branch.
3.  Make your changes.
4.  Submit a pull request.

## License

MIT License - see LICENSE file for details (Note: A LICENSE file is not provided in the code, but this is indicated by the `generate_readme_content` function).

---
*This documentation was automatically generated by the AI Documentation System.*