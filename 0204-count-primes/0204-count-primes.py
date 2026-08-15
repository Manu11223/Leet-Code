class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0

        is_composite = bytearray(n)  # index 0..n-1, all start as 0 (not composite)
        is_composite[0] = is_composite[1] = 1

        for i in range(2, int(n ** 0.5) + 1):
            if not is_composite[i]:
                # start marking from i*i (smaller multiples already marked)
                for j in range(i * i, n, i):
                    is_composite[j] = 1

        return is_composite.count(0)