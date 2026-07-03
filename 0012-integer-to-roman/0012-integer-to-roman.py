class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []
        for i in range(len(values)):
            if num == 0:
                break
            v = values[i]
            if num >= v:
                count = num // v
                result.append(symbols[i] * count)
                num -= v * count

        return ''.join(result)