class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        n = len(nums)

        def backtrack(start: int) -> None:
            if start == n:
                result.append(nums[:])
                return

            for i in range(start, n):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]  # undo swap

        backtrack(0)
        return result