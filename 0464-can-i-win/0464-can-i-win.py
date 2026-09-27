from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False
        
        @lru_cache(maxsize=None)
        def can_win(used_mask: int, remaining: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if used_mask & bit:
                    continue
                if i >= remaining:
                    return True
                if not can_win(used_mask | bit, remaining - i):
                    return True
            return False
        
        return can_win(0, desiredTotal)