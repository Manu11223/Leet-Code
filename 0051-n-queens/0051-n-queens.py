class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []
        col_placement = [0] * n  # col_placement[row] = column index of queen
        full_mask = (1 << n) - 1

        def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
            if row == n:
                board = []
                for r in range(n):
                    row_str = ['.'] * n
                    row_str[col_placement[r]] = 'Q'
                    board.append(''.join(row_str))
                result.append(board)
                return

            # available positions: bits not attacked by column or either diagonal
            available = full_mask & ~(cols | diag1 | diag2)

            while available:
                bit = available & (-available)
                available ^= bit
                col = bit.bit_length() - 1
                col_placement[row] = col

                backtrack(
                    row + 1,
                    cols | bit,
                    (diag1 | bit) << 1,
                    (diag2 | bit) >> 1
                )

        backtrack(0, 0, 0, 0)
        return result
        