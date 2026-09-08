from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (a, b), v in zip(equations, values):
            graph[a][b] = v
            graph[b][a] = 1.0 / v
        
        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0
            visited.add(src)
            for neighbor, weight in graph[src].items():
                if neighbor not in visited:
                    result = dfs(neighbor, dst, visited)
                    if result != -1.0:
                        return weight * result
            return -1.0
        
        return [dfs(c, d, set()) for c, d in queries]