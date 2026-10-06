class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) & 1:
            return 0
        goal = (total + target) >> 1

        dp = [0] * (goal + 1)
        dp[0] = 1
        for x in nums:
            for s in range(goal, x - 1, -1):
                dp[s] += dp[s - x]
        return dp[goal]