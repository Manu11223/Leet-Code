from collections import deque

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        visited = {node: Node(node.val)}
        queue = deque([node])
        
        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr].neighbors.append(visited[neighbor])
        
        return visited[node]