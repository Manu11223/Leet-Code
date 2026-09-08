class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # F(0)
        current = sum(i * num for i, num in enumerate(nums))
        max_val = current
        
        for k in range(1, n):
            # nums[n-k] is the element wrapping to index 0 in arr_k
            current += total_sum - n * nums[n - k]
            max_val = max(max_val, current)
        
        return max_val