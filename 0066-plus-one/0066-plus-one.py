class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)

        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        # all digits were 9 and became 0 — need an extra leading digit
        return [1] + digits
        