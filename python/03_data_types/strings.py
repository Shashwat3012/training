import datetime
from decimal import Decimal
from dataclasses import dataclass

@dataclass
# Example class for f-string demonstrations
class Person:
    name: str
    age: int
    salary: float

# Showcase string operations and f-string formatting
def demonstrate_strings():
    # Basic string creation
    single_quoted = 'Hello, World!'
    double_quoted = "Hello, World!"
    triple_quoted = """This is a
    multiline string
    with proper indentation."""
    
    raw_string = r"This is a raw string with \n and \t"
    
    print("Basic Strings:")
    print(f"Single quoted: {single_quoted}")
    print(f"Raw string: {raw_string}")
    
    # F-string basics
    name = "Alice"
    age = 30
    height = 5.8
    
    # Simple f-string
    basic_fstring = f"Hello, my name is {name} and I'm {age} years old."
    print(f"\nBasic f-string: {basic_fstring}")
    
    # F-string with expressions
    print(f"Next year, {name} will be {age + 1} years old.")
    print(f"Is {name} an adult? {age >= 18}")
    
    # Advanced f-string formatting
    pi = 3.14159265359
    large_number = 1234567.89
    
    print(f"\nAdvanced F-string Formatting:")
    print(f"Pi to 2 decimal places: {pi:.2f}")
    print(f"Pi in scientific notation: {pi:.2e}")
    print(f"Large number with commas: {large_number:,.2f}")
    print(f"Percentage: {0.856:.1%}")
    
    # String alignment and padding
    word = "Python"
    print(f"\nString Alignment:")
    print(f"Left aligned: '{word:<15}'")
    print(f"Right aligned: '{word:>15}'")
    print(f"Center aligned: '{word:^15}'")
    print(f"Center with fill: '{word:*^15}'")
    
    # Date and time formatting
    now = datetime.datetime.now()
    print(f"\nDate/Time Formatting:")
    print(f"Current time: {now:%Y-%m-%d %H:%M:%S}")
    print(f"Formatted date: {now:%B %d, %Y}")
    print(f"Time only: {now:%I:%M %p}")




# Demonstrate advanced f-string capabilities
def advanced_fstring_features():
    
    # F-strings with object attributes
    person = Person("Bob", 25, 75000.50)
    
    print("F-strings with Objects:")
    print(f"Employee: {person.name}, Age: {person.age}, Salary: ${person.salary:,.2f}")
    
    # F-strings with dictionary access
    data = {
        "product": "Laptop",
        "price": 1299.99,
        "discount": 0.15
    }
    
    final_price = data["price"] * (1 - data["discount"])
    print(f"\nDictionary access in f-strings:")
    print(f"Product: {data['product']}")
    print(f"Original price: ${data['price']:.2f}")
    print(f"After {data['discount']:.0%} discount: ${final_price:.2f}")
    
    # F-strings with method calls
    text = "hello world"
    print(f"\nMethod calls in f-strings:")
    print(f"Title case: {text.title()}")
    print(f"Word count: {len(text.split())}")
    print(f"Reversed: {text[::-1]}")
    
    # Conditional expressions in f-strings
    score = 85
    grade = f"Grade: {'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'}"
    print(f"\nConditional in f-string: {grade}")
    
    # Nested f-strings (Python 3.12+)
    items = ["apple", "banana", "cherry"]
    print(f"Items: {', '.join(f'{item.title()}' for item in items)}")



# Demonstrate essential string methods
def string_methods_showcase():
    sample_text = "  The Quick Brown Fox Jumps Over The Lazy Dog  "
    
    print("String Methods Demonstration:")
    print(f"Original: '{sample_text}'")
    print(f"Stripped: '{sample_text.strip()}'")
    print(f"Lower case: '{sample_text.lower()}'")
    print(f"Upper case: '{sample_text.upper()}'")
    print(f"Title case: '{sample_text.title()}'")
    print(f"Swapped case: '{sample_text.swapcase()}'")
    
    # String testing methods
    tests = {
        "Is alphanumeric": "abc123".isalnum(),
        "Is alphabetic": "abcdef".isalpha(),
        "Is digit": "12345".isdigit(),
        "Is lowercase": "hello".islower(),
        "Is uppercase": "HELLO".isupper(),
        "Starts with 'The'": sample_text.strip().startswith("The"),
        "Ends with 'Dog'": sample_text.strip().endswith("Dog"),
    }
    
    print("\nString Testing Methods:")
    for test, result in tests.items():
        print(f"{test}: {result}")
    
    # String manipulation
    sentence = "Python is awesome"
    words = sentence.split()
    
    print(f"\nString Manipulation:")
    print(f"Split into words: {words}")
    print(f"Join with hyphens: {'-'.join(words)}")
    print(f"Replace 'awesome' with 'fantastic': {sentence.replace('awesome', 'fantastic')}")
    print(f"Find 'is': {sentence.find('is')}")
    print(f"Count 'o': {sentence.count('o')}")


#  Driver COde
if __name__ == "__main__":
    demonstrate_strings()
    advanced_fstring_features()
    string_methods_showcase()