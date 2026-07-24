class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        low, high = 1, x // 2  # sqrt(x) <= x/2 for x >= 4
        result = 1

        while low <= high:
            mid = (low + high) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                result = mid  # mid is a valid candidate, try for a larger one
                low = mid + 1
            else:
                high = mid - 1

        return result