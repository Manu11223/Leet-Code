class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9
        upper = 10**n - 1
        lower = 10**(n - 1)
        for left in range(upper, lower - 1, -1):
            s = str(left)
            p = int(s + s[::-1])
            d = upper
            while d * d >= p:
                if p % d == 0:
                    return p % 1337
                d -= 1
        return -1  # unreachable for 1 <= n <= 8