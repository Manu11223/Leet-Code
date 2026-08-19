class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        result = []
        path = []

        def backtrack(start, remaining_k, remaining_n):
            if remaining_k == 0:
                if remaining_n == 0:
                    result.append(path[:])
                return
            
            # Prune: not enough digits left to pick from [start..9]
            if 9 - start + 1 < remaining_k:
                return
            
            for num in range(start, 10):
                if num > remaining_n:
                    break  # numbers only increase, no point continuing
                
                # Prune: even the smallest possible remaining sum exceeds target
                min_possible = num + sum(range(num + 1, num + remaining_k))
                if min_possible > remaining_n:
                    break
                
                path.append(num)
                backtrack(num + 1, remaining_k - 1, remaining_n - num)
                path.pop()

        backtrack(1, k, n)
        return result