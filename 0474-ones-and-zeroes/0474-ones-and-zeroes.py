class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            z = s.count('0')
            o = len(s) - z
            for i in range(m, z - 1, -1):
                row, prev = dp[i], dp[i - z]
                for j in range(n, o - 1, -1):
                    v = prev[j - o] + 1
                    if v > row[j]:
                        row[j] = v

        return dp[m][n]