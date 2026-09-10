from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd = False
        
        for c in counts.values():
            length += c - (c % 2)   # add the largest even part of c
            if c % 2 == 1:
                has_odd = True
        
        return length + 1 if has_odd else length