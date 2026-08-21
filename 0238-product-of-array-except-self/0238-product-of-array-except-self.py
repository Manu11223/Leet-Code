class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        # Pass 1: answer[i] = product of all elements to the left of i
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Pass 2: multiply in the product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer