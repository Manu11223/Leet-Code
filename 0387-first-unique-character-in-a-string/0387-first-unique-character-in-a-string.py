class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        for i, ch in enumerate(s):
            if counts[ord(ch) - ord('a')] == 1:
                return i

        return -1