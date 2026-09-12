class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        kept_end = intervals[0][1]
        removed = 0

        for start, end in intervals[1:]:
            if start >= kept_end:
                # no overlap (touching at a point counts as non-overlapping)
                kept_end = end
            else:
                # overlaps the last kept interval — remove this one
                removed += 1

        return removed