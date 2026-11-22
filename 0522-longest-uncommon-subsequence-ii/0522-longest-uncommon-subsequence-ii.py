from typing import List

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)

        def is_subseq(a: str, b: str) -> bool:
            it = iter(b)
            return all(c in it for c in a)  # `in` consumes the iterator

        for i, s in enumerate(strs):
            for j, t in enumerate(strs):
                if len(t) < len(s):
                    return len(s)          # no longer string contains s
                if i != j and is_subseq(s, t):
                    break                  # s is common, try next candidate
            else:
                return len(s)
        return -1