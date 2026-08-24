class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        
        def count_live_neighbors(r: int, c: int) -> int:
            count = 0
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n:
                        # original state is live if value is 1 (live->live) or 2 (live->dead)
                        if board[nr][nc] == 1 or board[nr][nc] == 2:
                            count += 1
            return count
        
        for i in range(m):
            for j in range(n):
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:
                    # live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = 2  # live -> dead
                    # else stays 1 (live -> live)
                else:
                    # dead cell
                    if live_neighbors == 3:
                        board[i][j] = 3  # dead -> live
                    # else stays 0 (dead -> dead)
        
        # decode final state
        for i in range(m):
            for j in range(n):
                board[i][j] %= 2