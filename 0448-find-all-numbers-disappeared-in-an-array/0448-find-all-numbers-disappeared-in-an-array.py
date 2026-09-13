class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        n = len(nums)

        for i in range(n):
            val = abs(nums[i])
            idx = val - 1
            if nums[idx] > 0:
                nums[idx] = -nums[idx]

        result = []
        for i in range(n):
            if nums[i] > 0:
                result.append(i + 1)

        return result