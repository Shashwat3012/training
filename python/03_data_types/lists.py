import random
from typing import List, Any, Optional
from collections import Counter
import itertools
import sys
import time

# Showcase basic list operations and creation methods
def demonstrate_basic_lists():
    # Different ways to create lists
    empty_list = []
    numbers = [1, 2, 3, 4, 5]
    mixed_types = [1, "hello", 3.14, True, [1, 2, 3]]
    
    # List comprehensions
    squares = [x**2 for x in range(1, 6)]
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    
    print("List Creation:")
    print(f"Empty list: {empty_list}")
    print(f"Numbers: {numbers}")
    print(f"Mixed types: {mixed_types}")
    print(f"Squares (1-5): {squares}")
    print(f"Even squares (1-10): {even_squares}")
    
    # Using list() constructor
    string_to_list = list("Python")
    range_to_list = list(range(5, 15, 2))
    
    print(f"\nUsing list() constructor:")
    print(f"String to list: {string_to_list}")
    print(f"Range to list: {range_to_list}")


# LIst Methods
def demonstrate_list_methods():
    fruits = ["apple", "banana", "cherry"]
    
    print("Original list:", fruits)
    
    # Adding elements
    fruits.append("date")
    print("After append('date'):", fruits)
    
    fruits.insert(1, "apricot")
    print("After insert(1, 'apricot'):", fruits)
    
    fruits.extend(["elderberry", "fig"])
    print("After extend(['elderberry', 'fig']):", fruits)
    
    # Removing elements
    removed_item = fruits.pop()
    print(f"After pop(): {fruits} (removed: {removed_item})")
    
    fruits.remove("apricot")
    print("After remove('apricot'):", fruits)
    
    # Finding elements
    print(f"\nIndex of 'cherry': {fruits.index('cherry')}")
    print(f"Count of 'apple': {fruits.count('apple')}")
    print(f"'banana' in list: {'banana' in fruits}")
    
    # Sorting and reversing
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nOriginal numbers: {numbers}")
    
    sorted_numbers = sorted(numbers)  # Returns new list
    print(f"Sorted (new list): {sorted_numbers}")
    print(f"Original unchanged: {numbers}")
    
    numbers.sort(reverse=True)  # Modifies original
    print(f"Sorted in-place (desc): {numbers}")
    
    numbers.reverse()
    print(f"Reversed: {numbers}")




# advanced list operations 
def advanced_list_operations():
    # List slicing
    numbers = list(range(10))
    
    print("List Slicing:")
    print(f"Original: {numbers}")
    print(f"First 5: {numbers[:5]}")
    print(f"Last 3: {numbers[-3:]}")
    print(f"Every 2nd element: {numbers[::2]}")
    print(f"Reverse: {numbers[::-1]}")
    print(f"Middle section: {numbers[2:8:2]}")
    
    # Nested lists and matrix operations
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print(f"\nMatrix Operations:")
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    # Transpose using list comprehension
    transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    print("Transposed:")
    for row in transposed:
        print(row)
    
    # Flatten nested list
    flattened = [item for row in matrix for item in row]
    print(f"Flattened: {flattened}")



def list_comprehension_mastery():
    # Basic comprehensions
    squares = [x**2 for x in range(10)]
    print(f"Squares: {squares}")
    
    # Conditional comprehensions
    even_squares = [x**2 for x in range(10) if x % 2 == 0]
    positive_negatives = [x if x > 0 else -x for x in [-5, -2, 0, 3, 7]]
    
    print(f"Even squares: {even_squares}")
    print(f"Absolute values: {positive_negatives}")
    
    # Nested comprehensions
    words = ["hello", "world", "python", "programming"]
    vowel_counts = [sum(1 for char in word if char.lower() in 'aeiou') for word in words]
    
    print(f"Words: {words}")
    print(f"Vowel counts: {vowel_counts}")
    
    # Complex comprehensions with multiple conditions
    numbers = range(1, 51)
    fizzbuzz = [
        "FizzBuzz" if n % 15 == 0 else
        "Fizz" if n % 3 == 0 else
        "Buzz" if n % 5 == 0 else
        n
        for n in numbers
    ]
    
    print(f"FizzBuzz (first 20): {fizzbuzz[:20]}")
    
    # Dictionary comprehension from lists
    word_lengths = {word: len(word) for word in words}
    print(f"Word lengths: {word_lengths}")




def performance_and_memory_tips():
    # Memory usage comparison
    list_of_lists = [[0] * 100 for _ in range(100)]
    list_with_same_ref = [[0] * 100] * 100  # Don't do this!
    
    print("Memory and Performance Tips:")
    print(f"Proper nested list size: {sys.getsizeof(list_of_lists)} bytes")
    
    # Demonstrate the problem with shared references
    list_with_same_ref[0][0] = 1
    print(f"Shared reference problem - all rows affected: {list_with_same_ref[0][0]} == {list_with_same_ref[1][0]}")
    
    # Generator vs list comprehension for memory
    def memory_efficient_processing(data_size: int = 1000):
        # List comprehension - creates all items in memory
        list_comp = [x**2 for x in range(data_size)]
        
        # Generator expression - creates items on demand
        gen_expr = (x**2 for x in range(data_size))
        
        print(f"List comprehension memory: {sys.getsizeof(list_comp)} bytes")
        print(f"Generator expression memory: {sys.getsizeof(gen_expr)} bytes")
        
        return list_comp, gen_expr
    
    memory_efficient_processing()




# Real-world examples and use cases
def practical_list_examples():
    # Data processing pipeline
    def process_sales_data():
        sales_data = [
            {"product": "Laptop", "price": 999.99, "quantity": 2},
            {"product": "Mouse", "price": 29.99, "quantity": 5},
            {"product": "Keyboard", "price": 79.99, "quantity": 3},
            {"product": "Monitor", "price": 299.99, "quantity": 1},
        ]
        
        # Calculate total revenue per product
        revenues = [item["price"] * item["quantity"] for item in sales_data]
        
        # Find expensive items (price > 100)
        expensive_items = [item for item in sales_data if item["price"] > 100]
        
        # Sort by revenue (descending)
        sorted_by_revenue = sorted(
            zip(sales_data, revenues), 
            key=lambda x: x[1], 
            reverse=True
        )
        
        print("Sales Data Processing:")
        print(f"Total revenues: {revenues}")
        print(f"Total sales: ${sum(revenues):.2f}")
        print(f"Expensive items: {[item['product'] for item in expensive_items]}")
        print("Top revenue products:")
        for (product_data, revenue) in sorted_by_revenue:
            print(f"  {product_data['product']}: ${revenue:.2f}")
    
    process_sales_data()
    
    # Batch processing example by splitting itens
    def batch_process_items(items: List[Any], batch_size: int = 3) -> List[List[Any]]:
        batches = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            batches.append(batch)
        
        return batches
    
    items = list(range(1, 11))
    batches = batch_process_items(items, batch_size=3)
    
    print(f"\nBatch Processing:")
    print(f"Original items: {items}")
    print(f"Batches of 3: {batches}")




# Demonstrate common algorithms implemented with lists
def list_algorithms_showcase():
    
    # Binary search (requires sorted list)
    def binary_search(sorted_list: List[int], target: int) -> Optional[int]:
        left, right = 0, len(sorted_list) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if sorted_list[mid] == target:
                return mid
            elif sorted_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return None
    
    # Merge two sorted lists into 1
    def merge_sorted_lists(list1: List[int], list2: List[int]) -> List[int]:
        merged = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                merged.append(list1[i])
                i += 1
            else:
                merged.append(list2[j])
                j += 1
        
        # Add remaining elements
        merged.extend(list1[i:])
        merged.extend(list2[j:])
        
        return merged
    
    # Quick sort implementation
    def quicksort(arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)
    
    # Demonstrate algorithms
    numbers = [64, 34, 25, 12, 22, 11, 90]
    sorted_numbers = sorted(numbers)
    
    print("Algorithm Demonstrations:")
    print(f"Original: {numbers}")
    print(f"Sorted: {sorted_numbers}")
    
    # Binary search
    target = 25
    index = binary_search(sorted_numbers, target)
    print(f"Binary search for {target}: found at index {index}")
    
    # Merge sorted lists
    list1 = [1, 3, 5, 7]
    list2 = [2, 4, 6, 8, 10]
    merged = merge_sorted_lists(list1, list2)
    print(f"Merge {list1} and {list2}: {merged}")
    
    # Quick sort
    unsorted = [3, 6, 8, 10, 1, 2, 1]
    quick_sorted = quicksort(unsorted)
    print(f"Quicksort {unsorted}: {quick_sorted}")



# Driver COde
if __name__ == "__main__":
    demonstrate_basic_lists()
    print("\n" + "="*60 + "\n")
    demonstrate_list_methods()
    print("\n" + "="*60 + "\n")
    advanced_list_operations()
    print("\n" + "="*60 + "\n")
    list_comprehension_mastery()
    print("\n" + "="*60 + "\n")
    performance_and_memory_tips()
    print("\n" + "="*60 + "\n")
    practical_list_examples()
    print("\n" + "="*60 + "\n")
    list_algorithms_showcase()