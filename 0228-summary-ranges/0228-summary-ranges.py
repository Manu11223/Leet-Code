class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if not nums:
            return []

        result = []
        start = nums[0]

        for i in range(1, len(nums) + 1):
            # End of array, or a break in the consecutive sequence
            if i == len(nums) or nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]
                if start == end:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{end}")
                if i < len(nums):
                    start = nums[i]

        return result