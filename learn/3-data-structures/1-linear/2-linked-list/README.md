# Linked Lists

A linked list is a linear data structure where elements (nodes) are stored in separate memory locations and connected via pointers.

![Linked List](/assets/linked-list.png)

## Characteristics of Linked Lists
- Dynamic size (can grow and shrink as needed).
- Non-contiguous memory allocation.
- Each node contains:
  - Data
  - A pointer to the next node (for singly linked lists).

## Types of Linked Lists
- **Singly Linked List**: Each node points to the next node.
- **Doubly Linked List**: Each node points to both the next and previous nodes.
- **Circular Linked List**: The last node points back to the first node.

## Time Complexity
- **Accessing an element**: O(n) - Sequential traversal is required.
- **Adding an element**:
  - Beginning: O(1)
  - Middle/End: O(n) (requires traversal)
- **Removing an element**:
  - Beginning: O(1)
  - Middle/End: O(n) (requires traversal)

## Linked List Operations in Python

### Creating a Node
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

### Creating a Linked List
```python
class LinkedList:
    def __init__(self):
        self.head = None
```

### Adding a Node at the Beginning
```python
def insert_at_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node
```

### Removing a Node
```python
def delete_node(self, key):
    temp = self.head
    if temp and temp.data == key:
        self.head = temp.next
        temp = None
        return
    prev = None
    while temp and temp.data != key:
        prev = temp
        temp = temp.next
    if temp is None:
        return
    prev.next = temp.next
    temp = None
```

### Traversing a Linked List
```python
def traverse(self):
    temp = self.head
    while temp:
        print(temp.data)
        temp = temp.next
```

## Pros and Cons of Linked Lists

### Advantages
- Efficient insertions and deletions (O(1) at the beginning).
- Dynamic memory allocation.
- No wasted memory due to fixed sizes like arrays.

### Disadvantages
- Slower access (O(n) vs. O(1) for arrays).
- Uses extra memory for pointers.

## Alternative Data Structures
- **Arrays**: Faster access but require shifting for insertions/deletions.
- **Hash Tables**: Faster lookups but require more memory.
- **Balanced Trees**: Provide better searching capabilities.

## Conclusion
Linked lists offer flexibility in memory management and efficient insertions/deletions, but they trade off fast random access. Choosing between arrays and linked lists depends on the specific use case.
