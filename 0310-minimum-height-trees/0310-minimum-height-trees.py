from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n == 1:
            return [0]
        if n == 2:
            return [0, 1]

        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)

        leaves = deque(i for i in range(n) if len(adj[i]) == 1)
        remaining = n

        while remaining > 2:
            leaf_count = len(leaves)
            remaining -= leaf_count
            for _ in range(leaf_count):
                leaf = leaves.popleft()
                neighbor = adj[leaf].pop()  # leaf has exactly one neighbor
                adj[neighbor].discard(leaf)
                if len(adj[neighbor]) == 1:
                    leaves.append(neighbor)

        return list(leaves)