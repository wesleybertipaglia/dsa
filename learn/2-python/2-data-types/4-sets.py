# Ordered: No (unordered collection)
# Mutable: Yes
# Duplicates: No (all elements must be unique)
# Indexing: No
# Different Data Types: Yes

# creating
empty_set = set()
numbers = {1, 2, 3, 4, 5}

# properties
length = len(numbers)  # 5

# access
# Sets do not support indexing. You must convert to a list or iterate.

# add elements
numbers.add(6)  # {1, 2, 3, 4, 5, 6}
numbers.update([7, 8, 9])  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# remove elements
numbers.remove(1)  # {2, 3, 4, 5, 6, 7, 8, 9} - raises KeyError if element not found
numbers.discard(2)  # {3, 4, 5, 6, 7, 8, 9} - does not raise error if element not found
numbers.pop()  # removes and returns an arbitrary element
numbers.clear()  # clears all elements

# copying
numbers_copy = numbers.copy()  # {3, 4, 5, 6, 7, 8, 9}

# set operations

# union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a | set_b  # {1, 2, 3, 4, 5}

# intersection: elements in both set_a and set_b
intersection_set = set_a & set_b  # {3}

# difference: elements in set_a but not in set_b
difference_set = set_a - set_b  # {1, 2}

# symmetric difference: elements in set_a or set_b but not in both
symmetric_difference_set = set_a ^ set_b  # {1, 2, 4, 5}

# checking
is_in_set = 3 in numbers  # True
is_not_in_set = 10 not in numbers  # True

# iterating
for number in numbers:
    print(number)

# nested sets
# Sets cannot contain other sets directly because sets are mutable and therefore not hashable.
# however, sets can contain frozensets.
nested_set = {frozenset({1, 2, 3}), frozenset({4, 5, 6})}
for sub_set in nested_set:
    for number in sub_set:
        print(number)
