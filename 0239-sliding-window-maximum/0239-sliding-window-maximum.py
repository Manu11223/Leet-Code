from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()   # stores indices, values in decreasing order
        result = []

        for i, num in enumerate(nums):
            # Remove indices that have fallen out of the window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove indices whose values are dominated by the current number
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # Once we've seen at least k elements, record the max
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result