from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], 
                      nums3: list[int], nums4: list[int]) -> int:
        sum_ab = defaultdict(int)
        for a in nums1:
            for b in nums2:
                sum_ab[a + b] += 1
        
        count = 0
        for c in nums3:
            for d in nums4:
                count += sum_ab.get(-(c + d), 0)
        
        return count