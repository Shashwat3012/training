# Python Functions Examples

# 1. Parameters and arguments
def greet(name, age):
    print(f"Hello {name}, you are {age} years old")

# Calling function with arguments
greet("shashwat tripathi", 21)




# Seeting default parameters for no parameters passed
def introduce(name, age=21, city="Mumbai"):
    print(f"Hi, I'm {name}, {age} years old from {city}")

introduce("shashwat tripathi")
introduce("shashwat tripathi", 22, "Delhi")




# Modifying and returning parameter
def calculate_age_after_years(current_age, years):
    future_age = current_age + years
    return future_age

age = 21
future_age = calculate_age_after_years(age, 5)
print(f"shashwat will be {future_age} years old after 5 years")




# Return multiple values
def get_student_info():
    name = "shashwat tripathi"
    age = 21
    course = "Computer Science"
    return name, age, course

student_name, student_age, student_course = get_student_info()
print(f"Student: {student_name}, Age: {student_age}, Course: {student_course}")



# 3. Args and Kwargs
# *args - variable number of arguments
def show_subjects(*subjects):
    print("shashwat's subjects:")
    for subject in subjects:
        print(f"- {subject}")

show_subjects("Python", "Math", "Physics")
show_subjects("English", "History")


# **kwargs - keyword arguments
def show_details(**details):
    print("shashwat's details:")
    for key, value in details.items():
        print(f"{key}: {value}")

show_details(name="shashwat tripathi", age=21, college="VESIT")
show_details(name="shashwat tripathi", age=21, hobby="coding", city="Mumbai")

# Using both args and kwargs
def student_info(name, *subjects, **details):
    print(f"Student: {name}")
    print("Subjects:")
    for subject in subjects:
        print(f"- {subject}")
    print("Other details:")
    for key, value in details.items():
        print(f"{key}: {value}")

student_info("shashwat tripathi", "Python", "Java", "C++", age=21, college="VESIT", year="Final")