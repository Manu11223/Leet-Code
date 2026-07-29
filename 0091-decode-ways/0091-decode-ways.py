class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        n = len(s)
        # prev2 = dp[i-2], prev1 = dp[i-1]
        prev2, prev1 = 1, 1  # dp[0]=1 (empty string), dp[1]=1 (first char valid, non-zero)

        for i in range(2, n + 1):
            curr = 0

            one_digit = int(s[i - 1])
            two_digit = int(s[i - 2:i])

            if one_digit != 0:
                curr += prev1
            if 10 <= two_digit <= 26:
                curr += prev2

            if curr == 0:  # early exit: no valid decoding possible from here on
                return 0

            prev2, prev1 = prev1, curr

        return prev1