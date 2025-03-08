# Tabulation

Tabulation is an optimization technique used in dynamic programming to solve problems by solving all subproblems and storing their solutions in a table (usually an array or a 2D matrix). It builds the solution iteratively from the base cases up to the final solution. Unlike memoization, which is top-down, tabulation is a bottom-up approach.

## Key Concepts
- **Bottom-Up Approach**: Tabulation solves the problem by starting from the simplest subproblems and gradually solving more complex ones by building upon the solutions of smaller subproblems.
- **Table (or Array)**: A table is used to store the solutions to subproblems. These solutions are filled out iteratively, usually in a 1D or 2D array.
- **No Recursion**: Unlike memoization, tabulation doesn't involve recursion. Instead, the solutions are computed iteratively.

## How Tabulation Works
1. **Define the Table**: Start by creating a table (or array) that will store the solutions to subproblems.
2. **Base Case(s)**: Initialize the table with the base case(s) values, which are usually simple and easy to solve.
3. **Iterative Computation**: Solve each subproblem by filling in the table iteratively, using the values of previously solved subproblems.
4. **Final Solution**: The final solution to the problem is typically found in the last entry of the table (or array), depending on the problem's structure.

## Time Complexity
Tabulation generally has a time complexity of **O(n)** or **O(n * m)**, depending on the problem, where `n` and `m` represent the dimensions of the problem (e.g., the number of states or subproblems). Tabulation tends to be more efficient in terms of space and time than memoization in many cases, especially if the table size can be reduced or optimized.

## Common Examples
- **Fibonacci Sequence**: Using tabulation, we can compute the nth Fibonacci number by filling an array starting from the base cases (F(0) and F(1)).
- **0/1 Knapsack Problem**: Use a 2D array to store the maximum value that can be obtained for each weight and number of items considered, iterating over the choices.
- **Longest Common Subsequence (LCS)**: Use a 2D table to store the length of the LCS between two strings, and build up the solution from smaller substrings.
- **Coin Change Problem**: Build up a solution iteratively by filling a table that keeps track of the minimum number of coins needed for each possible amount.
- **Edit Distance (Levenshtein Distance)**: Use a 2D table to store the minimum number of operations required to transform one string into another.

## Advantages
- **Efficient**: Avoids the overhead of recursion and redundant computations by solving all subproblems iteratively.
- **No Recursion**: Unlike memoization, tabulation does not use recursion, which can make it more efficient in some situations.
- **Improved Space Complexity**: Depending on the problem, the space complexity may be reduced by using a 1D array or optimizing the storage of the table.

## Disadvantages
- **Space Complexity**: Tabulation may require a significant amount of space if the table is large, especially for problems with many states or dimensions.
- **Predefined Structure**: Tabulation requires that the problem be decomposed into subproblems that can be solved iteratively, which may not always be straightforward.
- **Less Intuitive**: For some problems, tabulation may be harder to implement or less intuitive than memoization, which often maps more naturally to recursive approaches.
