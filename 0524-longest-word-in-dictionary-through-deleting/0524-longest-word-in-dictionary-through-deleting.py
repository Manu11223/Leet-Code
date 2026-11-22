from typing import List

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        best = ""
        for w in dictionary:
            lw, lb = len(w), len(best)
            if lw < lb or (lw == lb and w >= best):
                continue                      # can't improve on best
            it = iter(s)
            if all(c in it for c in w):       # w is a subsequence of s
                best = w
        return best