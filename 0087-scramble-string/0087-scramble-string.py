from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        n = len(s1)

        @lru_cache(maxsize=None)
        def dp(i1: int, i2: int, length: int) -> bool:
            # Base case: identical substrings
            if s1[i1:i1+length] == s2[i2:i2+length]:
                return True

            # Prune: different character counts can never scramble to match
            if Counter(s1[i1:i1+length]) != Counter(s2[i2:i2+length]):
                return False

            for k in range(1, length):
                # No swap: s1[i1:i1+k] <-> s2[i2:i2+k], s1[i1+k:] <-> s2[i2+k:]
                if dp(i1, i2, k) and dp(i1 + k, i2 + k, length - k):
                    return True
                # Swap: s1[i1:i1+k] <-> s2[i2+length-k:i2+length]
                if dp(i1, i2 + length - k, k) and dp(i1 + k, i2, length - k):
                    return True

            return False

        return dp(0, 0, n)