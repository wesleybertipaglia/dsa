# Depth-First Search (DFS)

**Depth-first search (DFS)** is another graph traversal algorithm that explores as far down a branch as possible before backtracking. It answers similar questions as BFS:

1. **Is there a path from node A to node B?**
2. **What is the path from node A to node B?**

![DFS](/assets/dfs.png)

**How DFS Works:**
- DFS starts at the root node and explores as far as possible along each branch before backtracking.
- Unlike BFS, which explores nodes level by level, DFS follows a path all the way to its end before considering other branches.

## Example Scenario: Buying Eggs from Sellers

Let's use the same market example, but this time using DFS to find the seller who has eggs:

![Sellers](/assets/dfs_sellers.png)

- Seller 1 → Seller 2
- Seller 1 → Seller 3
- Seller 2 → Seller 4
- Seller 4 → Seller 5

### How DFS Helps:
- DFS starts from **Seller 1**, explores **Seller 2**, then goes deeper to **Seller 4**, and finally reaches **Seller 5** before backtracking.
- It will check every branch before moving to the next possible seller.

### DFS Algorithm:

```plaintext
depth-first():
    stack = [s1]
    visited = []

    while stack:
        seller = stack.pop()

        if seller not in visited:
            if seller.hasEggs():
                return seller
            else:
                stack.push(seller.neighbors)
                visited.add(seller)
```

- stack: Keeps track of the sellers to visit, storing the most recent seller first (LIFO - Last In, First Out).
- visited: Ensures each seller is checked only once.
- The algorithm moves deeper into the graph before checking other paths and returns when it finds a seller with eggs.
