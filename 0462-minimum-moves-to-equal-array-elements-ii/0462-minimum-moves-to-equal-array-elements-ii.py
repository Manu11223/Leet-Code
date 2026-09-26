import random

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        def quickselect(arr, k):
            # Returns the k-th smallest element (0-indexed)
            if len(arr) == 1:
                return arr[0]
            pivot = random.choice(arr)
            less = [x for x in arr if x < pivot]
            equal = [x for x in arr if x == pivot]
            greater = [x for x in arr if x > pivot]
            
            if k < len(less):
                return quickselect(less, k)
            elif k < len(less) + len(equal):
                return pivot
            else:
                return quickselect(greater, k - len(less) - len(equal))
        
        median = quickselect(nums, len(nums) // 2)
        return sum(abs(num - median) for num in nums)