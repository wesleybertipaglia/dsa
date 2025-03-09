# Prefix Sum

The **Prefix Sum** technique is an optimization method used to efficiently compute range sums or cumulative sums of elements in an array. By storing the cumulative sums up to each index, you can calculate the sum of any subarray in constant time, making it particularly useful for problems where multiple range sum queries need to be answered efficiently.

The technique is often used in problems that require frequent summation of elements from an array or when you need to repeatedly calculate the sum of subarrays.

## Key Concepts
#### Prefix Sum Array
This is an auxiliary array where each element at index `i` represents the sum of all elements in the original array from index `0` to `i`.

#### Efficient Range Queries
Once the prefix sum array is built, the sum of any subarray can be computed in constant time by using the formula:

```python
Sum(i, j) = prefix_sum[j] - prefix_sum[i-1]
```

Where `prefix_sum[j]` is the sum of elements from index `0` to `j`, and `prefix_sum[i-1]` is the sum of elements from index `0` to `i-1`.

## Time Complexity
- **O(n)**: The time complexity to build the prefix sum array is **O(n)**, where `n` is the number of elements in the array. This is because you compute the sum of the array elements once.
- **O(1)**: The time complexity to query the sum of any subarray is **O(1)**, since you can directly access the precomputed prefix sums.

## Steps to Compute Prefix Sum
#### Initialization
Create an array `prefix_sum` with size `n + 1` (or `n` depending on implementation), where `prefix_sum[0] = 0` to account for the sum of an empty array.

#### Building the Prefix Sum Array
For each element in the original array, compute the cumulative sum up to that index and store it in the `prefix_sum` array.

#### Querying the Range Sum
For a given range `(i, j)`, the sum of elements in the range can be calculated as `prefix_sum[j] - prefix_sum[i-1]`.

## Example

Given an array: `[1, 2, 3, 4, 5]`

1. **Compute Prefix Sum**:
- `prefix_sum[0] = 0` (sum of no elements)
- `prefix_sum[1] = 1` (sum of the first element)
- `prefix_sum[2] = 3` (sum of the first two elements: 1 + 2)
- `prefix_sum[3] = 6` (sum of the first three elements: 1 + 2 + 3)
- `prefix_sum[4] = 10` (sum of the first four elements: 1 + 2 + 3 + 4)
- `prefix_sum[5] = 15` (sum of all elements: 1 + 2 + 3 + 4 + 5)

Prefix sum array: `[0, 1, 3, 6, 10, 15]`

2. **Query Range Sum (i=1, j=3)**:
- To find the sum from index `1` to `3`, you calculate:

```python
sum(1, 3) = prefix_sum[3] - prefix_sum[0] = 6 - 0 = 6
```

## Common Applications
1. **Range Sum Queries**:
- Prefix sum is commonly used when you need to answer multiple range sum queries on an array. After preprocessing the prefix sum array, each query can be answered in constant time.
- Example: Given an array of integers, calculate the sum of elements in a specified range multiple times.

2. **Subarray Sum Problems**:
- Problems that involve finding the sum of a subarray within a given range can be solved efficiently using the prefix sum technique.
 
3. **Finding Subarrays with Specific Properties**:
- The prefix sum technique can be used to find subarrays that meet specific criteria, such as a subarray with a sum equal to a target value, by leveraging the difference of prefix sums.

4. **Calculating Cumulative Sums**:
- Prefix sums can be used to compute cumulative sums for tasks such as tracking the cumulative total of sales, temperatures, or scores over time.

5. **2D Prefix Sum (Matrix Sum Queries)**:
- The prefix sum technique can be extended to two-dimensional matrices, where you can precompute the sum of all elements in the top-left submatrix up to any index `(i, j)` to quickly query the sum of any submatrix.

For a 2D array `arr`:

```python
prefix_sum[i][j] = arr[i][j] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]
```


## Advantages
#### Efficient Query Handling
The primary advantage of using prefix sum is the ability to answer range sum queries in constant time after an initial preprocessing step.

#### Time Complexity
Reduces the time complexity of range sum queries from **O(n)** to **O(1)** after the **O(n)** preprocessing step.

#### Space Efficiency
The space complexity is **O(n)** for the prefix sum array, which is quite efficient for problems requiring multiple range sum queries.

## Disadvantages
#### Space Complexity
While the space complexity is **O(n)**, for extremely large arrays, this may not be ideal as it requires extra space.

#### Static Data
Prefix sum is ideal for static data where the array doesn’t change frequently. If the data is frequently updated, it may not be efficient to recompute the prefix sum after each update.

#### Limited to Sum Queries
This technique is primarily used for sum-related queries and does not directly work for other types of range queries (e.g., finding the maximum in a range).
