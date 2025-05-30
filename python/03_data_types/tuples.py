from typing import Tuple, NamedTuple, Any
from collections import namedtuple
import sys
import time


# Named tuple for 2D coordinates using modern typing
class Point(NamedTuple):
    x: float
    y: float
    
    def distance_from_origin(self) -> float:
        """Calculate distance from origin."""
        return (self.x ** 2 + self.y ** 2) ** 0.5



# Basic tuple operations
def demonstrate_basic_tuples():
    # Different ways to create tuples
    empty_tuple = ()
    single_item = (42,)  # Note the comma for single-item tuple
    coordinates = (10, 20)
    rgb_color = (255, 128, 0)
    mixed_tuple = (1, "hello", 3.14, True)
    
    print("Tuple Creation:")
    print(f"Empty tuple: {empty_tuple} (type: {type(empty_tuple).__name__})")
    print(f"Single item: {single_item}")
    print(f"Coordinates: {coordinates}")
    print(f"RGB color: {rgb_color}")
    print(f"Mixed types: {mixed_tuple}")
    
    # Tuple without parentheses (tuple packing)
    packed_tuple = 1, 2, 3, 4
    print(f"Packed tuple: {packed_tuple}")
    
    # Tuple unpacking
    x, y = coordinates
    r, g, b = rgb_color
    
    print(f"\nTuple Unpacking:")
    print(f"x = {x}, y = {y}")
    print(f"r = {r}, g = {g}, b = {b}")
    
    # Extended unpacking (Python 3.0+)
    numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    first, second, *middle, second_last, last = numbers
    
    print(f"Extended unpacking:")
    print(f"First: {first}, Second: {second}")
    print(f"Middle: {middle}")
    print(f"Second last: {second_last}, Last: {last}")



# Tuple Methods
def demonstrate_tuple_methods():
    # Tuple methods (limited due to immutability)
    colors = ("red", "green", "blue", "red", "yellow", "red")
    
    print("Tuple Methods:")
    print(f"Colors: {colors}")
    print(f"Count of 'red': {colors.count('red')}")
    print(f"Index of 'blue': {colors.index('blue')}")
    print(f"Length: {len(colors)}")
    
    # Tuple operations
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    print(f"\nTuple Operations:")
    print(f"Concatenation: {tuple1 + tuple2}")
    print(f"Repetition: {tuple1 * 3}")
    print(f"Membership: {2 in tuple1}")
    print(f"Slicing: {colors[1:4]}")
    
    # Comparison
    print(f"Comparison (1,2,3) < (1,2,4): {(1,2,3) < (1,2,4)}")
    print(f"Comparison (1,2,3) == (1,2,3): {(1,2,3) == (1,2,3)}")




def demonstrate_named_tuples():
    # Using collections.namedtuple (older approach)
    Person = namedtuple('Person', ['name', 'age', 'city'])
    
    # Creating instances
    alice = Person("Alice", 30, "New York")
    bob = Person("Bob", 25, "San Francisco")
    
    print("Named Tuples (collections.namedtuple):")
    print(f"Alice: {alice}")
    print(f"Alice's name: {alice.name}")
    print(f"Alice's age: {alice.age}")
    
    # Named tuple methods
    print(f"Alice as dict: {alice._asdict()}")
    print(f"Fields: {alice._fields}")
    
    # Replace method (returns new tuple)
    older_alice = alice._replace(age=31)
    print(f"Older Alice: {older_alice}")
    
    # Using modern NamedTuple (typing module)
    point1 = Point(3.0, 4.0)
    point2 = Point(0.0, 0.0)
    
    print(f"\nModern Named Tuples (typing.NamedTuple):")
    print(f"Point 1: {point1}")
    print(f"Distance from origin: {point1.distance_from_origin():.2f}")
    
    # Named tuples are still tuples
    print(f"Point1 + Point2: {tuple(point1) + tuple(point2)}")




def tuple_use_cases():
    # 1. Function returning multiple values
    def get_name_age():
        """Return multiple values as tuple."""
        return "Charlie", 28
    
    name, age = get_name_age()
    print(f"Function return: {name}, {age}")
    
    # 2. Dictionary keys (tuples are hashable)
    coordinates_dict = {
        (0, 0): "Origin",
        (1, 0): "Right",
        (0, 1): "Up",
        (-1, 0): "Left",
        (0, -1): "Down"
    }
    
    print(f"\nTuples as dictionary keys:")
    for coord, direction in coordinates_dict.items():
        print(f"{coord}: {direction}")
    
    # 3. Swapping variables
    a, b = 10, 20
    print(f"Before swap: a={a}, b={b}")
    a, b = b, a
    print(f"After swap: a={a}, b={b}")
    
    # 4. Configuration settings (immutable)
    DATABASE_CONFIG = (
        "localhost",
        5432,
        "myapp",
        "production"
    )
    
    host, port, database, environment = DATABASE_CONFIG
    print(f"\nDatabase config: {host}:{port}/{database} ({environment})")
    
    # 5. RGB color palette
    COLOR_PALETTE = (
        (255, 0, 0),    # Red
        (0, 255, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 255, 0),  # Yellow
        (255, 0, 255),  # Magenta
    )
    
    print(f"Color palette:")
    color_names = ["Red", "Green", "Blue", "Yellow", "Magenta"]
    for i, (r, g, b) in enumerate(COLOR_PALETTE):
        print(f"  {color_names[i]}: RGB({r}, {g}, {b})")




# Advanced tuple usage
def advanced_tuple_techniques():
    # Tuple comprehension (actually generator)
    numbers = (1, 2, 3, 4, 5)
    squared_gen = (x**2 for x in numbers)  # This is a generator
    squared_tuple = tuple(x**2 for x in numbers)  # Convert to tuple
    
    print("Tuple Comprehension:")
    print(f"Original: {numbers}")
    print(f"Squared tuple: {squared_tuple}")
    
    # Nested tuples
    matrix = (
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    )
    
    print(f"\nNested tuples (matrix):")
    for row in matrix:
        print(row)
    
    # Tuple unpacking in loops
    students = [
        ("Alice", 85, "A"),
        ("Bob", 92, "A+"),
        ("Charlie", 78, "B+"),
        ("Diana", 96, "A+")
    ]
    
    print(f"\nTuple unpacking in loops:")
    for name, score, grade in students:
        print(f"{name}: {score} ({grade})")
    
    # Enumerate with tuples
    fruits = ("apple", "banana", "cherry")
    print(f"\nEnumerate with tuples:")
    for index, fruit in enumerate(fruits):
        print(f"{index}: {fruit}")
    
    # Zip creating tuples
    names = ("Alice", "Bob", "Charlie")
    ages = (25, 30, 35)
    cities = ("NYC", "LA", "Chicago")
    
    combined = tuple(zip(names, ages, cities))
    print(f"\nZip creating tuples:")
    print(f"Combined: {combined}")
    
    # Tuple as frozen set alternative (for simple cases)
    immutable_set = tuple(sorted(set([3, 1, 4, 1, 5, 9, 2, 6])))
    print(f"Immutable set-like tuple: {immutable_set}")



# Tuple compared to list
def performance_comparison():
    # Memory usage
    list_data = [i for i in range(1000)]
    tuple_data = tuple(i for i in range(1000))
    
    print("Performance Comparison:")
    print(f"List memory usage: {sys.getsizeof(list_data)} bytes")
    print(f"Tuple memory usage: {sys.getsizeof(tuple_data)} bytes")
    
    # Access time comparison
    def time_access(data, iterations=100000):
        """Time random access operations."""
        start_time = time.perf_counter()
        for _ in range(iterations):
            _ = data[500]  # Access middle element
        end_time = time.perf_counter()
        return end_time - start_time
    
    list_time = time_access(list_data)
    tuple_time = time_access(tuple_data)
    
    print(f"List access time: {list_time:.6f} seconds")
    print(f"Tuple access time: {tuple_time:.6f} seconds")
    print(f"Tuple is {list_time/tuple_time:.2f}x faster for access")
    
    # Iteration comparison
    def time_iteration(data, iterations=1000):
        """Time iteration operations."""
        start_time = time.perf_counter()
        for _ in range(iterations):
            for item in data:
                pass  # Just iterate
        end_time = time.perf_counter()
        return end_time - start_time
    
    list_iter_time = time_iteration(list_data)
    tuple_iter_time = time_iteration(tuple_data)
    
    print(f"List iteration time: {list_iter_time:.6f} seconds")
    print(f"Tuple iteration time: {tuple_iter_time:.6f} seconds")



# Demonstrate tuple best practices and common patterns
def tuple_best_practices():
    print("Tuple Best Practices:")
    
    # 1. Use tuples for heterogeneous data
    employee_record = ("Shashwat Tripathi", 101, "Engineering", 75000.0)
    print(f"Employee record: {employee_record}")
    
    # 2. Use named tuples for better readability
    Employee = namedtuple('Employee', ['name', 'id', 'department', 'salary'])
    shashwat = Employee("Shashwat Tripathi", 101, "Engineering", 75000.0)
    print(f"Named tuple: {shashwat}")
    
    # 3. Return multiple values from functions
    def calculate_stats(numbers):
        if not numbers:
            return 0, 0, 0, 0
        
        total = sum(numbers)
        count = len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        
        return total, count, minimum, maximum
    
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    total, count, min_val, max_val = calculate_stats(data)
    print(f"Stats: total={total}, count={count}, min={min_val}, max={max_val}")
    
    # 4. Use tuples for constants that shouldn't change
    HTTP_STATUS_CODES = (
        (200, "OK"),
        (404, "Not Found"),
        (500, "Internal Server Error")
    )
    
    print("HTTP Status Codes:")
    for code, message in HTTP_STATUS_CODES:
        print(f"  {code}: {message}")
    
    # 5. Tuple unpacking for cleaner code
    def process_coordinates(points):
        for x, y in points:
            distance = (x**2 + y**2)**0.5
            print(f"Point ({x}, {y}): distance = {distance:.2f}")
    
    points = [(3, 4), (0, 5), (1, 1), (2, 3)]
    process_coordinates(points)





if __name__ == "__main__":
    demonstrate_basic_tuples()
    print("\n" + "="*60 + "\n")
    demonstrate_tuple_methods()
    print("\n" + "="*60 + "\n")
    demonstrate_named_tuples()
    print("\n" + "="*60 + "\n")
    tuple_use_cases()
    print("\n" + "="*60 + "\n")
    advanced_tuple_techniques()
    print("\n" + "="*60 + "\n")
    performance_comparison()
    print("\n" + "="*60 + "\n")
    tuple_best_practices()