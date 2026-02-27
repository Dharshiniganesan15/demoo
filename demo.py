"""
Demo Calculator - Advanced Mathematical Operations
This module demonstrates various calculator functions with comprehensive error handling.
"""

import math
import operator
from typing import Union, List, Tuple, Dict, Any
from dataclasses import dataclass
from enum import Enum

class OperationType(Enum):
    """Enumeration for supported calculator operations."""
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"
    POWER = "power"
    SQUARE_ROOT = "square_root"
    PERCENTAGE = "percentage"
    MODULO = "modulo"

@dataclass
class CalculationResult:
    """Data class for storing calculation results."""
    operation: str
    operand1: Union[float, int]
    operand2: Union[float, int, None]
    result: Union[float, int]
    success: bool
    error_message: str = None
    timestamp: str = None

class AdvancedCalculator:
    """
    Advanced calculator with comprehensive mathematical operations.
    Supports basic arithmetic, scientific calculations, and statistical functions.
    """
    
    def __init__(self):
        self.history: List[CalculationResult] = []
        self.operation_map = {
            OperationType.ADD: operator.add,
            OperationType.SUBTRACT: operator.sub,
            OperationType.MULTIPLY: operator.mul,
            OperationType.DIVIDE: operator.truediv,
            OperationType.POWER: operator.pow,
            OperationType.MODULO: operator.mod,
        }
    
    def add(self, a: Union[float, int], b: Union[float, int]) -> CalculationResult:
        """Add two numbers."""
        return self._perform_operation(OperationType.ADD, a, b)
    
    def subtract(self, a: Union[float, int], b: Union[float, int]) -> CalculationResult:
        """Subtract second number from first."""
        return self._perform_operation(OperationType.SUBTRACT, a, b)
    
    def multiply(self, a: Union[float, int], b: Union[float, int]) -> CalculationResult:
        """Multiply two numbers."""
        return self._perform_operation(OperationType.MULTIPLY, a, b)
    
    def divide(self, a: Union[float, int], b: Union[float, int]) -> CalculationResult:
        """Divide first number by second."""
        if b == 0:
            return CalculationResult(
                operation="divide",
                operand1=a,
                operand2=b,
                result=0,
                success=False,
                error_message="Division by zero is not allowed"
            )
        return self._perform_operation(OperationType.DIVIDE, a, b)
    
    def power(self, base: Union[float, int], exponent: Union[float, int]) -> CalculationResult:
        """Raise base to the power of exponent."""
        return self._perform_operation(OperationType.POWER, base, exponent)
    
    def square_root(self, number: Union[float, int]) -> CalculationResult:
        """Calculate square root of a number."""
        if number < 0:
            return CalculationResult(
                operation="square_root",
                operand1=number,
                operand2=None,
                result=0,
                success=False,
                error_message="Square root of negative number is not real"
            )
        
        result = math.sqrt(number)
        return CalculationResult(
            operation="square_root",
            operand1=number,
            operand2=None,
            result=result,
            success=True
        )
    
    def percentage(self, part: Union[float, int], whole: Union[float, int]) -> CalculationResult:
        """Calculate percentage of part relative to whole."""
        if whole == 0:
            return CalculationResult(
                operation="percentage",
                operand1=part,
                operand2=whole,
                result=0,
                success=False,
                error_message="Cannot calculate percentage with zero as whole"
            )
        
        result = (part / whole) * 100
        return CalculationResult(
            operation="percentage",
            operand1=part,
            operand2=whole,
            result=result,
            success=True
        )
    
    def modulo(self, a: Union[float, int], b: Union[float, int]) -> CalculationResult:
        """Calculate remainder of division."""
        if b == 0:
            return CalculationResult(
                operation="modulo",
                operand1=a,
                operand2=b,
                result=0,
                success=False,
                error_message="Modulo by zero is not allowed"
            )
        return self._perform_operation(OperationType.MODULO, a, b)
    
    def factorial(self, n: int) -> CalculationResult:
        """Calculate factorial of a non-negative integer."""
        if not isinstance(n, int) or n < 0:
            return CalculationResult(
                operation="factorial",
                operand1=n,
                operand2=None,
                result=0,
                success=False,
                error_message="Factorial is only defined for non-negative integers"
            )
        
        if n > 170:  # Prevent overflow
            return CalculationResult(
                operation="factorial",
                operand1=n,
                operand2=None,
                result=0,
                success=False,
                error_message="Factorial of numbers greater than 170 may cause overflow"
            )
        
        result = math.factorial(n)
        return CalculationResult(
            operation="factorial",
            operand1=n,
            operand2=None,
            result=result,
            success=True
        )
    
    def logarithm(self, number: Union[float, int], base: Union[float, int] = math.e) -> CalculationResult:
        """Calculate logarithm of a number with specified base (default: natural log)."""
        if number <= 0:
            return CalculationResult(
                operation="logarithm",
                operand1=number,
                operand2=base,
                result=0,
                success=False,
                error_message="Logarithm is only defined for positive numbers"
            )
        
        if base <= 0 or base == 1:
            return CalculationResult(
                operation="logarithm",
                operand1=number,
                operand2=base,
                result=0,
                success=False,
                error_message="Logarithm base must be positive and not equal to 1"
            )
        
        result = math.log(number, base)
        return CalculationResult(
            operation="logarithm",
            operand1=number,
            operand2=base,
            result=result,
            success=True
        )
    
    def sine(self, angle: Union[float, int], degrees: bool = True) -> CalculationResult:
        """Calculate sine of an angle."""
        angle_rad = math.radians(angle) if degrees else angle
        result = math.sin(angle_rad)
        return CalculationResult(
            operation="sine",
            operand1=angle,
            operand2=degrees,
            result=result,
            success=True
        )
    
    def cosine(self, angle: Union[float, int], degrees: bool = True) -> CalculationResult:
        """Calculate cosine of an angle."""
        angle_rad = math.radians(angle) if degrees else angle
        result = math.cos(angle_rad)
        return CalculationResult(
            operation="cosine",
            operand1=angle,
            operand2=degrees,
            result=result,
            success=True
        )
    
    def tangent(self, angle: Union[float, int], degrees: bool = True) -> CalculationResult:
        """Calculate tangent of an angle."""
        angle_rad = math.radians(angle) if degrees else angle
        
        # Check for undefined values (90°, 270°, etc.)
        if degrees and angle % 180 == 90:
            return CalculationResult(
                operation="tangent",
                operand1=angle,
                operand2=degrees,
                result=0,
                success=False,
                error_message=f"Tangent is undefined at {angle}°"
            )
        
        result = math.tan(angle_rad)
        return CalculationResult(
            operation="tangent",
            operand1=angle,
            operand2=degrees,
            result=result,
            success=True
        )
    
    def _perform_operation(self, operation: OperationType, a: Union[float, int], b: Union[float, int]) -> CalculationResult:
        """Perform basic arithmetic operation."""
        try:
            operation_func = self.operation_map.get(operation)
            if operation_func:
                result = operation_func(a, b)
                return CalculationResult(
                    operation=operation.value,
                    operand1=a,
                    operand2=b,
                    result=result,
                    success=True
                )
            else:
                return CalculationResult(
                    operation=operation.value,
                    operand1=a,
                    operand2=b,
                    result=0,
                    success=False,
                    error_message=f"Unsupported operation: {operation.value}"
                )
        except Exception as e:
            return CalculationResult(
                operation=operation.value,
                operand1=a,
                operand2=b,
                result=0,
                success=False,
                error_message=str(e)
            )
    
    def get_history(self) -> List[CalculationResult]:
        """Get calculation history."""
        return self.history.copy()
    
    def clear_history(self) -> None:
        """Clear calculation history."""
        self.history.clear()
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics about calculations performed."""
        if not self.history:
            return {
                'total_calculations': 0,
                'successful_calculations': 0,
                'failed_calculations': 0,
                'most_common_operation': None,
                'average_result': 0
            }
        
        successful = [calc for calc in self.history if calc.success]
        failed = [calc for calc in self.history if not calc.success]
        
        # Count operations
        operation_counts = {}
        for calc in self.history:
            operation_counts[calc.operation] = operation_counts.get(calc.operation, 0) + 1
        
        most_common = max(operation_counts, key=operation_counts.get) if operation_counts else None
        
        # Calculate average of successful results
        average_result = sum(calc.result for calc in successful) / len(successful) if successful else 0
        
        return {
            'total_calculations': len(self.history),
            'successful_calculations': len(successful),
            'failed_calculations': len(failed),
            'most_common_operation': most_common,
            'average_result': average_result,
            'operation_distribution': operation_counts
        }

def demonstrate_calculator():
    """Demonstrate calculator functionality."""
    print("🧮 Advanced Calculator Demonstration")
    print("=" * 50)
    
    # Create calculator instance
    calc = AdvancedCalculator()
    
    # Basic arithmetic operations
    print("\n📊 Basic Arithmetic Operations:")
    
    operations = [
        ("Addition", calc.add, 10, 5),
        ("Subtraction", calc.subtract, 10, 3),
        ("Multiplication", calc.multiply, 6, 7),
        ("Division", calc.divide, 20, 4),
        ("Power", calc.power, 2, 8),
        ("Modulo", calc.modulo, 17, 5),
    ]
    
    for name, func, a, b in operations:
        result = func(a, b)
        if result.success:
            print(f"✅ {name}: {a} {result.operation} {b} = {result.result}")
        else:
            print(f"❌ {name}: {result.error_message}")
    
    # Scientific operations
    print("\n🔬 Scientific Operations:")
    
    scientific_ops = [
        ("Square Root", calc.square_root, 25),
        ("Percentage", calc.percentage, 25, 100),
        ("Factorial", calc.factorial, 5),
        ("Logarithm", calc.logarithm, 100, 10),
        ("Sine", calc.sine, 30),
        ("Cosine", calc.cosine, 60),
        ("Tangent", calc.tangent, 45),
    ]
    
    for name, func, *args in scientific_ops:
        result = func(*args)
        if result.success:
            args_str = ", ".join(str(arg) for arg in args)
            print(f"✅ {name}({args_str}) = {result.result:.4f}")
        else:
            print(f"❌ {name}: {result.error_message}")
    
    # Error handling demonstrations
    print("\n⚠️ Error Handling Examples:")
    
    error_cases = [
        ("Division by zero", calc.divide, 10, 0),
        ("Square root of negative", calc.square_root, -16),
        ("Factorial of negative", calc.factorial, -5),
        ("Modulo by zero", calc.modulo, 10, 0),
        ("Logarithm of zero", calc.logarithm, 0),
        ("Tangent at 90°", calc.tangent, 90),
    ]
    
    for name, func, *args in error_cases:
        result = func(*args)
        print(f"❌ {name}: {result.error_message}")
    
    # Statistics
    print("\n📈 Calculator Statistics:")
    stats = calc.get_statistics()
    print(f"Total calculations: {stats['total_calculations']}")
    print(f"Successful: {stats['successful_calculations']}")
    print(f"Failed: {stats['failed_calculations']}")
    print(f"Most common operation: {stats['most_common_operation']}")
    print(f"Average result: {stats['average_result']:.2f}")
    
    print("\n🎉 Calculator demonstration complete!")

# Interactive calculator
def interactive_calculator():
    """Run interactive calculator mode."""
    calc = AdvancedCalculator()
    
    print("\n🎮 Interactive Calculator Mode")
    print("Available operations: add, subtract, multiply, divide, power, sqrt, percent, factorial, log, sin, cos, tan")
    print("Type 'quit' to exit, 'history' to see history, 'stats' to see statistics")
    print("Type 'clear' to clear history")
    
    while True:
        try:
            user_input = input("\n🧮 Enter operation: ").strip().lower()
            
            if user_input == 'quit':
                break
            elif user_input == 'history':
                history = calc.get_history()
                if history:
                    print("\n📜 Calculation History:")
                    for i, calc_result in enumerate(history[-10:], 1):  # Show last 10
                        status = "✅" if calc_result.success else "❌"
                        print(f"{i}. {status} {calc_result.operation}: {calc_result.result}")
                else:
                    print("No history yet.")
                continue
            elif user_input == 'stats':
                stats = calc.get_statistics()
                print(f"\n📊 Statistics: {stats}")
                continue
            elif user_input == 'clear':
                calc.clear_history()
                print("History cleared.")
                continue
            
            # Parse operation and operands
            parts = user_input.split()
            if len(parts) < 2:
                print("❌ Please specify operation and operands")
                continue
            
            operation = parts[0]
            operands = [float(x) for x in parts[1:]]
            
            # Perform calculation
            result = None
            if operation == 'add' and len(operands) == 2:
                result = calc.add(operands[0], operands[1])
            elif operation == 'subtract' and len(operands) == 2:
                result = calc.subtract(operands[0], operands[1])
            elif operation == 'multiply' and len(operands) == 2:
                result = calc.multiply(operands[0], operands[1])
            elif operation == 'divide' and len(operands) == 2:
                result = calc.divide(operands[0], operands[1])
            elif operation == 'power' and len(operands) == 2:
                result = calc.power(operands[0], operands[1])
            elif operation == 'sqrt' and len(operands) == 1:
                result = calc.square_root(operands[0])
            elif operation == 'percent' and len(operands) == 2:
                result = calc.percentage(operands[0], operands[1])
            elif operation == 'factorial' and len(operands) == 1:
                result = calc.factorial(int(operands[0]))
            elif operation == 'log' and len(operands) >= 1:
                if len(operands) == 2:
                    result = calc.logarithm(operands[0], operands[1])
                else:
                    result = calc.logarithm(operands[0])
            elif operation == 'sin' and len(operands) == 1:
                result = calc.sine(operands[0])
            elif operation == 'cos' and len(operands) == 1:
                result = calc.cosine(operands[0])
            elif operation == 'tan' and len(operands) == 1:
                result = calc.tangent(operands[0])
            else:
                print("❌ Invalid operation or wrong number of operands")
                continue
            
            if result:
                if result.success:
                    print(f"✅ Result: {result.result}")
                else:
                    print(f"❌ Error: {result.error_message}")
                
                # Add to history
                from datetime import datetime
                result.timestamp = datetime.now().isoformat()
                calc.history.append(result)
        
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {str(e)}")

# Main execution
if __name__ == "__main__":
    print("🧮 Advanced Calculator - Mathematical Operations Tool")
    print("Choose mode:")
    print("1. Demonstration mode")
    print("2. Interactive mode")
    
    choice = input("Enter choice (1 or 2): ").strip()
    
    if choice == "1":
        demonstrate_calculator()
    elif choice == "2":
        interactive_calculator()
    else:
        print("❌ Invalid choice. Running demonstration mode...")
        demonstrate_calculator()
