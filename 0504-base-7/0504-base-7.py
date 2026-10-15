class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = num < 0
        n = abs(num)
        digits = []

        while n:
            digits.append(str(n % 7))
            n //= 7

        if neg:
            digits.append("-")
        return "".join(reversed(digits))