# Demonstration of Python Collections: Lists, Sets, Tuples

# Lists Examples
print("Lists Examples")
my_list = [1, 2, 3, 4]
my_list.append(5)
my_list.insert(1, 'inserted')
my_list.extend([6, 7, 8])
print("Extended List:", my_list)
my_list.remove('inserted')
popped_item = my_list.pop(0)
print("Modified List after removing elements:", my_list)
my_list.sort(reverse=True)
print("Sorted List:", my_list)
new_list = my_list.copy()
print("Copied List:", new_list)
sub_numbers = my_list[1:4]
print("Sliced List [1:4]:", sub_numbers)
reversed_numbers = my_list[::-1]
print("Reversed List:", reversed_numbers)

# Sets Examples
print("\nSets Examples")
my_set = {1, 2, 3, 2}
my_set.add(4)
my_set.discard(5)  # No error if element not found
print("Unique Elements Set:", my_set)
union_set = my_set.union({4, 5})
intersection_set = my_set.intersection({2, 3, 5})
difference_set = my_set.difference({3, 4})
print("Union Set:", union_set)
print("Intersection Set:", intersection_set)
print("Difference Set:", difference_set)

# Tuples Examples
print("\nTuples Examples")
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)
# Trying to change a value of a tuple will result in TypeError
# my_tuple[1] = 4  # Uncommenting this line will raise an error
tuple_packed = 4, 5, 6
x, y, z = tuple_packed
print("Unpacked Tuple:", x, y, z)
print("Count of 1 in Tuple:", my_tuple.count(1))
print("Index of 2 in Tuple:", my_tuple.index(2))

# Function Returning Multiple Values Using Tuples
def min_max(values):
    return min(values), max(values)

min_val, max_val = min_max([10, 20, 30, 40, 50])
print("Minimum and Maximum Values:", min_val, max_val)

# Comprehensive Lists Examples
print("\nComprehensive Lists Examples")
# Creating a list with mixed types
mixed_list = [1, "apple", 3.14, [1, 2, 3]]
print("Mixed List:", mixed_list)

# Accessing list elements
print("First element:", mixed_list[0])
print("Last element (negative indexing):", mixed_list[-1])

# List slicing
print("Sliced part of the list (1-3):", mixed_list[1:3])

# Removing elements by value and by index
mixed_list.remove("apple")  # Removing by value
del mixed_list[0]  # Removing by index
print("List after deletions:", mixed_list)

# Nested list operations
nested_list = [[1, 2], [3, 4]]
nested_list[0].append(3)
print("Nested List Modification:", nested_list)

# Comprehensive Sets Examples
print("\nComprehensive Sets Examples")
# Checking membership
sample_set = {1, 2, 3, 4, 5}
print("Is 3 in the set?", 3 in sample_set)
print("Is 6 not in the set?", 6 not in sample_set)

# Symmetric difference
another_set = {4, 5, 6}
print("Symmetric Difference:", sample_set.symmetric_difference(another_set))

# Adding multiple elements (using update)
sample_set.update([5, 6, 7])
print("Updated Set:", sample_set)

# Comprehensive Tuples Examples
print("\nComprehensive Tuples Examples")
# Tuple concatenation
tuple_one = (1, 2, 3)
tuple_two = (4, 5, 6)
concatenated_tuple = tuple_one + tuple_two
print("Concatenated Tuple:", concatenated_tuple)

# Tuples in dictionaries as keys
tuple_dict = {(1, 2): "tuple_as_key", (3, 4): "another_tuple_as_key"}
print("Dictionary with Tuple Keys:", tuple_dict)
print("Accessing via tuple key (1,2):", tuple_dict[(1, 2)])

# Repeating tuples
repeated_tuple = tuple_one * 3
print("Repeated Tuple:", repeated_tuple)

# Using tuples in a loop
for item in tuple_one:
    print(f"Tuple item: {item}")

# Function that returns a tuple
def get_stats(numbers):
    return max(numbers), min(numbers), sum(numbers) / len(numbers)

stats = get_stats([10, 20, 30, 40, 50])
print("Stats (Max, Min, Avg):", stats)
