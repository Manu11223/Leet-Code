class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            dp[i] = 1                  # dp[i][i]
            prev = 0                   # dp[i+1][j-1], empty range at j = i+1
            for j in range(i + 1, n):
                tmp = dp[j]            # dp[i+1][j], the diagonal for the next j
                if s[i] == s[j]:
                    dp[j] = prev + 2
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                prev = tmp
        return dp[n - 1]