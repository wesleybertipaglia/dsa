# Graph Algorithms

Graph algorithms are techniques used to solve problems related to graphs. A graph is a collection of nodes (vertices) connected by edges (links). These algorithms help in traversing, searching, and analyzing the structure and properties of graphs.

## 1. **Graph Representation**
Before we can perform operations, a graph needs to be represented. The two most common representations are:
- **Adjacency Matrix**: A 2D array where element `matrix[i][j]` is true if there's an edge between vertex `i` and `j`.
- **Adjacency List**: A list of lists, where each vertex has a list of connected vertices.

## 2. **Graph Traversal Algorithms**
Traversal algorithms are used to visit all the nodes in a graph.

### a. **Depth-First Search (DFS)**
- **Purpose**: Explore as far as possible along a branch before backtracking.
- **Time Complexity**: O(V + E) where V is vertices and E is edges.
- **Space Complexity**: O(V) due to recursion stack (or O(V) for an explicit stack).

### b. **Breadth-First Search (BFS)**
- **Purpose**: Explore all neighbors at the present depth level before moving on to nodes at the next depth level.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V) for the queue used in BFS.

## 3. **Shortest Path Algorithms**
These algorithms are used to find the shortest path between two vertices in a graph.

### a. **Dijkstra's Algorithm**
- **Purpose**: Find the shortest path from a single source to all other nodes in a weighted graph with non-negative weights.
- **Time Complexity**: O(V^2) for simple implementation, O(E + V log V) with priority queues.
- **Space Complexity**: O(V)

### b. **Bellman-Ford Algorithm**
- **Purpose**: Find the shortest path from a single source to all other nodes, works with negative weight edges.
- **Time Complexity**: O(VE)
- **Space Complexity**: O(V)

### c. **Floyd-Warshall Algorithm**
- **Purpose**: Find the shortest paths between all pairs of nodes in a weighted graph.
- **Time Complexity**: O(V^3)
- **Space Complexity**: O(V^2)

## 4. **Minimum Spanning Tree (MST) Algorithms**
These algorithms find the subset of edges that connect all vertices with the minimum total edge weight.

### a. **Kruskal's Algorithm**
- **Purpose**: Find the minimum spanning tree by sorting edges in increasing weight and adding them one by one if they don’t form a cycle.
- **Time Complexity**: O(E log E)
- **Space Complexity**: O(V + E)

### b. **Prim's Algorithm**
- **Purpose**: Build the MST by starting from an arbitrary vertex and adding the shortest edge that connects the tree to a vertex not in the tree.
- **Time Complexity**: O(V^2) (using a simple array), O(E + V log V) with a priority queue.
- **Space Complexity**: O(V)

## 5. **Topological Sorting**
- **Purpose**: Order vertices in a directed acyclic graph (DAG) such that for every directed edge `u -> v`, vertex `u` comes before `v`.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

### **Algorithm**: 
- **Kahn’s Algorithm** (BFS-based).
- **DFS-based Topological Sort**.

## 6. **Graph Connectivity Algorithms**
These algorithms check whether the graph is connected or find its connected components.

### a. **Union-Find / Disjoint Set**
- **Purpose**: Manage a partition of a set into disjoint subsets and supports efficient union and find operations.
- **Time Complexity**: O(α(V)) where α is the inverse Ackermann function, nearly constant.
- **Space Complexity**: O(V)

## 7. **Network Flow Algorithms**
These algorithms deal with the flow of data through a network of vertices and edges.

### a. **Ford-Fulkerson Algorithm**
- **Purpose**: Find the maximum flow from a source to a sink in a flow network.
- **Time Complexity**: O(max_flow * E)
- **Space Complexity**: O(V + E)

### b. **Edmonds-Karp Algorithm**
- **Purpose**: An implementation of the Ford-Fulkerson method that uses BFS for finding augmenting paths.
- **Time Complexity**: O(V * E^2)
- **Space Complexity**: O(V + E)

## 8. **Cycle Detection Algorithms**
These algorithms help in detecting cycles in a graph.

### a. **Cycle Detection in Directed Graph (DFS)**
- **Purpose**: Detect cycles in a directed graph using DFS by keeping track of the recursion stack.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

### b. **Cycle Detection in Undirected Graph (Union-Find)**
- **Purpose**: Detect cycles in an undirected graph using Union-Find.
- **Time Complexity**: O(E log V)
- **Space Complexity**: O(V)

## 9. **Graph Coloring**
Graph coloring is the assignment of labels (colors) to vertices such that no two adjacent vertices share the same color.

### a. **Greedy Coloring Algorithm**
- **Purpose**: Assign colors to vertices using a greedy approach.
- **Time Complexity**: O(V^2)
- **Space Complexity**: O(V)

## 10. **Strongly Connected Components (SCC)**
These algorithms find strongly connected components (SCCs) in directed graphs where every vertex is reachable from every other vertex in the same component.

### a. **Kosaraju’s Algorithm**
- **Purpose**: Find SCCs by performing two DFS passes.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

### b. **Tarjan’s Algorithm**
- **Purpose**: Find SCCs using a single DFS pass.
- **Time Complexity**: O(V + E)
- **Space Complexity**: O(V)

## Conclusion
Graph algorithms are essential for solving many real-world problems, including network routing, social network analysis, and optimization problems. Understanding the properties of the graph and selecting the appropriate algorithm is key to solving these problems efficiently.

