# Hash Sets

A hash set is a data structure that stores a collection of unique elements. It uses a **hash function** to map elements to indices in an array, providing efficient operations for adding, checking existence, and removing elements.

## Characteristics of Hash Sets
- **Unique Elements**: Hash sets do not allow duplicate values.
- **Unordered**: The elements in a hash set are not stored in any particular order.
- **Efficient Operations**: Provides fast insertions, deletions, and lookups on average.
- Uses a **hash function** to calculate the index of the element in the underlying array.

## Time Complexity
- **Insertion**: O(1) on average, O(n) in the worst case (due to collisions).
- **Deletion**: O(1) on average, O(n) in the worst case.
- **Search/Lookup**: O(1) on average, O(n) in the worst case.
- **Check for Element Existence**: O(1) on average, O(n) in the worst case.

## Collision Handling in Hash Sets
- **Chaining**: Similar to hash tables, chaining is used to resolve collisions by storing multiple elements at the same index in a linked list.
- **Open Addressing**: Resolves collisions by probing the next available slot in the array.

## Hash Set Operations in Python

### Using Python's Built-in `set`

```python
# Python's built-in set provides a hash set implementation
hash_set = set()
hash_set.add(5)  # Insertion
hash_set.add(10)  # Insertion
print(5 in hash_set)  # Check if element exists
hash_set.remove(5)  # Deletion
```

### Custom Hash Set Implementation Using Chaining

```python
class HashSet:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def add(self, key):
        index = self.hash_function(key)
        if key not in self.table[index]:
            self.table[index].append(key)
    
    def contains(self, key):
        index = self.hash_function(key)
        return key in self.table[index]
    
    def remove(self, key):
        index = self.hash_function(key)
        if key in self.table[index]:
            self.table[index].remove(key)
```

## Advantages
- Fast membership testing (O(1) on average).
- Efficient for large datasets when you need to check or remove elements quickly.
- **No duplicates**: Automatically ensures that all elements are unique.

## Disadvantages
- **Collisions can affect performance**: Handling collisions can lead to slower operations in some cases.
- **Unordered**: Elements are not stored in any specific order.
- **Uses more memory**: Hash sets can use more memory compared to other collections like lists or arrays.

## Use Cases of Hash Sets
- **Checking for duplicates**: Ensures unique elements in a collection.
- **Fast membership testing**: Checking if an element exists in the set quickly.
- **Set operations**: Useful in performing union, intersection, and difference operations efficiently.

## Conclusion
Hash sets provide a highly efficient way to store unique elements, offering constant-time complexity for adding, checking, and removing elements in most cases. However, they come with the trade-off of using more memory and being unordered.