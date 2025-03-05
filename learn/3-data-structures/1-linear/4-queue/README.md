# Queue

A queue is a linear data structure that follows the **First In, First Out (FIFO)** principle, meaning the first element added is the first one to be removed.

![queues](/assets/queue.png)

## Characteristics of a Queue
- Operates on the **FIFO** principle (first in, first out).
- Elements are added (**enqueue**) at the rear and removed (**dequeue**) from the front.
- Can be implemented using arrays or linked lists.

## Time Complexity
- **Enqueue (Adding an element)**: O(1)
- **Dequeue (Removing an element)**: O(1)
- **Peek (Accessing the front element)**: O(1)
- **Search**: O(n)

## Types of Queues
- **Simple Queue**: Standard FIFO behavior.
- **Circular Queue**: The rear connects back to the front to reuse space.
- **Double-ended Queue (Deque)**: Allows insertion and deletion from both ends.
- **Priority Queue**: Elements are dequeued based on priority instead of order.

## Queue Operations in Python

### Implementing a Queue Using a List
```python
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)  # O(1)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # O(n) due to shifting
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]  # O(1)
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
```

### Implementing a Queue Using a Linked List
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node  # O(1)
    
    def dequeue(self):
        if self.front is None:
            return None
        dequeued_data = self.front.data
        self.front = self.front.next  # O(1)
        if self.front is None:
            self.rear = None
        return dequeued_data
    
    def peek(self):
        return self.front.data if self.front else None
    
    def is_empty(self):
        return self.front is None
```

## Pros and Cons of Queues

### Advantages
- **Efficient operations**: Enqueue and dequeue are O(1) (in linked list implementation).
- **Useful for scheduling and buffering tasks.**

### Disadvantages
- **Limited access**: Can only access elements in FIFO order.
- **Array-based queues require shifting elements during dequeue (O(n) time complexity).**

## Use Cases of Queues
- **Task scheduling** (CPU scheduling, printer queues).
- **Handling requests in web servers.**
- **Breadth-first search (BFS) in graph algorithms.**
- **Message queues in asynchronous processing.**

## Alternative Data Structures
- **Stacks**: Follow Last In, First Out (LIFO) instead of FIFO.
- **Deque**: Allows operations from both ends.
- **Priority Queue**: Orders elements by priority instead of insertion order.

## Conclusion
Queues are fundamental data structures used for FIFO-based processing. They are widely used in scheduling, buffering, and managing sequential tasks efficiently. The choice of implementation (array or linked list) depends on performance requirements.
