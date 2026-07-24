class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1

        while low <= high:
            mid = (low + high) // 2
            row, col = divmod(mid, n)
            value = matrix[row][col]

            if value == target:
                return True
            elif value < target:
                low = mid + 1
            else:
                high = mid - 1

        return False