class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def helper(s: str) -> int:
            if len(s) < k:
                return 0
            
            count = {}
            for char in s:
                count[char] = count.get(char, 0) + 1
            
            for char, freq in count.items():
                if freq < k:
                    # split on this char and recurse on each piece
                    return max(helper(piece) for piece in s.split(char))
            
            # every character in s appears >= k times
            return len(s)
        
        return helper(s)