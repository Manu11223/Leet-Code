class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Skip duplicate values for i (safe optimization, doesn't affect correctness)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if abs(s - target) < abs(closest - target):
                    closest = s

                if s == target:
                    return s  # can't get closer than an exact match
                elif s < target:
                    left += 1
                else:
                    right -= 1

        return closest