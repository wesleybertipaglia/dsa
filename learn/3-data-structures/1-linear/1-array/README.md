# Arrays

An array is a collection of data elements stored in contiguous memory locations. It allows for efficient access and manipulation of data.

![Arrays](/assets/array.png)

## Characteristics of Arrays
- Uses sequential memory addresses.
- Fixed size (in most programming languages).
- Elements must be of the same data type.
- Supports both static and dynamic allocation (depending on the language).

## Time Complexity
- **Accessing an element**: O(1) - Direct indexing.
- **Adding/Removing elements**: O(n) - Requires shifting elements.
- **Searching for an element**:
  - Linear Search: O(n)
  - Binary Search (sorted arrays only): O(log n)

## Array Operations in Python

### Creating an Array
```python
arr = [1, 2, 3, 4, 5]  # List in Python (behaves like an array)
```

### Accessing Elements
```python
first_element = arr[0]  # O(1) operation
```

### Adding Elements
```python
arr.append(6)  # O(1) if no resizing required, O(n) otherwise
```

### Removing Elements
```python
del arr[2]  # O(n) because elements need to shift
```

### Iterating Over an Array
```python
for num in arr:
    print(num)
```

## Pros and Cons of Arrays

### Advantages
- Fast access to elements using indices.
- Efficient use of memory due to contiguous storage.
- Simplicity in implementation.

### Disadvantages
- Fixed size (in most languages, except dynamic arrays like Python lists).
- Expensive insertions and deletions due to shifting.
- Requires contiguous memory, which may be a limitation for large datasets.

## Conclusion
Arrays are fundamental data structures that provide fast element access and efficient memory usage. However, they come with trade-offs in insertion and deletion times. Choosing the right data structure depends on the specific use case.
