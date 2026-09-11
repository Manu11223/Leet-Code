from typing import List
from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        m, n = len(heights), len(heights[0])

        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def bfs(starts, visited):
            q = deque(starts)
            for r, c in starts:
                visited[r][c] = True
            while q:
                r, c = q.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < m and 0 <= nc < n
                            and not visited[nr][nc]
                            and heights[nr][nc] >= heights[r][c]):
                        visited[nr][nc] = True
                        q.append((nr, nc))

        pacific_starts = [(0, c) for c in range(n)] + [(r, 0) for r in range(m)]
        atlantic_starts = [(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)]

        bfs(pacific_starts, pacific)
        bfs(atlantic_starts, atlantic)

        result = []
        for r in range(m):
            for c in range(n):
                if pacific[r][c] and atlantic[r][c]:
                    result.append([r, c])
        return result