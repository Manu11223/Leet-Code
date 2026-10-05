class Solution:
    def __init__(self):
        s = [1, 2, 2]
        i, nxt = 2, 1
        while len(s) < 100_002:
            s.extend([nxt] * s[i])
            nxt ^= 3
            i += 1
        pre = [0]
        for x in s:
            pre.append(pre[-1] + (x == 1))
        self.pre = pre

    def magicalString(self, n: int) -> int:
        return self.pre[n]