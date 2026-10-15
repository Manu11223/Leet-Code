from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []  # indices, values non-increasing bottom to top

        for i in range(2 * n):
            cur = nums[i % n]
            while stack and nums[stack[-1]] < cur:
                res[stack.pop()] = cur
            if i < n:
                stack.append(i)

        return res