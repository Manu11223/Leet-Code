from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        len_s, len_p = len(s), len(p)
        if len_s < len_p:
            return []

        target_count = Counter(p)
        window_count = Counter(s[:len_p])

        result = []
        if window_count == target_count:
            result.append(0)

        for i in range(len_p, len_s):
            left_char = s[i - len_p]
            right_char = s[i]

            window_count[right_char] += 1
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]

            if window_count == target_count:
                result.append(i - len_p + 1)

        return result