# Showcasing different variable types and naming conventions.

# Proper variable naming (snake_case for variables)
student_name = "Shashwat"
student_age = 21
is_active = True



# Multiple assignment
x, y, z = 10, 20, 30



# Chain assignment
a = b = c = 100



# Swapping variables
first_number = 5
second_number = 10
print(f"Before swap: first={first_number}, second={second_number}")

first_number, second_number = second_number, first_number
print(f"After swap: first={first_number}, second={second_number}")



# Dynamic typing showcase
dynamic_var = 42
print(f"Initial type: {type(dynamic_var).__name__} = {dynamic_var}")

dynamic_var = "Now I'm a string!"
print(f"Changed type: {type(dynamic_var).__name__} = {dynamic_var}")

dynamic_var = [1, 2, 3, 4]
print(f"Now a list: {type(dynamic_var).__name__} = {dynamic_var}")



# Variable scope demonstration
global_var = "I'm global"

def inner_function():
    local_var = "I'm local"
    nonlocal_var = "I can access outer scope"
    return local_var, nonlocal_var




