class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        rev = s[::-1]
        t = s + '#' + rev
        n = len(t)
        
        # KMP failure function
        fail = [0] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j > 0 and t[i] != t[j]:
                j = fail[j - 1]
            if t[i] == t[j]:
                j += 1
            fail[i] = j
        
        longest_palindromic_prefix_len = fail[n - 1]
        to_add = rev[:len(s) - longest_palindromic_prefix_len]
        
        return to_add + s