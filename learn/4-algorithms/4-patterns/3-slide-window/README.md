# Sliding Window

Is an efficient algorithmic technique used to solve problems involving contiguous subarrays or substrings. It helps reduce the time complexity by avoiding redundant computations in problems that require checking or processing subarrays or substrings of a fixed or variable length. The sliding window technique uses two pointers (or indices) to create a "window" that moves across the data structure, allowing you to optimize the process.

## Key Concepts
#### Window
A contiguous section of the array (or string) that is examined in each step. The window can have a fixed size or a dynamic size.

#### Sliding the Window
The window is moved across the data structure by incrementally adjusting the start and end indices of the window, typically from left to right.

#### Efficiency
This technique helps to avoid redundant calculations that occur when recalculating the result from scratch every time for overlapping subarrays or substrings.

## Types of Sliding Window

### Fixed-size Sliding Window
- In this case, the size of the window remains constant, and you move it across the data structure one element at a time.
- **Example problem**: Finding the maximum sum of a subarray of size `k`.

### Variable-size Sliding Window
- In this case, the size of the window is not fixed. The window grows or shrinks based on certain conditions (e.g., meeting a target sum or condition).
- **Example problem**: Finding the smallest subarray with a sum greater than or equal to a given target.

## Time Complexity
- **O(n)**: The sliding window technique usually results in **O(n)** time complexity because each element in the data structure is processed only once. Both the start and end pointers move across the array, and each element is added or removed from the window once.

## Common Applications

### Maximum/Minimum Sum Subarray of Fixed Size
- Given an array, find the maximum (or minimum) sum of a contiguous subarray of size `k`. 
- **Example**: Given the array `[2, 1, 5, 1, 3, 2]` and `k = 3`, find the maximum sum of any subarray of length `k`.
- **Approach**: Use a sliding window to calculate the sum of the first `k` elements, then slide the window one element at a time while updating the sum by adding the next element and removing the first element.

```python
def maxSumSubarray(arr, k):
    window_sum = sum(arr[:k])  # Initial sum of first k elements
    max_sum = window_sum
    
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Slide the window
        max_sum = max(max_sum, window_sum)
    
    return max_sum
```

### Finding Substrings or Subarrays with a Specific Sum or Condition

- For example, finding the smallest subarray whose sum is greater than or equal to a target value.
- **Example**: Given an array [2, 1, 5, 2, 3, 2] and a target sum of 7, find the smallest subarray whose sum is greater than or equal to 7.
- **Approach**: Expand the window to include more elements, and once the sum exceeds the target, shrink the window from the left to find the smallest valid subarray.

```python
def smallestSubarraySum(arr, target):
    window_sum = 0
    min_length = float('inf')
    left = 0
    
    for right in range(len(arr)):
        window_sum += arr[right]  # Expand the window by including arr[right]
        
        while window_sum >= target:  # Shrink the window to find minimum length
            min_length = min(min_length, right - left + 1)
            window_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0
```

### Longest Substring Without Repeating Characters

- Given a string, find the length of the longest substring without repeating characters.
- **Approach**: Use the sliding window technique with two pointers (start and end). As the end pointer moves across the string, adjust the start pointer to maintain a valid substring without duplicates.

```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_len = 0
    
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove characters until no duplicates
            left += 1
        char_set.add(s[right])
        max_len = max(max_len, right - left + 1)
    
    return max_len
```

### Sliding Window for Pattern Matching

- The sliding window is also useful for searching patterns or substrings in larger strings, especially when both the string and the pattern are moving simultaneously.

### Subarray or Substring with At Most K Distinct Elements

- Given an array or string, find the longest subarray (or substring) with at most k distinct elements.
- **Approach**: Use the sliding window to expand the window and count the distinct elements, adjusting the window's size as necessary.

## Advantages
#### Efficiency
Reduces the time complexity of problems that would otherwise require nested loops or brute force, often transforming solutions from O(n²) to O(n).

#### Memory Usage
The sliding window technique often requires only a small, fixed amount of extra memory, especially if a fixed-size window is used.

#### Simplicity
The algorithm is easy to implement and doesn't require complex data structures.

## Disadvantages
#### Limited Applicability
The sliding window technique is only useful for problems that involve contiguous subarrays or substrings. It may not be applicable for problems that require non-contiguous selections.

#### Edge Cases
Some problems may require additional handling of edge cases, such as empty arrays, strings, or cases with no valid subarray.
