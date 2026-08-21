from functools import lru_cache

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        @lru_cache(maxsize=None)
        def solve(expr: str) -> list[int]:
            # Base case: no operator, it's a pure number
            if expr.isdigit():
                return [int(expr)]

            results = []
            for i, ch in enumerate(expr):
                if ch in '+-*':
                    left_results = solve(expr[:i])
                    right_results = solve(expr[i+1:])
                    for l in left_results:
                        for r in right_results:
                            if ch == '+':
                                results.append(l + r)
                            elif ch == '-':
                                results.append(l - r)
                            else:  # ch == '*'
                                results.append(l * r)
            return results

        return solve(expression)