class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # min is strictly to the right of mid
                left = mid + 1
            elif nums[mid] < nums[right]:
                # min is at mid or to the left
                right = mid
            else:
                # nums[mid] == nums[right]: can't determine side, shrink safely
                right -= 1

        return nums[left]