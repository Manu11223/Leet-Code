from bisect import bisect_left

class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        # pair each start with its original index, sort by start
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        start_vals = [s[0] for s in starts]

        result = [-1] * n
        for i, (start, end) in enumerate(intervals):
            pos = bisect_left(start_vals, end)
            if pos < n:
                result[i] = starts[pos][1]

        return result