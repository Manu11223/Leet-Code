class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if stones[1] != 1:
            return False
        
        stone_set = set(stones)
        n = len(stones)
        target = stones[-1]
        
        # dp[stone] = set of jump sizes that can land here
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        
        for stone in stones:
            for k in dp[stone]:
                for jump in (k - 1, k, k + 1):
                    if jump > 0 and (stone + jump) in dp:
                        dp[stone + jump].add(jump)
        
        return len(dp[target]) > 0