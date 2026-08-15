class Solution:
    def rob(self, nums: list[int]) -> int:
        prev, curr = 0, 0  # prev = dp[i-2], curr = dp[i-1]
        for num in nums:
            prev, curr = curr, max(curr, prev + num)
        return curr