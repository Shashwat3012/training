


# Demonstrating basic dictionary operations
def basic_dictionary_operations():
    # Creating dictionaries
    student = {
        'name': 'shashwat tripathi',
        'age': 21,
        'course': 'Computer Science',
        'grades': [85, 92, 78, 96]
    }
    
    print("Original student data:")
    print(student)
    
    # Accessing values
    print(f"\nStudent name: {student['name']}")
    print(f"Student age: {student['age']}")
    
    # Using get() method (safer)
    email = student.get('email', 'not provided')
    print(f"Email: {email}")
    
    # Adding new key-value pairs
    student['email'] = 'shashwat@example.com'
    student['city'] = 'Mumbai'
    
    # Updating existing values
    student['age'] = 22  # Birthday!
    
    print("\nUpdated student data:")
    print(student)



# Nested Dictionaries
def nested_dictionaries():
    company = {
        'name': 'Tech Solutions',
        'employees': {
            'manager': {
                'name': 'shashwat tripathi',
                'age': 21,
                'salary': 75000,
                'skills': ['Python', 'Leadership', 'Project Management']
            },
            'developer': {
                'name': 'priya sharma',
                'age': 24,
                'salary': 65000,
                'skills': ['JavaScript', 'React', 'Node.js']
            }
        },
        'departments': ['IT', 'HR', 'Finance']
    }
    
    print("Company structure:")
    print(f"Company: {company['name']}")
    
    # Accessing nested data
    manager = company['employees']['manager']
    print(f"Manager: {manager['name']}, Age: {manager['age']}")
    print(f"Manager skills: {', '.join(manager['skills'])}")



# Different Methods in dictionaries
def dictionary_methods():
    inventory = {
        'laptops': 25,
        'keyboards': 50,
        'mice': 30,
        'monitors': 15
    }
    
    print("Inventory management:")
    print(f"Original inventory: {inventory}")
    
    # Dictionary methods
    print(f"\nItems: {list(inventory.keys())}")
    print(f"Quantities: {list(inventory.values())}")
    print(f"Key-value pairs: {list(inventory.items())}")
    
    # Iterating through dictionary
    print("\nCurrent stock levels:")
    for item, quantity in inventory.items():
        status = "Low stock" if quantity < 20 else "Good stock"
        print(f"{item.capitalize()}: {quantity} units - {status}")
    
    # Dictionary comprehension
    low_stock = {item: qty for item, qty in inventory.items() if qty < 20}
    print(f"\nLow stock items: {low_stock}")




# Dictionary usage
def practical_dictionary_example():
    students = {
        'shashwat tripathi': {
            'subjects': {
                'Math': [85, 90, 88],
                'Physics': [78, 85, 82],
                'Chemistry': [92, 89, 94]
            },
            'age': 21
        },
        'amit kumar': {
            'subjects': {
                'Math': [76, 82, 79],
                'Physics': [85, 88, 86],
                'Chemistry': [80, 85, 83]
            },
            'age': 20
        }
    }
    
    print("Student Grade Calculator:")
    
    for student_name, data in students.items():
        print(f"\n{student_name.title()}:")
        
        total_marks = 0
        subject_count = 0
        
        for subject, marks in data['subjects'].items():
            avg_marks = sum(marks) / len(marks)
            print(f"  {subject}: {avg_marks:.1f}%")
            total_marks += avg_marks
            subject_count += 1
        
        overall_avg = total_marks / subject_count
        print(f"  Overall Average: {overall_avg:.1f}%")
        
        # Grade calculation
        if overall_avg >= 90:
            grade = 'A+'
        elif overall_avg >= 80:
            grade = 'A'
        elif overall_avg >= 70:
            grade = 'B'
        else:
            grade = 'C'
        
        print(f"  Grade: {grade}")




# Main function to run all dictionary examples
def main():
    print("=" * 50)
    print("DICTIONARIES - Shashwat Tripathi")
    print("=" * 50)
    
    basic_dictionary_operations()
    print("\n" + "-" * 50)
    
    nested_dictionaries()
    print("\n" + "-" * 50)
    
    dictionary_methods()
    print("\n" + "-" * 50)
    
    practical_dictionary_example()


# DRiver Code
if __name__ == "__main__":
    main()