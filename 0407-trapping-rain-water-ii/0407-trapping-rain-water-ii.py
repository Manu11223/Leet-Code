import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        m, n = len(heightMap), len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # push all boundary cells
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        water = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while heap:
            height, r, c = heapq.heappop(heap)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    water += max(0, height - heightMap[nr][nc])
                    heapq.heappush(heap, (max(height, heightMap[nr][nc]), nr, nc))
        
        return water