# Ordered: Yes (as of Python 3.7+)
# Mutable: Yes
# Duplicates: Values only
# Indexing: Keys only
# Different Data Types: Yes

# creating
empty_dict = {}
numbers = {'one': 1, 'two': 2, 'three': 3}

# properties
length = len(numbers)  # 3

# access
one = numbers['one']  # 1
# numbers['four']  # KeyError: 'four'

# modifying elements
numbers['one'] = 10  # {'one': 10, 'two': 2, 'three': 3}
numbers['four'] = 4  # {'one': 10, 'two': 2, 'three': 3, 'four': 4}

# adding elements
numbers['five'] = 5  # {'one': 10, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# removing elements
del numbers['one']  # {'two': 2, 'three': 3, 'four': 4, 'five': 5}
removed_value = numbers.pop('two')  # 2, {'three': 3, 'four': 4, 'five': 5}
numbers.popitem()  # removes and returns an arbitrary key-value pair
numbers.clear()  # clears all elements

# copying
numbers_copy = numbers.copy()
numbers_copy = dict(numbers)

# dict operations
keys = numbers.keys()  # dict_keys(['three', 'four', 'five'])
values = numbers.values()  # dict_values([3, 4, 5])
items = numbers.items()  # dict_items([('three', 3), ('four', 4), ('five', 5)])

# merging
other_numbers = {'six': 6, 'seven': 7}
numbers.update(other_numbers)  # {'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7}

# checking
is_in_dict = 'three' in numbers  # True
is_not_in_dict = 'one' not in numbers  # True

# iterating
for key in numbers:
    print(key, numbers[key])

for key, value in numbers.items():
    print(key, value)

# nested dictionaries
nested_dict = {
    'first': {'name': 'John', 'age': 30},
    'second': {'name': 'Doe', 'age': 25}
}
for key, sub_dict in nested_dict.items():
    for sub_key, sub_value in sub_dict.items():
        print(f"{key} -> {sub_key}: {sub_value}")

# default values
default_value = numbers.get('eight', 0)  # 0, if 'eight' does not exist

# dictionary comprehension
squares = {x: x*x for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
