class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        # dp represents the current row being built; starts as "previous row" = all 0s
        dp = [0] * (n + 1)
        max_side = 0

        for i in range(1, m + 1):
            prev_diag = 0  # dp[i-1][j-1], the value before it gets overwritten
            for j in range(1, n + 1):
                temp = dp[j]  # this is dp[i-1][j] before we overwrite it
                if matrix[i - 1][j - 1] == '1':
                    dp[j] = min(dp[j], dp[j - 1], prev_diag) + 1
                    max_side = max(max_side, dp[j])
                else:
                    dp[j] = 0
                prev_diag = temp

        return max_side * max_side