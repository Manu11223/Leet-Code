class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, path = [], []

        def dfs(start: int) -> None:
            if len(path) > 1:
                res.append(path[:])
            seen = set()
            for i in range(start, n):
                x = nums[i]
                if x in seen or (path and x < path[-1]):
                    continue
                seen.add(x)
                path.append(x)
                dfs(i + 1)
                path.pop()

        dfs(0)
        return res