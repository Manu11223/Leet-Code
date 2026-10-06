from math import isqrt

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = isqrt(area)
        while area % w:
            w -= 1
        return [area // w, w]