# Dynamic Programming (DP)

Dynamic Programming is an optimization technique used to solve problems by breaking them down into simpler subproblems and storing the results of these subproblems to avoid redundant computations. It is particularly useful for problems that have overlapping subproblems and optimal substructure, meaning that optimal solutions to subproblems can be used to construct an optimal solution to the overall problem.

## Key Concepts
- **Overlapping Subproblems**: The problem can be divided into smaller subproblems that are solved independently but are used repeatedly throughout the problem.
- **Optimal Substructure**: The problem’s optimal solution can be constructed from the optimal solutions of its subproblems.
- **Memoization**: Storing the results of expensive function calls and reusing them when the same calculations are needed again (Top-Down approach).
- **Tabulation**: Solving the problem by iteratively building up a table (usually a 2D array) from the base cases (Bottom-Up approach).

## Steps of Dynamic Programming
1. **Characterize the Structure of the Optimal Solution**: Break the problem into smaller subproblems and define the optimal solution in terms of these subproblems.
2. **Define the Value of the Subproblems**: Develop a recursive formula or recurrence relation to express the solution of a problem as a function of the solutions to its subproblems.
3. **Compute the Value of the Optimal Solution**: Use either memoization (top-down) or tabulation (bottom-up) to compute the optimal solution by solving subproblems once and storing their results.
4. **Reconstruct the Solution (Optional)**: If needed, reconstruct the solution from the stored values (often done in pathfinding problems).

## Time Complexity
The time complexity of Dynamic Programming is typically much better than brute force methods because redundant calculations are avoided. The time complexity often depends on the number of subproblems and the amount of work done for each subproblem. It’s generally expressed as:

```
O(n * m) or O(n^2)
```

Where `n` and `m` are the problem-specific parameters (e.g., length of the input or number of states).

## Common Examples
- **Fibonacci Sequence**: Computing the nth Fibonacci number by breaking down the problem into smaller subproblems and storing the results.
- **0/1 Knapsack Problem**: Finding the maximum value of items that can be placed in a knapsack with a weight limit.
- **Longest Common Subsequence (LCS)**: Finding the longest subsequence common to two sequences.
- **Matrix Chain Multiplication**: Determining the most efficient way to multiply a chain of matrices.
- **Coin Change Problem**: Finding the minimum number of coins needed to make a certain amount from a set of coin denominations.
- **Edit Distance (Levenshtein Distance)**: Finding the minimum number of operations (insertions, deletions, substitutions) to convert one string to another.

## Advantages
- Avoids redundant computations by storing solutions to subproblems.
- Makes solving complex problems feasible by breaking them down into smaller, manageable subproblems.
- Significantly reduces time complexity compared to brute force approaches.

## Disadvantages
- Requires extra space to store solutions of subproblems.
- May not be applicable for all problems, as they need to exhibit overlapping subproblems and optimal substructure.
- Some DP problems may still have high time complexity depending on the number of subproblems.
