
# Basic Type conversion
def basic_type_conversion():
    print("Basic Type Conversions:")
    
    # String to numbers
    age_str = "21"
    age_int = int(age_str)
    print(f"String '{age_str}' to int: {age_int}")
    
    salary_str = "50000.75"
    salary_float = float(salary_str)
    print(f"String '{salary_str}' to float: {salary_float}")
    
    # Numbers to string
    score = 95
    score_str = str(score)
    print(f"Int {score} to string: '{score_str}'")
    
    # Boolean conversions
    is_student = True
    is_student_str = str(is_student)
    print(f"Boolean {is_student} to string: '{is_student_str}'")
    
    # String to boolean (practical way)
    answer = "yes"
    is_positive = answer.lower() in ['yes', 'true', '1', 'y']
    print(f"String '{answer}' to boolean: {is_positive}")



# Type safe conversion
def safe_type_conversion():
    # Safely convert value to integer
    def safe_int_convert(value):
        try:
            return int(value)
        except ValueError:
            print(f"Cannot convert '{value}' to integer")
            return None
    
    # Safely convert value to float
    def safe_float_convert(value):
        try:
            return float(value)
        except ValueError:
            print(f"Cannot convert '{value}' to float")
            return None
    
    print("\nSafe Type Conversions:")
    
    test_values = ["21", "3.14", "hello", "25.5", "abc123"]
    
    for value in test_values:
        int_result = safe_int_convert(value)
        float_result = safe_float_convert(value)
        
        print(f"Value: '{value}'")
        print(f"  To int: {int_result}")
        print(f"  To float: {float_result}")




# Converting between different collection types
def collection_conversions():
    print("\nCollection Conversions:")
    
    # String to list
    name = "shashwat tripathi"
    name_list = list(name)
    print(f"String to list: {name_list}")
    
    # String to list (words)
    words = name.split()
    print(f"String to word list: {words}")
    
    # List to string
    joined_name = " ".join(words)
    print(f"List to string: '{joined_name}'")
    
    # List to tuple
    numbers = [1, 2, 3, 4, 5]
    numbers_tuple = tuple(numbers)
    print(f"List to tuple: {numbers_tuple}")
    
    # Tuple to list
    back_to_list = list(numbers_tuple)
    print(f"Tuple to list: {back_to_list}")
    
    # List to set (removes duplicates)
    grades = [85, 90, 85, 92, 90, 88]
    unique_grades = set(grades)
    print(f"List with duplicates: {grades}")
    print(f"Set (unique values): {unique_grades}")



# Conversion Example
def practical_conversion_example():
    print("\nPractical Example: User Registration")
    
    # Simulating user input (normally from input() function)
    user_input = {
        'name': 'shashwat tripathi',
        'age': '21',
        'height': '5.8',
        'is_student': 'yes',
        'subjects': 'Math,Physics,Chemistry'
    }
    
    print("Raw user input:", user_input)
    
    # Process and convert the data
    processed_data = {}
    
    # Keep name as string, but clean it
    processed_data['name'] = user_input['name'].strip().title()
    
    # Convert age to integer
    try:
        processed_data['age'] = int(user_input['age'])
    except ValueError:
        processed_data['age'] = None
        print("Invalid age provided")
    
    # Convert height to float
    try:
        processed_data['height'] = float(user_input['height'])
    except ValueError:
        processed_data['height'] = None
        print("Invalid height provided")
    
    # Convert is_student to boolean
    processed_data['is_student'] = user_input['is_student'].lower() in ['yes', 'true', '1', 'y']
    
    # Convert subjects string to list
    processed_data['subjects'] = [subject.strip() for subject in user_input['subjects'].split(',')]
    
    print("\nProcessed data:")
    for key, value in processed_data.items():
        print(f"  {key}: {value} (type: {type(value).__name__})")



# Converting numbers
def numeric_base_conversions():
    print("\nNumeric Base Conversions:")
    
    number = 21  # Shashwat's age
    
    # Convert to different bases
    binary = bin(number)
    octal = oct(number)
    hexadecimal = hex(number)
    
    print(f"Decimal {number} conversions:")
    print(f"  Binary: {binary}")
    print(f"  Octal: {octal}")
    print(f"  Hexadecimal: {hexadecimal}")
    
    # Convert back to decimal
    from_binary = int('0b10101', 2)  # 21 in binary
    from_hex = int('0x15', 16)       # 21 in hex
    
    print(f"\nBack to decimal:")
    print(f"  From binary '0b10101': {from_binary}")
    print(f"  From hex '0x15': {from_hex}")



# Main Function
def main():
    print("=" * 50)
    print("TYPE CONVERSION - Shashwat Tripathi")
    print("=" * 50)
    
    basic_type_conversion()
    print("\n" + "-" * 30)
    
    safe_type_conversion()
    print("\n" + "-" * 30)
    
    collection_conversions()
    print("\n" + "-" * 30)
    
    practical_conversion_example()
    print("\n" + "-" * 30)
    
    numeric_base_conversions()

if __name__ == "__main__":
    main()