class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        p = 1  # current place value: 1, 10, 100, ...
        while p <= n:
            high = n // (p * 10)
            cur = (n // p) % 10
            low = n % p
            
            if cur == 0:
                count += high * p
            elif cur == 1:
                count += high * p + low + 1
            else:
                count += (high + 1) * p
            
            p *= 10
        return count