class Solution:
    def countArrangement(self, n: int) -> int:
        cand = [[] for _ in range(n + 1)]
        for pos in range(1, n + 1):
            for num in range(1, n + 1):
                if num % pos == 0 or pos % num == 0:
                    cand[pos].append(1 << (num - 1))

        dp = [0] * (1 << n)
        dp[0] = 1
        for mask in range(1 << n):
            ways = dp[mask]
            if not ways:
                continue                      # unreachable state
            pos = mask.bit_count() + 1        # Python 3.10+
            if pos > n:
                continue
            for bit in cand[pos]:
                if not mask & bit:
                    dp[mask | bit] += ways
        return dp[-1]