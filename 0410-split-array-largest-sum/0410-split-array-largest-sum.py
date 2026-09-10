class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def subarrays_needed(max_sum: int) -> int:
            count = 1
            current = 0
            for num in nums:
                if current + num > max_sum:
                    count += 1
                    current = num
                else:
                    current += num
            return count
        
        lo, hi = max(nums), sum(nums)
        
        while lo < hi:
            mid = (lo + hi) // 2
            if subarrays_needed(mid) <= k:
                hi = mid       # feasible, try to shrink further
            else:
                lo = mid + 1   # infeasible, need larger cap
        
        return lo