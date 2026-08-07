class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        
        isPal = [[False] * n for _ in range(n)]
        for i in range(n):
            isPal[i][i] = True
        
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or isPal[i + 1][j - 1]:
                        isPal[i][j] = True
        
        result = []
        path = []
        
        def backtrack(start):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if isPal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()
        
        backtrack(0)
        return result