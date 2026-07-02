class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i = 0
        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Step 1: skip leading whitespace
        while i < n and s[i] == ' ':
            i += 1

        if i == n:
            return 0

        # Step 2: sign
        sign = 1
        if s[i] == '+' or s[i] == '-':
            if s[i] == '-':
                sign = -1
            i += 1

        # Step 3: read digits
        result = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            result = result * 10 + digit

            # Early clamp to avoid unbounded growth
            if sign == 1 and result > INT_MAX:
                return INT_MAX
            if sign == -1 and -result < INT_MIN:
                return INT_MIN

            i += 1

        return sign * result