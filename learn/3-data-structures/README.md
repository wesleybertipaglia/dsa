# Data Structures

Data structures are methods for organizing and storing data efficiently, allowing for quick access and modifications. They define how data is laid out and managed in a computer's memory.

## How Storage Works

### RAM (Random Access Memory)
Variables are stored in RAM for quick access during program execution.

### Bytes
- A **byte** consists of 8 bits and is the basic unit of memory storage.
- A byte can represent numbers, characters, or other data types.

### Bits
- A **bit** is the smallest unit of data, represented as either 0 or 1.
- Bits form binary data, which is the fundamental language for computers.

## Storing Data Types

### Integer (int)
- An **integer** typically takes up **4 bytes** (32 bits) of memory, though it can vary by system architecture.
- Example: The integer 42 is stored as `00000000 00000000 00000000 00101010`.

### Other Data Types
- **Float**: Typically takes **4 bytes** for single precision or **8 bytes** for double precision.
- **Character (char)**: Usually takes **1 byte** for storing a single character using ASCII or Unicode encoding.

## Storing Data Structures

### Array of Integers
- An **array** is a collection of elements of the same type, stored in **continuous memory**.
- Each integer typically takes **4 bytes**.
- Example: An array of 3 integers `[1, 2, 3]` would occupy **12 bytes** (3 * 4 bytes).
- **Memory Layout**: Elements are placed consecutively in memory:

```
[1, 2, 3]

1 -> #f00
2 -> #f04
3 -> #f08
```

### Linked List
- A **linked list** is a collection of elements where each element (called a node) contains data and a reference (pointer) to the next node in the list.
- Unlike arrays, linked lists do not require **continuous memory**.
- Each node typically contains:
  - A **data** field (for example, an integer).
  - A **pointer** field (which holds the memory address of the next node).
- Memory Usage:
  - If an integer node is stored, it may occupy **4 bytes** for the data and **4 bytes** for the pointer (on a 32-bit system).
  - A linked list with `n` nodes will use more memory than an array because of the extra pointers.

```
Node 1: (data = 1, next = address of Node 2) 
Node 2: (data = 2, next = address of Node 3) 
Node 3: (data = 3, next = NULL)

Node 1 -> #f28
Node 2 -> #f45
Node 3 -> #f83
```