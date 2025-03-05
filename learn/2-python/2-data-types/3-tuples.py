# Ordered: Yes
# Mutable: No (immutable)
# Duplicates: Yes
# Indexing: Yes
# Different Data Types: Yes

# creating
empty_tuple = ()
single_element_tuple = (1,)
numbers = (1, 2, 3, 4, 5)

# properties
length = len(numbers)  # 5

# access
first_number = numbers[0]  # 1
last_number = numbers[-1]  # 5

# modifying elements
# Tuples are immutable, so elements cannot be changed directly. You must create a new tuple.
numbers = (0, *numbers[1:-1], 6)  # (0, 2, 3, 4, 6)

# adding elements
# Tuples are immutable, so elements cannot be added directly. You must create a new tuple.
numbers = numbers + (7, 8, 9)  # (0, 2, 3, 4, 6, 7, 8, 9)

# removing elements
# Tuples are immutable, so elements cannot be removed directly. You must create a new tuple.
numbers = numbers[:1] + numbers[2:]  # remove the second element (index 1), resulting in (0, 3, 4, 6, 7, 8, 9)

# slicing
subset = numbers[1:3]  # (3, 4)
start_to_three = numbers[:3]  # (0, 3, 4)
from_four_to_end = numbers[3:]  # (6, 7, 8, 9)
all_elements = numbers[:]  # (0, 3, 4, 6, 7, 8, 9)
every_second_element = numbers[::2]  # (0, 4, 7, 9)
reversed_tuple = numbers[::-1]  # (9, 8, 7, 6, 4, 3, 0)

# copying
numbers_copy = numbers[:]  # (0, 3, 4, 6, 7, 8, 9)

# sorting
# Tuples are immutable, so sorting returns a new list instead.
sorted_numbers = tuple(sorted(numbers))  # (0, 3, 4, 6, 7, 8, 9)

# searching
index_of_4 = numbers.index(4)  # 2
count_of_3 = numbers.count(3)  # 1

# checking
is_in_tuple = 4 in numbers  # True
is_not_in_tuple = 10 not in numbers  # True

# reversing
# Tuples are immutable, so reversing returns a new tuple.
reversed_tuple = numbers[::-1]  # (9, 8, 7, 6, 4, 3, 0)

# iterating
for number in numbers:
    print(number)

# nested tuples
nested_tuple = ((1, 2, 3), (4, 5, 6))
for sub_tuple in nested_tuple:
    for number in sub_tuple:
        print(number)
