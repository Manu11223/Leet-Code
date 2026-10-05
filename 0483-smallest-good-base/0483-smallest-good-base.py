class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        def geo(k: int, m: int) -> int:
            return (k**m - 1) // (k - 1)

        for m in range(num.bit_length(), 2, -1):
            lo, hi = 2, int(num ** (1.0 / (m - 1))) + 1  # generous upper bound
            while lo <= hi:
                mid = (lo + hi) // 2
                v = geo(mid, m)
                if v == num:
                    return str(mid)
                if v < num:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return str(num - 1)  # m = 2