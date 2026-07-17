class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        n = len(intervals)
        i = 0

        # Phase 1: intervals ending before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2: merge all overlapping intervals into newInterval
        start, end = newInterval[0], newInterval[1]
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # Phase 3: remaining intervals after the merged interval
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
        