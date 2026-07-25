class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        path = []
        n = len(nums)

        def backtrack(start: int) -> None:
            result.append(path[:])  # every path, including partial ones, is a valid subset

            for i in range(start, n):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result