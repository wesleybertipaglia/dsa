# Searching Algorithms

Searching algorithms are techniques used to locate a specific element or value within a collection of data. Below is a summary of some common searching algorithms.

## Linear Search
The simplest searching algorithm, where each element is checked in sequence until the desired element is found or the end of the list is reached.

- **Time Complexity**: O(n), where n is the number of elements in the list.
- **Space Complexity**: O(1)
- **Use Case**: Best for small or unsorted lists.

### Example:
```python
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
```

## Binary Search
An efficient search algorithm for sorted lists. It works by repeatedly dividing the search interval in half. If the target value is less than the middle element, it narrows the search to the left half, otherwise to the right half.

- **Time Complexity**: O(log n), where n is the number of elements.
- **Space Complexity**: O(1) for iterative implementation, O(log n) for recursive implementation.
- **Use Case**: Best for large sorted arrays or lists.

### Example:
```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

## Conclusion
Different searching algorithms have different strengths and use cases. Here's a quick summary:

- **Linear Search**: Simple, works on unsorted lists.
- **Binary Search**: Efficient, works on sorted lists.

Choose the search algorithm based on the characteristics of the data and the size of the dataset.
