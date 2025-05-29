from typing import Any

# Showcase boolean operations and truthiness in Python
def demonstrate_booleans():
    # Basic boolean values
    is_valid = True
    is_empty = False
    
    print("Basic Boolean Values:")
    print(f"is_valid: {is_valid} (type: {type(is_valid).__name__})")
    print(f"is_empty: {is_empty} (type: {type(is_empty).__name__})")
    
    # Boolean operations
    print(f"\nLogical Operations:")
    print(f"True and False: {True and False}")
    print(f"True or False: {True or False}")
    print(f"not True: {not True}")
    print(f"not False: {not False}")
    
    # Comparison operations that return booleans
    a, b = 10, 20
    
    comparisons = {
        'Equal': a == b,
        'Not equal': a != b,
        'Less than': a < b,
        'Greater than': a > b,
        'Less or equal': a <= b,
        'Greater or equal': a >= b,
    }
    
    print(f"\nComparison Operations (a={a}, b={b}):")
    for operation, result in comparisons.items():
        print(f"{operation}: {result}")
    
    # Identity vs equality
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = list1
    
    print(f"\nIdentity vs Equality:")
    print(f"list1 == list2: {list1 == list2}")  # True (same content)
    print(f"list1 is list2: {list1 is list2}")  # False (different objects)
    print(f"list1 is list3: {list1 is list3}")  # True (same object)




# Show Python's truthiness concept - what evaluates to True/False
def demonstrate_truthiness():
    # Values that are considered False (falsy)
    falsy_values = [
        False,
        None,
        0,
        0.0,
        0j,  # complex number
        "",  # empty string
        [],  # empty list
        (),  # empty tuple
        {},  # empty dict
        set(),  # empty set
    ]
    
    print("Falsy Values (evaluate to False in boolean context):")
    for value in falsy_values:
        print(f"{repr(value):>10} -> {bool(value)}")
    
    # Values that are considered True (truthy)
    truthy_values = [
        True,
        1,
        -1,
        3.14,
        "hello",
        [1, 2, 3],
        (1,),
        {"key": "value"},
        {1, 2, 3},
    ]
    
    print(f"\nTruthy Values (evaluate to True in boolean context):")
    for value in truthy_values:
        print(f"{repr(value):>15} -> {bool(value)}")

# Demonstrating booleans in different contexts
def boolean_context_examples():
    
    # In conditional statements
    # Returning status based on truthiness of value
    def check_status(value: Any) -> str:
        if value:
            return "Active"
        else:
            return "Inactive"
    
    test_values = [True, False, 1, 0, "hello", "", [1, 2], [], None]
    
    print("Boolean Context in Conditionals:")
    for val in test_values:
        status = check_status(val)
        print(f"{repr(val):>10} -> {status}")
    
    # Short-circuit evaluation
    print(f"\nShort-circuit Evaluation:")
    
    # Simulate an expensive operation
    def expensive_operation():
        print("Expensive operation called!")
        return True
    
    # 'and' short-circuits if first operand is False
    print("False and expensive_operation():")
    result1 = False and expensive_operation()  # expensive_operation() not called
    print(f"Result: {result1}")
    
    print("\nTrue and expensive_operation():")
    result2 = True and expensive_operation()  # expensive_operation() is called
    print(f"Result: {result2}")
    
    # 'or' short-circuits if first operand is True
    print("\nTrue or expensive_operation():")
    result3 = True or expensive_operation()  # expensive_operation() not called
    print(f"Result: {result3}")





# Showing advanced boolean usage patterns
def advanced_boolean_patterns():
    
    # Using booleans for filtering
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_numbers = [num for num in numbers if num % 2 == 0]
    
    print("Boolean Filtering:")
    print(f"Original numbers: {numbers}")
    print(f"Even numbers: {even_numbers}")
    
    # Boolean flags for control flow
    # Process data with boolean flags controlling behavior
    def process_data(data: list, validate: bool = True, transform: bool = False, log: bool = False):
        
        if log:
            print(f"Processing {len(data)} items...")
        
        if validate:
            # Simulate validation
            if not data:
                return None
            if log:
                print("Data validation passed")
        
        result = data.copy()
        
        if transform:
            result = [x * 2 for x in result]
            if log:
                print("Data transformation applied")
        
        return result
    
    sample_data = [1, 2, 3, 4, 5]
    
    print(f"\nBoolean Flags Example:")
    result1 = process_data(sample_data, validate=True, transform=False, log=True)
    print(f"Result 1: {result1}")
    
    result2 = process_data(sample_data, validate=True, transform=True, log=True)
    print(f"Result 2: {result2}")
    
    # Ternary operator (conditional expression)
    age = 20
    status = "adult" if age >= 18 else "minor"
    print(f"\nTernary operator: {age} years old -> {status}")
    
    # Chained comparisons
    score = 85
    grade_check = 80 <= score <= 90
    print(f"Score {score} is between 80 and 90: {grade_check}")


# Driver Code
if __name__ == "__main__":
    demonstrate_booleans()
    print("\n" + "="*50 + "\n")
    demonstrate_truthiness()
    print("\n" + "="*50 + "\n")
    boolean_context_examples()
    print("\n" + "="*50 + "\n")
    advanced_boolean_patterns()