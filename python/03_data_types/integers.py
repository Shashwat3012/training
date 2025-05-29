import sys
# from decimal import Decimal

# Showcasing integer operations, precision, and advanced features
def demonstrate_integers():
    # Basic integer operations
    regular_int = 42
    negative_int = -17
    zero = 0
    
    print(f"Basic integers: {regular_int}, {negative_int}, {zero}")
    
    # Large integers (Python handles arbitrary precision)
    large_number = 123456789012345678901234567890
    very_large = 10**100  # Googol
    
    print(f"Large number: {large_number}")
    print(f"Googol (10^100): {very_large}")
    
    # Number systems
    binary_num = 0b1010  # Binary (base 2)
    octal_num = 0o755    # Octal (base 8)
    hex_num = 0xFF       # Hexadecimal (base 16)
    
    print(f"Binary 1010 = {binary_num}")
    print(f"Octal 755 = {octal_num}")
    print(f"Hex FF = {hex_num}")
    
    # Arithmetic operations
    a, b = 15, 4
    
    operations = {
        'Addition': a + b,
        'Subtraction': a - b,
        'Multiplication': a * b,
        'Division (float)': a / b,
        'Floor division': a // b,
        'Modulus': a % b,
        'Exponentiation': a ** b,
    }
    
    print("\nArithmetic Operations:")
    for operation, result in operations.items():
        print(f"{operation}: {a} op {b} = {result}")
    
    # Bitwise operations
    x, y = 12, 25  # 12 = 1100, 25 = 11001 in binary
    
    bitwise_ops = {
        'AND': x & y,
        'OR': x | y,
        'XOR': x ^ y,
        'NOT x': ~x,
        'Left shift': x << 2,
        'Right shift': x >> 2,
    }
    
    print(f"\nBitwise Operations (x={x}, y={y}):")
    for op_name, result in bitwise_ops.items():
        print(f"{op_name}: {result}")
    
    # Advanced integer methods
    number = -42
    print(f"\nAdvanced methods for {number}:")
    print(f"Absolute value: {abs(number)}")
    print(f"Bit length: {number.bit_length()}")
    print(f"Convert to bytes: {number.to_bytes(4, 'big', signed=True)}")
    
    # Integer limits and system info
    print(f"\nSystem integer info:")
    print(f"Max int size: {sys.maxsize}")
    print(f"Int info: {sys.int_info}")
    
    # Working with divmod for efficiency
    dividend, divisor = 100, 7
    quotient, remainder = divmod(dividend, divisor)
    print(f"\ndivmod({dividend}, {divisor}) = ({quotient}, {remainder})")



# Demonstrate integer validation and type checking
def integer_validation_example():
    
    # Safely handle integer operations with validation
    def safe_integer_operation(value):
        
        if not isinstance(value, int):
            try:
                value = int(value)
            except (ValueError, TypeError):
                return None, f"Cannot convert {value} to integer"
        
        # Perform some operation
        result = value * 2 + 1
        return result, "Success"
    
    test_values = [42, "123", "abc", 3.14, None, True]
    
    print("\nInteger validation examples:")
    for val in test_values:
        result, message = safe_integer_operation(val)
        print(f"Input: {val} ({type(val).__name__}) -> Result: {result}, Status: {message}")

if __name__ == "__main__":
    demonstrate_integers()
    integer_validation_example()