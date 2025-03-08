# Tree Algorithms

Tree algorithms are used to process and manipulate tree data structures. These trees can represent hierarchical data and are widely used in computer science and artificial intelligence. Below are some common tree algorithms and their descriptions:

## 1. **Depth-First Search (DFS)**
DFS is a traversal algorithm that explores as far as possible along each branch before backtracking.

### Steps:
- Start from the root node.
- Visit a child node and then recursively visit its children before backtracking.
- Continue this until all nodes are visited.

### Time Complexity: 
- O(n), where n is the number of nodes.

### Types:
- Pre-order DFS
- In-order DFS
- Post-order DFS

## 2. **Breadth-First Search (BFS)**
BFS is a traversal algorithm that explores all the nodes at the present depth level before moving on to the nodes at the next depth level.

### Steps:
- Start from the root node.
- Visit all sibling nodes before moving down to the next level.

### Time Complexity: 
- O(n), where n is the number of nodes.

## 3. **Binary Search Tree (BST) Algorithms**

### a. **Insertion**
Inserts a new node in a binary search tree while maintaining its properties:
- If the value is smaller than the current node, move to the left child.
- If the value is greater, move to the right child.
- Repeat until the correct position is found.

### b. **Deletion**
Remove a node from a binary search tree:
- If the node has no children, remove it directly.
- If the node has one child, replace it with its child.
- If the node has two children, replace it with its in-order successor or predecessor.

### c. **Searching**
To search for a value in a BST:
- If the value is smaller than the current node, search in the left subtree.
- If the value is larger, search in the right subtree.
- If the value matches the current node, the search is successful.

### Time Complexity: 
- O(log n) for balanced trees, O(n) for skewed trees.

## 4. **AVL Tree Algorithms**

AVL trees are self-balancing binary search trees. They ensure that the height difference (balance factor) between the left and right subtrees of any node is at most 1.

### a. **Rotation**
Rotations are used to maintain balance:
- **Left Rotation**: Used when the right subtree is heavier.
- **Right Rotation**: Used when the left subtree is heavier.
- **Left-Right Rotation**: A combination used for double imbalance.
- **Right-Left Rotation**: A combination used for double imbalance.

### Time Complexity: 
- O(log n) for all operations.

## Conclusion

Tree algorithms play a key role in efficiently handling hierarchical data and providing solutions to many computational problems. Understanding different tree structures and algorithms, such as binary search trees, AVL trees, and segment trees, allows for optimal solutions to problems involving searching, sorting, and range queries.
