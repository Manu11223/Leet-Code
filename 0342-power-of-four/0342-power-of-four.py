class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        # n must be a power of two: only one bit set
        if n & (n - 1) != 0:
            return False
        # that single bit must be in an even position (0-indexed)
        # 0x55555555 = 0101...0101 in binary — marks bits 0,2,4,...30
        return n & 0x55555555 != 0