class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        result = []
        path = []
        n = len(candidates)

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, n):
                c = candidates[i]
                if c > remaining:
                    break  # sorted, so no point checking further

                path.append(c)
                backtrack(i, remaining - c)  # i, not i+1: reuse allowed
                path.pop()

        backtrack(0, target)
        return result