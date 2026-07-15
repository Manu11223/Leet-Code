class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
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
                    break  # sorted, no point checking further

                if i > start and c == candidates[i - 1]:
                    continue  # skip duplicates at this recursion level

                path.append(c)
                backtrack(i + 1, remaining - c)  # i+1: each element used once
                path.pop()

        backtrack(0, target)
        return result