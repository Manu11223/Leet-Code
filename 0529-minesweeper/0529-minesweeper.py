from typing import List

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        r, c = click

        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board

        dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
        stack = [(r, c)]
        board[r][c] = 'B'  # tentatively mark as revealed so it's never pushed twice

        while stack:
            x, y = stack.pop()
            mines = 0
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    mines += 1

            if mines:
                board[x][y] = str(mines)
            else:
                # 'B' already set; expand to unrevealed neighbors
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'E':
                        board[nx][ny] = 'B'   # mark on push
                        stack.append((nx, ny))

        return board