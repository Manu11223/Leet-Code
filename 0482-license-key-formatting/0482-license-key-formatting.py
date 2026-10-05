class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        res, count = [], 0
        for ch in reversed(s):
            if ch == '-':
                continue
            if count == k:
                res.append('-')
                count = 0
            res.append(ch.upper())
            count += 1
        return ''.join(reversed(res))