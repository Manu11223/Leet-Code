class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        # dp[i][j]: s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* matching empty string
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pc = p[j - 1]
                if pc == '*':
                    # zero occurrence of preceding element
                    dp[i][j] = dp[i][j - 2]
                    # one or more occurrence, if preceding pattern char matches s[i-1]
                    prev = p[j - 2]
                    if prev == '.' or prev == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
                else:
                    if pc == '.' or pc == s[i - 1]:
                        dp[i][j] = dp[i - 1][j - 1]
                # else dp[i][j] stays False

        return dp[m][n]