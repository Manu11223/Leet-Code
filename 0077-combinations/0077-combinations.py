class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start: int) -> None:
            remaining_needed = k - len(path)

            if remaining_needed == 0:
                result.append(path[:])
                return

            # prune: if remaining numbers [start..n] can't fill remaining_needed slots, stop
            # last valid starting point is n - remaining_needed + 1
            for i in range(start, n - remaining_needed + 2):
                path.append(i)
                backtrack(i + 1)
                path.pop()

        backtrack(1)
        return result