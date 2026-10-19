class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        total = sum(machines)
        if total % n:
            return -1
        avg = total // n

        ans = run = 0
        for m in machines:
            d = m - avg
            run += d
            ans = max(ans, abs(run), d)
        return ans