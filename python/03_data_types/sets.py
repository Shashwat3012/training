from typing import Set, FrozenSet, Any
import time
import random


# Set creation and properties
def demonstrate_basic_sets():
    # Different ways to create sets
    empty_set = set()  # Note: {} creates a dict, not a set
    numbers_set = {1, 2, 3, 4, 5}
    string_set = {"apple", "banana", "cherry"}
    mixed_set = {1, "hello", 3.14, True}
    
    print("Set Creation:")
    print(f"Empty set: {empty_set} (type: {type(empty_set).__name__})")
    print(f"Numbers set: {numbers_set}")
    print(f"String set: {string_set}")
    print(f"Mixed set: {mixed_set}")
    
    # Set from other iterables
    list_to_set = set([1, 2, 2, 3, 3, 4])  # Duplicates removed
    string_to_set = set("hello")  # Each character as element
    
    print(f"\nFrom other iterables:")
    print(f"List to set (duplicates removed): {list_to_set}")
    print(f"String to set: {string_to_set}")
    
    # Set comprehension
    even_squares = {x**2 for x in range(10) if x % 2 == 0}
    print(f"Set comprehension (even squares): {even_squares}")




# Set Methods
def demonstrate_set_methods():
    fruits = {"apple", "banana", "cherry", "date"}
    
    print("Set Methods:")
    print(f"Original set: {fruits}")
    
    # Adding elements
    fruits.add("elderberry")
    print(f"After add('elderberry'): {fruits}")
    
    fruits.update(["fig", "grape", "kiwi"])
    print(f"After update(['fig', 'grape', 'kiwi']): {fruits}")
    
    # Removing elements
    fruits.remove("banana")  # Raises KeyError if not found
    print(f"After remove('banana'): {fruits}")
    
    discarded = fruits.discard("mango")  # No error if not found
    print(f"After discard('mango'): {fruits}")
    
    popped = fruits.pop()  # Removes arbitrary element
    print(f"After pop(): {fruits} (removed: {popped})")
    
    # Membership testing
    print(f"\nMembership testing:")
    print(f"'apple' in fruits: {'apple' in fruits}")
    print(f"'banana' in fruits: {'banana' in fruits}")
    
    # Set size and emptiness
    print(f"Set length: {len(fruits)}")
    print(f"Is empty: {len(fruits) == 0}")



#  Maths OPerations
def demonstrate_set_operations():
    # Sample sets for operations
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    set_c = {1, 2}
    
    print("Set Operations:")
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    print(f"Set C: {set_c}")
    
    # Union (elements in either set)
    union_result = set_a | set_b  # or set_a.union(set_b)
    print(f"\nUnion A | B: {union_result}")
    
    # Intersection (elements in both sets)
    intersection_result = set_a & set_b  # or set_a.intersection(set_b)
    print(f"Intersection A & B: {intersection_result}")
    
    # Difference (elements in first but not second)
    difference_result = set_a - set_b  # or set_a.difference(set_b)
    print(f"Difference A - B: {difference_result}")
    print(f"Difference B - A: {set_b - set_a}")
    
    # Symmetric difference (elements in either but not both)
    sym_diff_result = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
    print(f"Symmetric difference A ^ B: {sym_diff_result}")
   
   # Set relationships
    print(f"\nSet Relationships:")
    print(f"C is subset of A: {set_c <= set_a}")  # or set_c.issubset(set_a)
    print(f"A is superset of C: {set_a >= set_c}")  # or set_a.issuperset(set_c)
    print(f"A and B are disjoint: {set_a.isdisjoint(set_b)}")
    
    # Update operations (modify original set)
    original_set = {1, 2, 3}
    print(f"\nUpdate operations on {original_set}:")
    
    test_set = original_set.copy()
    test_set |= {4, 5}  # Union update
    print(f"After |= {{4, 5}}: {test_set}")
    
    test_set = original_set.copy()
    test_set &= {2, 3, 4}  # Intersection update
    print(f"After &= {{2, 3, 4}}: {test_set}")
    
    test_set = original_set.copy()
    test_set -= {2}  # Difference update
    print(f"After -= {{2}}: {test_set}")
    
    test_set = original_set.copy()
    test_set ^= {3, 4, 5}  # Symmetric difference update
    print(f"After ^= {{3, 4, 5}}: {test_set}")




# Show immutable sets (frozenset) usage
def demonstrate_frozen_sets():
   # Creating frozen sets
   frozen_nums = frozenset([1, 2, 3, 4, 5])
   frozen_colors = frozenset({"red", "green", "blue"})
   
   print("Frozen Sets (Immutable):")
   print(f"Frozen numbers: {frozen_nums}")
   print(f"Frozen colors: {frozen_colors}")
   
   # Frozen sets can be dictionary keys (they're hashable)
   set_dict = {
       frozenset([1, 2, 3]): "First set",
       frozenset([4, 5, 6]): "Second set",
       frozenset(["a", "b"]): "Letter set"
   }
   
   print(f"\nFrozen sets as dictionary keys:")
   for key, value in set_dict.items():
       print(f"{key}: {value}")
   
   # Set operations work with frozen sets
   regular_set = {3, 4, 5, 6}
   intersection = frozen_nums & regular_set
   print(f"\nIntersection of frozen and regular set: {intersection}")
   
   # Frozen sets of frozen sets (nested immutable collections)
   nested_frozen = frozenset([
       frozenset([1, 2]),
       frozenset([3, 4]),
       frozenset([5, 6])
   ])
   print(f"Nested frozen sets: {nested_frozen}")




def practical_set_applications():
   # 1. Removing duplicates from data
   def remove_duplicates_demo():
       # Sample data with duplicates
       email_list = [
           "alice@example.com", "bob@example.com", "charlie@example.com",
           "alice@example.com", "diana@example.com", "bob@example.com"
       ]
       
       unique_emails = list(set(email_list))
       
       print("Duplicate Removal:")
       print(f"Original emails ({len(email_list)}): {email_list}")
       print(f"Unique emails ({len(unique_emails)}): {unique_emails}")
       
       # Preserve order while removing duplicates
       def remove_duplicates_preserve_order(items):
           seen = set()
           result = []
           for item in items:
               if item not in seen:
                   seen.add(item)
                   result.append(item)
           return result
       
       ordered_unique = remove_duplicates_preserve_order(email_list)
       print(f"Ordered unique: {ordered_unique}")
   
   remove_duplicates_demo()
   
   # 2. Finding common elements across multiple lists
   def find_common_elements():
       # Sample datasets
       python_users = {"alice", "bob", "charlie", "diana", "eve"}
       java_users = {"bob", "charlie", "frank", "grace", "alice"}
       javascript_users = {"charlie", "diana", "frank", "henry", "alice"}
       
       # Users who know all three languages
       polyglots = python_users & java_users & javascript_users
       
       # Users who know at least one language
       all_users = python_users | java_users | javascript_users
       
       # Users who know exactly two languages
       python_java = (python_users & java_users) - javascript_users
       python_js = (python_users & javascript_users) - java_users
       java_js = (java_users & javascript_users) - python_users
       two_languages = python_java | python_js | java_js
       
       print(f"\nProgramming Language Users:")
       print(f"Python users: {python_users}")
       print(f"Java users: {java_users}")
       print(f"JavaScript users: {javascript_users}")
       print(f"Polyglots (all 3): {polyglots}")
       print(f"All users: {all_users}")
       print(f"Users with exactly 2 languages: {two_languages}")
   
   find_common_elements()
   
   # 3. Implementing tags system
   def tag_system_demo():
       articles = {
           "article1": {"python", "programming", "tutorial", "beginner"},
           "article2": {"javascript", "web", "frontend", "programming"},
           "article3": {"python", "data-science", "pandas", "advanced"},
           "article4": {"programming", "algorithms", "computer-science"},
           "article5": {"python", "web", "django", "backend"}
       }
       
       def find_articles_by_tags(required_tags: set, optional_tags: set = None):
           matching_articles = []
           
           for article_id, article_tags in articles.items():
               # Must have all required tags
               if required_tags.issubset(article_tags):
                   # Calculate relevance score based on optional tags
                   optional_matches = 0
                   if optional_tags:
                       optional_matches = len(article_tags & optional_tags)
                   
                   matching_articles.append((article_id, optional_matches, article_tags))
           
           # Sort by relevance (optional tag matches)
           matching_articles.sort(key=lambda x: x[1], reverse=True)
           return matching_articles
       
       # Search examples
       search1 = find_articles_by_tags({"python"}, {"tutorial", "beginner"})
       search2 = find_articles_by_tags({"programming"}, {"web", "advanced"})
       
       print(f"\nTag System Demo:")
       print("Articles and their tags:")
       for article, tags in articles.items():
           print(f"  {article}: {tags}")
       
       print(f"\nSearch for Python articles (prefer tutorial/beginner):")
       for article, score, tags in search1:
           print(f"  {article} (score: {score}): {tags}")
       
       print(f"\nSearch for programming articles (prefer web/advanced):")
       for article, score, tags in search2:
           print(f"  {article} (score: {score}): {tags}")
   
   tag_system_demo()




def performance_analysis():   
   # Membership testing performance
   def compare_membership_testing():
       """Compare membership testing across data structures."""
       
       size = 10000
       test_data = list(range(size))
       
       # Create different data structures
       test_list = test_data
       test_set = set(test_data)
       test_tuple = tuple(test_data)
       
       # Test membership for random elements
       test_elements = [random.randint(0, size-1) for _ in range(1000)]
       
       # Time list membership
       start = time.perf_counter()
       for element in test_elements:
           _ = element in test_list
       list_time = time.perf_counter() - start
       
       # Time set membership
       start = time.perf_counter()
       for element in test_elements:
           _ = element in test_set
       set_time = time.perf_counter() - start
       
       # Time tuple membership
       start = time.perf_counter()
       for element in test_elements:
           _ = element in test_tuple
       tuple_time = time.perf_counter() - start
       
       print("Membership Testing Performance:")
       print(f"List time: {list_time:.6f} seconds")
       print(f"Set time: {set_time:.6f} seconds")
       print(f"Tuple time: {tuple_time:.6f} seconds")
       print(f"Set is {list_time/set_time:.1f}x faster than list")
       print(f"Set is {tuple_time/set_time:.1f}x faster than tuple")
   
   compare_membership_testing()
   
   # Set operations performance
   def set_operations_performance():
       size1, size2 = 5000, 7000
       set1 = set(range(size1))
       set2 = set(range(size2//2, size2 + size2//2))
       
       operations = {
           "Union": lambda: set1 | set2,
           "Intersection": lambda: set1 & set2,
           "Difference": lambda: set1 - set2,
           "Symmetric Difference": lambda: set1 ^ set2
       }
       
       print(f"\nSet Operations Performance:")
       print(f"Set 1 size: {len(set1)}, Set 2 size: {len(set2)}")
       
       for op_name, operation in operations.items():
           start = time.perf_counter()
           result = operation()
           end = time.perf_counter()
           
           print(f"{op_name}: {end-start:.6f}s (result size: {len(result)})")
   
   set_operations_performance()



# Set usage code
def advanced_set_techniques():
   # 1. Set-based algorithms
   def find_duplicates_in_list(items):
       seen = set()
       duplicates = set()
       
       for item in items:
           if item in seen:
               duplicates.add(item)
           else:
               seen.add(item)
       
       return duplicates
   
   sample_list = [1, 2, 3, 2, 4, 5, 3, 6, 1, 7]
   dupes = find_duplicates_in_list(sample_list)
   print("Advanced Set Techniques:")
   print(f"Duplicates in {sample_list}: {dupes}")
   
   # 2. Set-based data filtering
   def filter_by_whitelist_blacklist(data, whitelist=None, blacklist=None):
       result = set(data)
       
       if whitelist:
           result &= whitelist  # Keep only whitelisted items
       
       if blacklist:
           result -= blacklist  # Remove blacklisted items
       
       return result
   
   all_items = {"apple", "banana", "cherry", "date", "elderberry", "fig"}
   whitelist = {"apple", "banana", "cherry", "grape"}  # grape not in all_items
   blacklist = {"banana", "date"}
   
   filtered = filter_by_whitelist_blacklist(all_items, whitelist, blacklist)
   print(f"\nFiltering example:")
   print(f"All items: {all_items}")
   print(f"Whitelist: {whitelist}")
   print(f"Blacklist: {blacklist}")
   print(f"Filtered result: {filtered}")
   
   # 3. Set-based graph algorithms
   def find_connected_components(edges):
       # Build adjacency representation
       graph = {}
       vertices = set()
       
       for u, v in edges:
           vertices.update([u, v])
           if u not in graph:
               graph[u] = set()
           if v not in graph:
               graph[v] = set()
           graph[u].add(v)
           graph[v].add(u)
       
       visited = set()
       components = []
       
       def dfs(vertex, component):
           if vertex in visited:
               return
           
           visited.add(vertex)
           component.add(vertex)
           
           for neighbor in graph.get(vertex, set()):
               dfs(neighbor, component)
       
       for vertex in vertices:
           if vertex not in visited:
               component = set()
               dfs(vertex, component)
               components.append(component)
       
       return components
   
   # Example graph edges
   graph_edges = [
       ('A', 'B'), ('B', 'C'), ('D', 'E'),
       ('F', 'G'), ('G', 'H'), ('H', 'F')
   ]
   
   components = find_connected_components(graph_edges)
   print(f"\nGraph connected components:")
   print(f"Edges: {graph_edges}")
   print(f"Components: {components}")

def set_best_practices():
   print("Set Best Practices:")
   
   # 1. Use sets for membership testing
   valid_extensions = {'.jpg', '.png', '.gif', '.bmp', '.svg'}
   
   def is_valid_image(filename):
       return any(filename.lower().endswith(ext) for ext in valid_extensions)
   
   test_files = ["photo.jpg", "document.pdf", "image.PNG", "video.mp4"]
   print("1. Membership testing:")
   for filename in test_files:
       print(f"  {filename}: {'Valid' if is_valid_image(filename) else 'Invalid'} image")
   
   # 2. Use sets for deduplication
   def deduplicate_preserving_order(items):
       seen = set()
       result = []
       for item in items:
           if item not in seen:
               seen.add(item)
               result.append(item)
       return result
   
   items_with_dupes = ['a', 'b', 'c', 'b', 'a', 'd', 'c', 'e']
   unique_items = deduplicate_preserving_order(items_with_dupes)
   print(f"\n2. Deduplication: {items_with_dupes} -> {unique_items}")
   
   # 3. Use sets for mathematical operations
   def analyze_survey_data():
       likes_pizza = {"Alice", "Bob", "Charlie", "Diana"}
       likes_pasta = {"Bob", "Diana", "Eve", "Frank"}
       likes_salad = {"Alice", "Charlie", "Eve", "Grace"}
       
       # People who like everything
       likes_all = likes_pizza & likes_pasta & likes_salad
       
       # People who like at least one
       likes_any = likes_pizza | likes_pasta | likes_salad
       
       # People who like exactly two dishes
       pizza_pasta = (likes_pizza & likes_pasta) - likes_salad
       pizza_salad = (likes_pizza & likes_salad) - likes_pasta
       pasta_salad = (likes_pasta & likes_salad) - likes_pizza
       likes_exactly_two = pizza_pasta | pizza_salad | pasta_salad
       
       return {
           'likes_all': likes_all,
           'likes_any': likes_any,
           'likes_exactly_two': likes_exactly_two,
           'total_respondents': len(likes_any)
       }
   
   survey_results = analyze_survey_data()
   print(f"\n3. Survey analysis:")
   for key, value in survey_results.items():
       print(f"  {key}: {value}")
   
   # 4. Use frozensets for immutable collections
   def create_permission_system():
       permissions = {
           'admin': frozenset(['read', 'write', 'delete', 'execute']),
           'editor': frozenset(['read', 'write']),
           'viewer': frozenset(['read']),
           'guest': frozenset()
       }
       
       def check_permission(role, action):
           """Check if role has permission for action."""
           return action in permissions.get(role, frozenset())
       
       return permissions, check_permission
   
   permissions, check_perm = create_permission_system()
   print(f"\n4. Permission system:")
   for role, perms in permissions.items():
       print(f"  {role}: {perms}")
   
   test_cases = [('admin', 'delete'), ('editor', 'delete'), ('viewer', 'read')]
   for role, action in test_cases:
       result = check_perm(role, action)
       print(f"  Can {role} {action}? {result}")



# Driver Code
if __name__ == "__main__":
   demonstrate_basic_sets()
   print("\n" + "="*60 + "\n")
   demonstrate_set_methods()
   print("\n" + "="*60 + "\n")
   demonstrate_set_operations()
   print("\n" + "="*60 + "\n")
   demonstrate_frozen_sets()
   print("\n" + "="*60 + "\n")
   practical_set_applications()
   print("\n" + "="*60 + "\n")
   performance_analysis()
   print("\n" + "="*60 + "\n")
   advanced_set_techniques()
   print("\n" + "="*60 + "\n")
   set_best_practices()