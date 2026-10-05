import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small, large = [], []          # small stores negated values (max-heap)
        delayed = defaultdict(int)
        ss = ls = 0                    # valid (non-deleted) sizes

        def prune(heap, is_small):
            while heap:
                v = -heap[0] if is_small else heap[0]
                if delayed[v]:
                    delayed[v] -= 1
                    heapq.heappop(heap)
                else:
                    break

        def balance():
            nonlocal ss, ls
            if ss > ls + 1:
                heapq.heappush(large, -heapq.heappop(small))
                ss -= 1; ls += 1
                prune(small, True)
            elif ss < ls:
                heapq.heappush(small, -heapq.heappop(large))
                ls -= 1; ss += 1
                prune(large, False)

        def add(x):
            nonlocal ss, ls
            if not small or x <= -small[0]:
                heapq.heappush(small, -x); ss += 1
            else:
                heapq.heappush(large, x); ls += 1
            balance()

        def remove(x):
            nonlocal ss, ls
            delayed[x] += 1
            if x <= -small[0]:
                ss -= 1
                if x == -small[0]:
                    prune(small, True)
            else:
                ls -= 1
                if x == large[0]:
                    prune(large, False)
            balance()

        def median():
            return float(-small[0]) if k & 1 else (-small[0] + large[0]) / 2

        for i in range(k):
            add(nums[i])
        res = [median()]
        for i in range(k, len(nums)):
            add(nums[i])
            remove(nums[i - k])
            res.append(median())
        return res