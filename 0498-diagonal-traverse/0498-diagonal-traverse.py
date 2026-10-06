class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for d in range(m + n - 1):
            lo = max(0, d - n + 1)
            hi = min(d, m - 1)
            rows = range(lo, hi + 1) if d & 1 else range(hi, lo - 1, -1)
            for i in rows:
                res.append(mat[i][d - i])
        return res