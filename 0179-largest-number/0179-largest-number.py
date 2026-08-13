from functools import cmp_to_key
from typing import List

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str, nums))
        
        def compare(a: str, b: str) -> int:
            if a + b > b + a:
                return -1  # a should come before b
            elif a + b < b + a:
                return 1   # b should come before a
            else:
                return 0
        
        strs.sort(key=cmp_to_key(compare))
        
        result = ''.join(strs)
        
        # Handle the all-zeros edge case: ["0","0"] -> "00" should be "0"
        return '0' if result[0] == '0' else result