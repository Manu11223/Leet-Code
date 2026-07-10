class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        i = 0
        
        while i < k:
            if nums[i] == val:
                k -= 1
                nums[i] = nums[k]  # overwrite with element from the end
                # don't increment i — need to check the swapped-in value too
            else:
                i += 1
        
        return k
        