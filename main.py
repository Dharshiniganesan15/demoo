"""
Advanced Python Project - Multi-Module Application
A comprehensive Python project with various modules and features.
"""

from typing import List, Dict, Any, Union, Optional
import json
import csv
import os
import statistics
import re
from datetime import datetime
import hashlib
import random
import string
from pathlib import Path

# ============================================================================
# MATHEMATICAL OPERATIONS
# ============================================================================

class Calculator:
    """Advanced calculator with various mathematical operations."""
    
    def __init__(self):
        self.operations_log = []
    
    def add(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Add two numbers."""
        result = a + b
        self.operations_log.append(f"add({a}, {b}) = {result}")
        return result
    
    def subtract(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Subtract two numbers."""
        result = a - b
        self.operations_log.append(f"subtract({a}, {b}) = {result}")
        return result
    
    def multiply(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Multiply two numbers."""
        result = a * b
        self.operations_log.append(f"multiply({a}, {b}) = {result}")
        return result
    
    def divide(self, a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.operations_log.append(f"divide({a}, {b}) = {result}")
        return result
    
    def power(self, base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
        """Calculate power."""
        result = base ** exponent
        self.operations_log.append(f"power({base}, {exponent}) = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calculate factorial."""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1
        for i in range(1, n + 1):
            result *= i
        self.operations_log.append(f"factorial({n}) = {result}")
        return result
    
    def find_min(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Find minimum value in a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        result = min(numbers)
        self.operations_log.append(f"find_min({numbers}) = {result}")
        return result
    
    def find_max(self, numbers: List[Union[int, float]]) -> Union[int, float]:
        """Find maximum value in a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        result = max(numbers)
        self.operations_log.append(f"find_max({numbers}) = {result}")
        return result
    
    def average(self, numbers: List[Union[int, float]]) -> float:
        """Calculate average of a list."""
        if not numbers:
            raise ValueError("List cannot be empty")
        result = sum(numbers) / len(numbers)
        self.operations_log.append(f"average({numbers}) = {result}")
        return result
    
    def get_operations_log(self) -> List[str]:
        """Get operations log."""
        return self.operations_log

# ============================================================================
# STRING PROCESSING
# ============================================================================

class StringProcessor:
    """Advanced string processor with various text operations."""
    
    def reverse_string(self, text: str) -> str:
        """Reverse a string."""
        return text[::-1]
    
    def to_uppercase(self, text: str) -> str:
        """Convert string to uppercase."""
        return text.upper()
    
    def to_lowercase(self, text: str) -> str:
        """Convert string to lowercase."""
        return text.lower()
    
    def to_title_case(self, text: str) -> str:
        """Convert string to title case."""
        return text.title()
    
    def count_words(self, text: str) -> int:
        """Count words in a string."""
        return len(text.split())
    
    def count_characters(self, text: str, include_spaces: bool = True) -> int:
        """Count characters in a string."""
        if include_spaces:
            return len(text)
        else:
            return len(text.replace(' ', ''))
    
    def is_palindrome(self, text: str) -> bool:
        """Check if string is a palindrome."""
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        return cleaned == cleaned[::-1]
    
    def extract_numbers(self, text: str) -> List[float]:
        """Extract all numbers from text."""
        return [float(num) for num in re.findall(r'-?\d+\.?\d*', text)]
    
    def extract_emails(self, text: str) -> List[str]:
        """Extract all email addresses from text."""
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_pattern, text)
    
    def extract_urls(self, text: str) -> List[str]:
        """Extract all URLs from text."""
        url_pattern = r'https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?'
        return re.findall(url_pattern, text)
    
    def remove_special_characters(self, text: str) -> str:
        """Remove special characters from string."""
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
    
    def truncate_string(self, text: str, max_length: int, suffix: str = '...') -> str:
        """Truncate string to maximum length."""
        if len(text) <= max_length:
            return text
        return text[:max_length - len(suffix)] + suffix

# ============================================================================
# DATA ANALYSIS
# ============================================================================

class DataAnalyzer:
    """Advanced data analyzer with statistical operations."""
    
    def basic_stats(self, data: List[Union[int, float]]) -> Dict[str, Union[int, float]]:
        """Calculate basic statistics for a dataset."""
        if not data:
            raise ValueError("Data list cannot be empty")
        
        return {
            'count': len(data),
            'sum': sum(data),
            'mean': statistics.mean(data),
            'median': statistics.median(data),
            'min': min(data),
            'max': max(data),
            'range': max(data) - min(data),
            'std_dev': statistics.stdev(data) if len(data) > 1 else 0,
            'variance': statistics.variance(data) if len(data) > 1 else 0
        }
    
    def correlation(self, x: List[Union[int, float]], y: List[Union[int, float]]) -> float:
        """Calculate correlation coefficient between two datasets."""
        if len(x) != len(y):
            raise ValueError("Datasets must have the same length")
        if len(x) < 2:
            raise ValueError("Datasets must have at least 2 elements")
        return statistics.correlation(x, y)
    
    def percentile(self, data: List[Union[int, float]], percentile: float) -> float:
        """Calculate percentile of data."""
        if not data:
            raise ValueError("Data list cannot be empty")
        if not 0 <= percentile <= 100:
            raise ValueError("Percentile must be between 0 and 100")
        return statistics.quantiles(data, n=100)[int(percentile) - 1]
    
    def frequency_distribution(self, data: List[Union[int, float]]) -> Dict[Union[int, float], int]:
        """Calculate frequency distribution of data."""
        if not data:
            raise ValueError("Data list cannot be empty")
        
        freq = {}
        for item in data:
            freq[item] = freq.get(item, 0) + 1
        return dict(sorted(freq.items()))

# ============================================================================
# FILE OPERATIONS
# ============================================================================

class FileManager:
    """File manager for various file operations."""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)
    
    def read_text_file(self, filename: str) -> str:
        """Read text content from file."""
        file_path = self.base_path / filename
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    
    def write_text_file(self, filename: str, content: str, mode: str = 'w') -> None:
        """Write text content to file."""
        file_path = self.base_path / filename
        with open(file_path, mode, encoding='utf-8') as file:
            file.write(content)
    
    def read_json_file(self, filename: str) -> Dict[str, Any]:
        """Read JSON data from file."""
        file_path = self.base_path / filename
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    
    def write_json_file(self, filename: str, data: Dict[str, Any], indent: int = 2) -> None:
        """Write JSON data to file."""
        file_path = self.base_path / filename
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=indent)
    
    def read_csv_file(self, filename: str, delimiter: str = ',') -> List[Dict[str, str]]:
        """Read CSV data from file."""
        file_path = self.base_path / filename
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=delimiter)
            return list(reader)
    
    def write_csv_file(self, filename: str, data: List[Dict[str, str]], fieldnames: Optional[List[str]] = None, delimiter: str = ',') -> None:
        """Write CSV data to file."""
        file_path = self.base_path / filename
        with open(file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames or data[0].keys(), delimiter=delimiter)
            writer.writeheader()
            writer.writerows(data)
    
    def list_files(self, extension: Optional[str] = None) -> List[str]:
        """List files in directory with optional extension filter."""
        files = []
        for item in self.base_path.iterdir():
            if item.is_file():
                if extension is None or item.suffix.lower() == extension.lower():
                    files.append(item.name)
        return files

# ============================================================================
# CRYPTOGRAPHY UTILITIES
# ============================================================================

class CryptoUtils:
    """Cryptography utilities for hashing and encoding."""
    
    @staticmethod
    def generate_hash(text: str, algorithm: str = 'sha256') -> str:
        """Generate hash of text using specified algorithm."""
        if algorithm.lower() == 'md5':
            return hashlib.md5(text.encode()).hexdigest()
        elif algorithm.lower() == 'sha1':
            return hashlib.sha1(text.encode()).hexdigest()
        elif algorithm.lower() == 'sha256':
            return hashlib.sha256(text.encode()).hexdigest()
        else:
            raise ValueError(f"Unsupported algorithm: {algorithm}")
    
    @staticmethod
    def generate_random_string(length: int = 10, include_digits: bool = True, include_uppercase: bool = True, include_lowercase: bool = True) -> str:
        """Generate random string."""
        characters = ""
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_digits:
            characters += string.digits
        
        return ''.join(random.choice(characters) for _ in range(length))
    
    @staticmethod
    def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
        """Apply Caesar cipher to text."""
        if decrypt:
            shift = -shift
        
        result = ""
        for char in text:
            if char.isalpha():
                start = ord('a') if char.islower() else ord('A')
                shifted = (ord(char) - start + shift) % 26 + start
                result += chr(shifted)
            else:
                result += char
        return result

# ============================================================================
# VALIDATION UTILITIES
# ============================================================================

class Validator:
    """Validation utilities for various data types."""
    
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate email address."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def is_valid_phone(phone: str) -> bool:
        """Validate phone number (basic validation)."""
        pattern = r'^[\d\s\-\(\)]+$'
        return re.match(pattern, phone) is not None
    
    @staticmethod
    def is_valid_url(url: str) -> bool:
        """Validate URL."""
        pattern = r'^https?://(?:[-\w.])+(?:[:\d]+)?(?:/(?:[\w/_.])*(?:\?(?:[\w&=%.])*)?(?:#(?:[\w.])*)?'
        return re.match(pattern, url) is not None
    
    @staticmethod
    def is_strong_password(password: str) -> bool:
        """Check if password meets strength requirements."""
        return (
            len(password) >= 8 and
            any(c.isupper() for c in password) and
            any(c.islower() for c in password) and
            any(c.isdigit() for c in password) and
            any(c in '!@#$%^&*()_+-=[]{}|;:<>?,./' for c in password)
        )

# ============================================================================
# MAIN DEMO FUNCTION
# ============================================================================

def demo_advanced_project():
    """Demonstrate all features of the advanced project."""
    print("=" * 60)
    print("ADVANCED PYTHON PROJECT DEMO")
    print("=" * 60)
    
    # Calculator Demo
    print("\n🔢 CALCULATOR DEMO")
    print("-" * 30)
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    print(f"2^8 = {calc.power(2, 8)}")
    print(f"5! = {calc.factorial(5)}")
    
    numbers = [1, 5, 3, 9, 7, 2, 8, 4, 6]
    print(f"Min of {numbers} = {calc.find_min(numbers)}")
    print(f"Max of {numbers} = {calc.find_max(numbers)}")
    print(f"Average of {numbers} = {calc.average(numbers):.2f}")
    
    # String Processor Demo
    print("\n📝 STRING PROCESSOR DEMO")
    print("-" * 30)
    processor = StringProcessor()
    text = "Hello World! This is a test string with 123 numbers and email@example.com"
    print(f"Original: {text}")
    print(f"Reversed: {processor.reverse_string(text)}")
    print(f"Uppercase: {processor.to_uppercase(text)}")
    print(f"Lowercase: {processor.to_lowercase(text)}")
    print(f"Title Case: {processor.to_title_case(text)}")
    print(f"Word Count: {processor.count_words(text)}")
    print(f"Character Count: {processor.count_characters(text)}")
    print(f"Is Palindrome: {processor.is_palindrome('madam')}")
    print(f"Extracted Numbers: {processor.extract_numbers(text)}")
    print(f"Extracted Emails: {processor.extract_emails(text)}")
    
    # Data Analyzer Demo
    print("\n📊 DATA ANALYZER DEMO")
    print("-" * 30)
    analyzer = DataAnalyzer()
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    stats = analyzer.basic_stats(data)
    print(f"Data: {data}")
    print(f"Statistics: {stats}")
    
    x_data = [1, 2, 3, 4, 5]
    y_data = [2, 4, 6, 8, 10]
    correlation = analyzer.correlation(x_data, y_data)
    print(f"Correlation between {x_data} and {y_data}: {correlation:.2f}")
    
    # File Manager Demo
    print("\n📁 FILE MANAGER DEMO")
    print("-" * 30)
    file_manager = FileManager("demo_files")
    
    # Create sample data
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    
    file_manager.write_json_file("sample_data.json", sample_data)
    file_manager.write_csv_file("sample_data.csv", sample_data)
    file_manager.write_text_file("sample.txt", "This is a sample text file.")
    
    print("Created files:")
    for file in file_manager.list_files():
        print(f"  - {file}")
    
    # Crypto Utils Demo
    print("\n🔐 CRYPTO UTILS DEMO")
    print("-" * 30)
    crypto = CryptoUtils()
    
    text = "Hello World"
    print(f"Original: {text}")
    print(f"MD5 Hash: {crypto.generate_hash(text, 'md5')}")
    print(f"SHA256 Hash: {crypto.generate_hash(text, 'sha256')}")
    print(f"Random String: {crypto.generate_random_string(12)}")
    print(f"Caesar Cipher (shift 3): {crypto.caesar_cipher(text, 3)}")
    print(f"Caesar Decipher (shift 3): {crypto.caesar_cipher(crypto.caesar_cipher(text, 3), 3, decrypt=True)}")
    
    # Validator Demo
    print("\n✅ VALIDATOR DEMO")
    print("-" * 30)
    validator = Validator()
    
    test_email = "user@example.com"
    test_phone = "123-456-7890"
    test_url = "https://www.example.com"
    test_password = "MySecurePass123!"
    
    print(f"Email '{test_email}' is valid: {validator.is_valid_email(test_email)}")
    print(f"Phone '{test_phone}' is valid: {validator.is_valid_phone(test_phone)}")
    print(f"URL '{test_url}' is valid: {validator.is_valid_url(test_url)}")
    print(f"Password 'MySecurePass123!' is strong: {validator.is_strong_password(test_password)}")
    
    print("\n" + "=" * 60)
    print("DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 60)

# ============================================================================
# SAMPLE FUNCTION FOR GEMINI TESTING
# ============================================================================

def calculate_simple_interest(principal: float, rate: float, time: float) -> float:
    """
    Calculate simple interest for a given principal, rate, and time period.
    
    Args:
        principal: The initial amount of money
        rate: The annual interest rate (as a decimal)
        time: The time period in years
        
    Returns:
        The calculated simple interest amount
        
    Example:
        >>> calculate_simple_interest(1000, 0.05, 2)
        100.0
    """
    return principal * rate * time

# ============================================================================
# MAIN EXECUTION
# ============================================================================

if __name__ == "__main__":
    demo_advanced_project()