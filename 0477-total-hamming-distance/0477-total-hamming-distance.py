class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for b in range(30):
            c = 0
            for x in nums:
                c += (x >> b) & 1
            ans += c * (n - c)
        return ans