# Sorting Algorithms Overview

Sorting algorithms are methods for arranging data in a specified order, typically in ascending or descending order. Below is a summary of popular sorting algorithms.

## Selection Sort
Repeatedly selects the smallest (or largest) element from the unsorted part of the list and swaps it with the first unsorted element.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Best Use Case:** When minimizing memory writes is crucial.

## Insertion Sort
Builds the final sorted array one element at a time. It takes each element and inserts it into the correct position relative to the already sorted part of the array.

- **Time Complexity:** O(n²)
- **Space Complexity:** O(1)
- **Best Use Case:** Small datasets or nearly sorted data.

## Merge Sort
A divide-and-conquer algorithm that splits the list into two halves, sorts them recursively, and then merges the sorted halves back together.

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Best Use Case:** Large datasets where stable sorting is required.

## Quick Sort
A divide-and-conquer algorithm that selects a pivot and partitions the list into two sublists: elements less than the pivot and elements greater than the pivot. The sublists are then sorted recursively.

- **Time Complexity:** O(n log n) (average), O(n²) (worst)
- **Space Complexity:** O(log n) (average)
- **Best Use Case:** Large datasets and when average time complexity is more important than the worst case.

---

## Summary Table

| Algorithm         | Time Complexity (Worst) | Space Complexity | Stable  |
|-------------------|-------------------------|------------------|---------|
| Selection Sort    | O(n²)                   | O(1)             | No      |
| Insertion Sort    | O(n²)                   | O(1)             | Yes     |
| Merge Sort        | O(n log n)              | O(n)             | Yes     |
| Quick Sort        | O(n²)                   | O(log n)         | No      |

---

## Key Points
- **Comparison-based algorithms** like Merge Sort, Quick Sort, and Heap Sort are ideal for general use with larger datasets.
- **Non-comparison-based algorithms** like Radix Sort, Counting Sort, and Bucket Sort work efficiently when the data is constrained to certain conditions (like integer ranges).
- **Stable sorting** ensures that elements with equal values retain their original relative order.

Choosing the right sorting algorithm depends on factors like dataset size, type of data, and whether stability is required.
