class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        # Transform string: "aba" -> "^#a#b#a#$"
        t = '#' + '#'.join(s) + '#'
        n = len(t)
        p = [0] * n
        center = right = 0
        
        for i in range(n):
            if i < right:
                p[i] = min(right - i, p[2 * center - i])
            
            # Expand around center i
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            
            if i + p[i] > right:
                center, right = i, i + p[i]
        
        max_len, center_index = max((n, i) for i, n in enumerate(p))
        start = (center_index - max_len) // 2
        return s[start:start + max_len]