# Hash Tables

A hash table (or hash map) is a data structure that stores key-value pairs and uses a **hash function** to compute an index for storing values efficiently.

![Hash Table](/assets/hash-table.png)

## Characteristics of Hash Tables
- Provides **fast lookups, insertions, and deletions**.
- Uses a **hash function** to map keys to indices in an array.
- Handles **collisions** using techniques like chaining or open addressing.
- Ideal for applications that require quick data retrieval.

## Time Complexity
- **Insertion**: O(1) on average, O(n) in the worst case (due to collisions).
- **Deletion**: O(1) on average, O(n) in the worst case.
- **Search/Lookup**: O(1) on average, O(n) in the worst case.

## Collision Handling Techniques
- **Chaining**: Uses linked lists to store multiple values at the same index.
- **Open Addressing**: Searches for the next available slot in case of a collision.
- **Double Hashing**: Uses a secondary hash function to resolve collisions.

## Hash Table Operations in Python

### Implementing a Hash Table Using a Dictionary
```python
# Python's built-in dictionary functions as a hash table
hash_table = {}
hash_table['name'] = 'Alice'  # Insertion
print(hash_table['name'])  # Lookup
```

### Implementing a Hash Table Using Chaining
```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])
    
    def get(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None
    
    def remove(self, key):
        index = self.hash_function(key)
        self.table[index] = [pair for pair in self.table[index] if pair[0] != key]
```

## Pros and Cons of Hash Tables

### Advantages
- **Fast lookups and insertions (O(1) on average).**
- **Efficient for large datasets.**
- **Keys can be of any hashable type.**

### Disadvantages
- **Collisions can affect performance.**
- **Uses more memory compared to arrays and linked lists.**
- **Unordered storage (not ideal for ordered data retrieval).**

## Use Cases of Hash Tables
- **Database indexing** (key-value storage).
- **Caching mechanisms** (fast data retrieval).
- **Symbol tables in compilers and interpreters.**
- **Counting frequency of elements (histograms).**

## Alternative Data Structures
- **Arrays**: Suitable for sequential data but slower for searches.
- **Binary Search Trees (BSTs)**: Provide ordered storage with O(log n) lookup time.
- **Linked Lists**: Useful when order matters but have slower lookups.

## Conclusion
Hash tables offer fast insertions and lookups, making them ideal for applications that require constant-time access to data. However, collision management and memory overhead should be considered when implementing them.
