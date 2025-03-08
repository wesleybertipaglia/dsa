# Greedy Algorithm

## Introduction
The Greedy Algorithm is a problem-solving technique that makes a sequence of choices, each of which looks the best at the moment, with the hope that these local optimal choices will lead to a globally optimal solution. Greedy algorithms are used for optimization problems and work when the problem has the "greedy-choice property" and "optimal substructure."

## Key Concepts
- **Greedy Choice Property**: At each step, a locally optimal choice is made with the hope that these local choices lead to a globally optimal solution.
- **Optimal Substructure**: The problem can be solved by combining optimal solutions to its subproblems.
- **Greedy Strategy**: Makes decisions based solely on the current situation without considering the future consequences.

## Steps of a Greedy Algorithm
1. **Initialization**: Start by setting up an empty solution set or structure.
2. **Greedy Selection**: At each step, choose the best option available based on the current state of the problem.
3. **Feasibility Check**: Ensure that the selected choice does not violate any constraints and is feasible.
4. **Solution Update**: Update the solution based on the selected choice.
5. **Repeat**: Continue the process until the solution is complete or all options have been explored.

## Time Complexity
The time complexity of greedy algorithms depends on the problem and how the greedy choices are selected. In many cases, greedy algorithms have a time complexity of:

```
O(n log n)
```

Where `n` is the number of elements being considered. However, the complexity varies based on the specific problem and the sorting or decision-making process involved.

## Common Examples
- **Activity Selection Problem**: Choosing the maximum number of activities that don't overlap, given their start and finish times.
- **Huffman Coding**: A method for data compression by assigning variable-length codes to characters, with shorter codes for more frequent characters.
- **Fractional Knapsack Problem**: Given a set of items with weights and values, maximize the value by taking fractional amounts of items while staying within a weight limit.
- **Prim's Algorithm**: Finding the Minimum Spanning Tree (MST) in a weighted graph by starting with a vertex and adding the shortest edge to the tree.
- **Dijkstra’s Algorithm**: Finding the shortest path from a source node to all other nodes in a graph with weighted edges.

## Advantages
- Simple and easy to implement.
- Fast and efficient for problems that satisfy the greedy-choice property and optimal substructure.
- Often provides a good approximation to the optimal solution for complex problems.

## Disadvantages
- **No Guarantee of Global Optimality**: Greedy algorithms do not always lead to the globally optimal solution for all problems. They only ensure locally optimal solutions.
- **Problem-Specific**: Greedy algorithms only work for problems that satisfy the greedy-choice property and optimal substructure.
- **May Not Work for All Problems**: Some problems require a more exhaustive or systematic search for the optimal solution (e.g., dynamic programming, backtracking).
