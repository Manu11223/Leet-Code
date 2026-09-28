class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        max_len = [0] * 26
        cur = 0
        for i, ch in enumerate(s):
            if i > 0 and (ord(ch) - ord(s[i - 1])) % 26 == 1:
                cur += 1
            else:
                cur = 1
            idx = ord(ch) - ord('a')
            if cur > max_len[idx]:
                max_len[idx] = cur
        return sum(max_len)