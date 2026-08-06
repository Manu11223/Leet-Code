class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        # Work on a copy of the bottom row to avoid mutating input (optional but safer)
        dp = triangle[-1][:]
        
        for i in range(n - 2, -1, -1):  # from second-to-last row up to row 0
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        
        return dp[0]