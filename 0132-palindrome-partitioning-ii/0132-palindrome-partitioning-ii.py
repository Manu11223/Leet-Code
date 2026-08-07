class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # isPal[i][j] = True if s[i:j+1] is a palindrome
        isPal = [[False] * n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or isPal[i + 1][j - 1]:
                        isPal[i][j] = True
        
        # cuts[i] = min cuts needed for s[0:i+1]
        cuts = [0] * n
        
        for i in range(n):
            if isPal[0][i]:
                cuts[i] = 0  # whole prefix s[0:i+1] is already a palindrome, no cut needed
            else:
                cuts[i] = i  # worst case: cut before every character (i cuts for i+1 chars)
                for j in range(1, i + 1):
                    if isPal[j][i]:
                        cuts[i] = min(cuts[i], cuts[j - 1] + 1)
        
        return cuts[n - 1]