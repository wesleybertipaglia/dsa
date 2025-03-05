# Stack

A stack is a linear data structure that follows the **Last In, First Out (LIFO)** principle, meaning the last element added is the first one to be removed.

![stack](/assets/stack.png)

## Characteristics of a Stack
- Operates on the **LIFO** principle (last in, first out).
- Elements are added (pushed) and removed (popped) from the **top** of the stack.
- Can be implemented using arrays or linked lists.

## Time Complexity
- **Push (Adding an element)**: O(1)
- **Pop (Removing an element)**: O(1)
- **Peek (Accessing the top element)**: O(1)
- **Search**: O(n)

## Stack Operations in Python

### Implementing a Stack Using a List
```python
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)  # O(1)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # O(1)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]  # O(1)
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
```

### Implementing a Stack Using a Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node  # O(1)
    
    def pop(self):
        if self.top is None:
            return None
        popped_data = self.top.data
        self.top = self.top.next  # O(1)
        return popped_data
    
    def peek(self):
        return self.top.data if self.top else None
    
    def is_empty(self):
        return self.top is None
```

## Pros and Cons of Stacks

### Advantages
- **Fast operations**: Push and pop are O(1).
- **Efficient memory usage**: No shifting like arrays.
- **Used in recursion, function calls, and undo mechanisms.**

### Disadvantages
- **Limited access**: Can only access the top element.
- **Fixed size in array-based implementations**.

## Use Cases of Stacks
- **Function call management** (recursion, backtracking).
- **Undo/Redo operations** (text editors, IDEs).
- **Expression evaluation** (postfix, prefix, infix conversions).
- **Browser history navigation**.

## Alternative Data Structures
- **Queues**: Follow First In, First Out (FIFO) instead of LIFO.
- **Deque (Double-ended Queue)**: Allows insertion and removal from both ends.
- **Linked Lists**: Provide more flexibility but require extra memory for pointers.

## Conclusion
Stacks are essential data structures used for LIFO operations, making them ideal for managing recursive calls, history tracking, and expression evaluation. The choice between an array-based or linked-list-based stack depends on memory and performance needs.
