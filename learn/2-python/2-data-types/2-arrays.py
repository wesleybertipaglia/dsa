# Ordered: Yes
# Mutable: Yes
# Duplicates: Yes
# Indexing: Yes
# Different Data Types: Yes

# creating
empty_list = []
populated_list = [1, 2, 3, 4, 5, "a", True]

# properties
length = len(populated_list) # 7

# access
populated_list[0] # 1
populated_list[-1] # True

# modifying elements
populated_list[0] = 0
populated_list[-1] = False

# adding elements
populated_list.append(6)
populated_list.insert(0, 0) # (index, value) -> [0, 1, 2, 3, 4, 5, "a", True, 6]
populated_list.extend([7, 8, 9]) # (list) -> [1, 2, 3, 4, 5, "a", True, 6, 7, 8, 9]
concatenated_list = [1, 2, 3] + [4, 5, 6]

# removing elements
populated_list.pop() # (index = -1) -> 9 
populated_list.pop(0) # 0
populated_list.remove(8) # 8
del populated_list[0] # 1
populated_list.clear()

# slicing
populated_list[1:3] # from 1 to 3
populated_list[:3] # from start to 3
populated_list[3:] # from 4 to end
populated_list[:] # all elements
populated_list[::2] # every 2nd element
populated_list[::-1] # reverse list

# copying
copied_list = populated_list.copy()
sliced_list = populated_list[:]
list_constructor = list(populated_list)

# sorting
populated_list.sort()
populated_list.sort(reverse=True) # reverse order
sorted_list = sorted(populated_list)

# searching
index = populated_list.index(3) # 2
count = populated_list.count(3) # 1

# checking
is_in = 3 in populated_list # True
is_not_in = 3 not in populated_list # False

# reversing
populated_list.reverse()
populated_list = populated_list[::-1]
populated_list = list(reversed(populated_list))

# iterating
for element in populated_list:
    print(element)

for index, element in enumerate(populated_list):
    print(index, element)

for index in range(len(populated_list)):
    print(populated_list[index])

# nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# access
matrix[0][0] # 1

# iterating
for row in matrix:
    for element in row:
        print(element)
