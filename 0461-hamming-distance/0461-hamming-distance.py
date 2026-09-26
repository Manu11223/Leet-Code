class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        diff = x ^ y
        count = 0
        while diff:
            diff &= diff - 1  # clears the lowest set bit
            count += 1
        return count