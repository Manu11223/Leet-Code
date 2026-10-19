from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        m = len(ring)
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        prev = {0: 0}                       # ring index -> min steps
        for c in key:
            nxt = {}
            for j in pos[c]:
                nxt[j] = 1 + min(
                    v + min(abs(j - k), m - abs(j - k)) for k, v in prev.items()
                )
            prev = nxt
        return min(prev.values())