class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorials = [1] * (n + 1)
        for i in range(1, n + 1):
            factorials[i] = factorials[i - 1] * i

        digits = [str(i) for i in range(1, n + 1)]
        result = []
        k -= 1  # convert to 0-indexed

        for i in range(n, 0, -1):
            f = factorials[i - 1]
            idx = k // f
            k %= f
            result.append(digits[idx])
            digits.pop(idx)

        return ''.join(result)
        