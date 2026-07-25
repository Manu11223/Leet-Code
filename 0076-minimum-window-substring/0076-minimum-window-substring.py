class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        required = len(need)  # number of distinct chars that must be fully satisfied
        window_count = {}
        formed = 0  # number of distinct chars currently satisfied in window

        best_len = float('inf')
        best_left = 0

        left = 0
        for right, ch in enumerate(s):
            window_count[ch] = window_count.get(ch, 0) + 1

            if ch in need and window_count[ch] == need[ch]:
                formed += 1

            # contract window from the left while it's still valid
            while formed == required:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_left = left

                left_ch = s[left]
                window_count[left_ch] -= 1
                if left_ch in need and window_count[left_ch] < need[left_ch]:
                    formed -= 1

                left += 1

        return "" if best_len == float('inf') else s[best_left:best_left + best_len]