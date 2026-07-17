class Solution:
    def totalNQueens(self, n: int) -> int:
        full_mask = (1 << n) - 1
        count = 0

        def backtrack(row: int, cols: int, diag1: int, diag2: int) -> None:
            nonlocal count
            if row == n:
                count += 1
                return

            available = full_mask & ~(cols | diag1 | diag2)

            while available:
                bit = available & (-available)
                available ^= bit

                backtrack(
                    row + 1,
                    cols | bit,
                    (diag1 | bit) << 1,
                    (diag2 | bit) >> 1
                )

        backtrack(0, 0, 0, 0)
        return count