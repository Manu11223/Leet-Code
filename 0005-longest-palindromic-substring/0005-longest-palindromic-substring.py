class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        start, end = 0, 0  # indices of the best palindrome found so far

        def expand_from_center(left: int, right: int) -> int:
            # Expands outward while s[left] == s[right], returns length of palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1  # length (undo the last invalid expansion)

        for i in range(len(s)):
            len1 = expand_from_center(i, i)       # odd length, center at i
            len2 = expand_from_center(i, i + 1)   # even length, center between i and i+1
            max_len = max(len1, len2)

            if max_len > end - start + 1:
                # Recompute start/end from center i and max_len
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end + 1]