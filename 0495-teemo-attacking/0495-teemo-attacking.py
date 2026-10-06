class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = duration
        for a, b in zip(timeSeries, timeSeries[1:]):
            total += min(duration, b - a)
        return total