from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        lo, hi = matrix[0][0], matrix[n - 1][n - 1]

        def count_less_equal(x: int) -> int:
            # Counts elements <= x using staircase walk from bottom-left
            count = 0
            row, col = n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= x:
                    count += row + 1  # all elements above in this column qualify
                    col += 1
                else:
                    row -= 1
            return count

        while lo < hi:
            mid = lo + (hi - lo) // 2
            if count_less_equal(mid) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo