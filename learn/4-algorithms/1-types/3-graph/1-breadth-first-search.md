# Breadth-First Search (BFS)

**Breadth-first search (BFS)** is a graph traversal algorithm that explores nodes level by level. It answers two key questions:

1. **Is there a path from node A to node B?**
2. **What is the shortest path from node A to node B?**

![BFS](/assets/bfs.png)

**How BFS Works:**
- BFS starts from a source node and explores all neighboring nodes before moving on to the next level.
- It ensures that the shortest path (in terms of the number of edges) is found, making it ideal for pathfinding tasks.

## Example Scenario: Buying Eggs from Sellers

Imagine you're going to a market and want to buy eggs from the first seller who has them. Here's the layout:

![Sellers](/assets/bfs_sellers.png)

- Seller 1 → Seller 2
- Seller 1 → Seller 3
- Seller 2 → Seller 4
- Seller 4 → Seller 5

### How BFS Helps:
- Start from **Seller 1** (first seller) and explore the neighboring sellers.
- Visit **Seller 2** and **Seller 3**.
- **Seller 4** can only be verified after visiting **Seller 2**, and **Seller 5** can only be verified after visiting **Seller 4**.

### BFS Algorithm:

```plaintext
breadth-first():
    queue = [s1, s2, s3]
    verified = []

    while queue:
        seller = queue.dequeue()

        if seller not in verified:
            if seller.hasEggs():
                return seller
            else:
                queue.enqueue(seller.neighbors)
                verified.add(seller)
```

- queue: Keeps track of the sellers to visit.
- verified: Ensures sellers are not visited more than once.
- The algorithm checks each seller, and if they have eggs, it returns that seller; otherwise, it continues exploring the neighbors.
