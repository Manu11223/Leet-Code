class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []  # monotonically decreasing stack of potential "3" (nums[j]) values
        third = float('-inf')  # best candidate for "2" (nums[k])
        
        for num in reversed(nums):
            if num < third:
                return True
            while stack and stack[-1] < num:
                third = stack.pop()
            stack.append(num)
        
        return False