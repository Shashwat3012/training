# Python Error Handling Examples



# Basic try-except
try:
    age = int(input("Enter shashwat's age: "))
    print(f"shashwat is {age} years old")
except ValueError:
    print("Please enter a valid number for age")



# Multiple except blocks
def divide_marks(total, subjects):
    try:
        average = total / subjects
        print(f"shashwat's average marks: {average}")
    except ZeroDivisionError:
        print("Cannot divide by zero subjects")
    except TypeError:
        print("Please use numbers only")

divide_marks(420, 5)  # works fine
divide_marks(420, 0)  # causes error



# 2. Else-finally
def check_student_file():
    try:
        file = open("shashwat_marks.txt", "r")
        data = file.read()
    except FileNotFoundError:
        print("shashwat's marks file not found")
    else:
        print("File opened successfully")
        print("shashwat's data loaded")
    finally:
        print("File operation completed")

check_student_file()




# Another else-finally example
def validate_age(age):
    try:
        if age < 0:
            raise ValueError("Age cannot be negative")
        age_check = int(age)
    except ValueError as e:
        print(f"Error: {e}")
    else:
        print(f"shashwat's age {age} is valid")
    finally:
        print("Age validation process finished")

validate_age(21)
validate_age(-5)




# 3. Raise
def check_student_grade(marks):
    if marks < 0:
        raise ValueError("Marks cannot be negative")
    if marks > 100:
        raise ValueError("Marks cannot exceed 100")
    return "Valid marks"

# Using raise
try:
    result = check_student_grade(85)
    print(f"shashwat's marks: {result}")
except ValueError as e:
    print(f"Error: {e}")

try:
    result = check_student_grade(120)  # This will raise error
    print(f"shashwat's marks: {result}")
except ValueError as e:
    print(f"Error: {e}")

# Custom exception with raise
def verify_student_age(name, age):
    if age != 21:
        raise Exception(f"{name} should be 21 years old")
    print(f"{name} age verified successfully")

try:
    verify_student_age("shashwat tripathi", 21)
    verify_student_age("shashwat tripathi", 20)
except Exception as e:
    print(f"Verification failed: {e}")




# Example combining all concepts
def student_login(username, password):
    try:
        if len(username) < 3:
            raise ValueError("Username too short")
        if username != "shashwat":
            raise Exception("Invalid username")
        if password != "pass123":
            raise Exception("Wrong password")
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Login error: {e}")
    else:
        print("shashwat tripathi logged in successfully")
    finally:
        print("Login attempt completed")

student_login("shashwat", "pass123")  # success
student_login("sh", "pass123")        # username error
student_login("shashwat", "wrong")    # password error