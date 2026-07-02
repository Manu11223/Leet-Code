class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10
            x //= 10
            rev = rev * 10 + digit

            # Early overflow check (before it grows further)
            if rev > INT_MAX:
                return 0

        rev *= sign
        return rev if INT_MIN <= rev <= INT_MAX else 0
        