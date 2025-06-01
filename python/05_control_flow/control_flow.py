# Python Control Flow Examples

# 1. If-else
def if_else_example():
    name = "shashwat tripathi"
    age = 21

    if age >= 18:
        print(f"{name} is an adult")
    else:
        print(f"{name} is a minor")


# Nested if-else example
def nested_if_else():
    marks = 85
    gender = "M"

    if gender == "M":
        if marks >= 90:
            print("The boy scored Grade A")
        elif marks >= 80:
            print("The boy scored Grade B")
        else:
            print("The boy scored Grade C")

    else:
        if marks >= 90:
            print("The girl scored Grade A")
        elif marks >= 80:
            print("The girl scored Grade B")
        else:
            print("The girl scored Grade C")



# 2. For loop
def for_loop(name):
    print(f"\n{name}'s favorite numbers:")
    for i in range(1, 6):
        print(f"Number {i}")

    # For loop with list
    hobbies = ["coding", "reading", "gaming"]
    for hobby in hobbies:
        print(f"{name} likes {hobby}")



# 3. While loop
def while_loop(name):
    count = 0
    print(f"\nCountdown for {name}:")
    while count < 5:
        print(f"Count: {count}")
        count += 1




# 4. Break and continue
def break_continue(name):
    print(f"\n{name}'s lucky numbers:")
    for num in range(1, 11):
        if num == 5:
            continue  # skip 5
        if num == 8:
            break     # stop at 8
        print(num)




# 5. Pass
def future_function():
    pass  # placeholder for later

    if 20 > 25:
        pass  # will add code later
    else:
        print("shashwat is young")




# 6. Loop-else
def loop_else(name, age):
    print(f"\nSearching for {name}'s age in list:")
    ages = [18, 19, 20, 22, 23]
    for a in ages:
        if a == age:
            print(f"Found age {age}!")
            break
    else:
        print(f"Age {age} not found in list")

# Another loop-else example
def new_loop_else():
    print("Checking even numbers:")
    for num in [1, 3, 5, 7]:
        if num % 2 == 0:
            print(f"Found even number: {num}")
            break
    else:
        print("No even numbers found")




# Driver code
def main():
    if_else_example()
    nested_if_else()
    for_loop("shashwat")
    while_loop("shashwat")
    break_continue("Shashwat")
    future_function()
    loop_else("shashwat", 21)
    new_loop_else()

if __name__ == "__main__":
    main()