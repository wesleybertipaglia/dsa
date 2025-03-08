# Memoization

Memoization is an optimization technique used to improve the efficiency of recursive algorithms by storing the results of expensive function calls and returning the cached result when the same inputs occur again. It is a key technique often used in dynamic programming to avoid redundant calculations and improve performance.

## Key Concepts
- **Caching Results**: Storing the results of function calls in a cache (usually in a dictionary or array) so that subsequent calls with the same parameters can be returned directly from the cache.
- **Recursive Function**: Memoization is particularly useful in recursive algorithms where the same subproblems are solved multiple times.
- **Avoiding Redundancy**: By remembering the results of subproblems, memoization reduces the number of function calls, leading to significant performance improvement.

## How Memoization Works
1. **Initial Function Call**: When a function is first called, it computes the result and stores it in a cache.
2. **Subsequent Calls**: If the function is called again with the same parameters, the result is retrieved from the cache instead of being recomputed.
3. **Cache Lookup**: The cache is usually checked before performing any calculations to see if the result for the given input already exists.

## Time Complexity
The time complexity of an algorithm using memoization typically improves from exponential (as in the case of naive recursion) to polynomial, because each subproblem is solved only once.

For example:
- **Fibonacci Sequence with Memoization**: By memoizing the Fibonacci function, you reduce the time complexity from `O(2^n)` (for naive recursion) to `O(n)`.

## Common Examples
- **Fibonacci Sequence**: The naive recursive approach to finding Fibonacci numbers has exponential time complexity. Memoization allows storing previously computed Fibonacci numbers to optimize this.
- **Factorial Calculation**: Using memoization to store the results of factorials avoids recomputing the same factorial multiple times.
- **Dynamic Programming Problems**: Many dynamic programming problems, such as the 0/1 Knapsack Problem, Longest Common Subsequence (LCS), and the Coin Change Problem, use memoization to store intermediate results.
- **Pathfinding Problems**: Memoization can be used in grid-based pathfinding algorithms (e.g., finding the shortest path in a grid) to store already explored states and avoid recalculating them.

## Advantages
- **Efficiency**: Improves the time complexity of recursive algorithms by avoiding redundant calculations.
- **Simple to Implement**: Often easy to implement by adding a cache (e.g., a dictionary or list).
- **Optimal Substructure**: Works well for problems that exhibit overlapping subproblems (like many dynamic programming problems).

## Disadvantages
- **Space Complexity**: Memoization requires extra space to store the results of subproblems, which may lead to high memory usage.
- **Overhead**: While it reduces time complexity, there can be overhead from the additional space used for caching.
- **Not Always Applicable**: Memoization only works for problems where results are repeatedly computed with the same input; it’s not useful for problems with no overlapping subproblems.
