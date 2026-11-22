from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        first = [-2] * (2 * n + 1)   # -2 = unseen; index offset by n
        first[n] = -1                # balance 0 before the array starts
        bal = n
        best = 0
        for i, x in enumerate(nums):
            bal += 1 if x else -1
            j = first[bal]
            if j == -2:
                first[bal] = i
            elif i - j > best:
                best = i - j
        return best