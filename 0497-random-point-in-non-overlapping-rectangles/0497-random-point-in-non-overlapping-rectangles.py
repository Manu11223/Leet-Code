import random
from bisect import bisect_right
from itertools import accumulate

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix = list(accumulate((x - a + 1) * (y - b + 1) for a, b, x, y in rects))
        self.total = self.prefix[-1]

    def pick(self) -> List[int]:
        r = random.randrange(self.total)
        i = bisect_right(self.prefix, r)
        offset = r - (self.prefix[i - 1] if i else 0)
        a, b, x, _ = self.rects[i]
        w = x - a + 1
        return [a + offset % w, b + offset // w]