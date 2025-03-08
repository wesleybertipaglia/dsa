# Backtracking

Backtracking is a problem-solving algorithmic technique used to find solutions to problems incrementally, by exploring all possible options and abandoning those that fail to meet the desired criteria. It is often used for combinatorial problems where we need to explore multiple possible configurations.

## Key Concepts
- **Incremental Search**: The solution is built step by step, and each step involves making a decision based on the current configuration.
- **Pruning**: At each step, the algorithm checks if continuing further is worth it. If not, it "backtracks" and tries another possibility.
- **Recursive**: The process of exploration and backtracking is often implemented using recursion.

## Steps of Backtracking
1. **Choose**: Make a choice or decision for the current step.
2. **Explore**: Explore further by making recursive calls and attempting to build on the current choice.
3. **Unchoose (Backtrack)**: If the current choice leads to an invalid state or does not lead to a solution, undo the decision and backtrack to the previous state to try an alternative option.

## Time Complexity
The time complexity of backtracking problems can vary greatly depending on the problem structure, but it often involves exploring a large search space, making it exponential in nature:

```
O(b^d)
```

Where:
- `b` is the branching factor (number of choices at each step),
- `d` is the depth of the search tree (number of decisions or levels).

## Common Examples
- **N-Queens Problem**: Place `n` queens on an `n x n` chessboard such that no two queens threaten each other.
- **Sudoku Solver**: Fill a Sudoku grid by trying each possible number and backtracking when an invalid configuration is reached.
- **Subset Sum Problem**: Find if there is a subset of numbers that sums to a given value.
- **Permutations and Combinations**: Generate all possible permutations or combinations of a set of elements.
- **Graph Coloring**: Assign colors to the vertices of a graph such that no two adjacent vertices have the same color.

## Advantages
- Simple to implement.
- Can solve problems with large search spaces efficiently by pruning invalid paths early.
- Works well for combinatorial optimization problems.

## Disadvantages
- Can be inefficient for large search spaces, as it may explore many invalid possibilities.
- The performance heavily depends on the pruning (backtracking) strategy.
