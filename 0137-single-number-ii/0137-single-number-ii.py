class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            bit_sum = 0
            for num in nums:
                bit_sum += (num >> i) & 1
            bit_sum %= 3
            result |= (bit_sum << i)
        
        # handle negative numbers (Python has no fixed-width ints, so convert from 32-bit two's complement)
        if result >= 2**31:
            result -= 2**32
        
        return result