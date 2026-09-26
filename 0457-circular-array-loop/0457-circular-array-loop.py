class Solution:
    def circularArrayLoop(self, nums: list[int]) -> bool:
        n = len(nums)
        
        def next_index(i: int) -> int:
            return (i + nums[i]) % n
        
        for i in range(n):
            if nums[i] == 0:
                continue
            
            slow, fast = i, next_index(i)
            
            while (nums[slow] * nums[fast] > 0 and 
                   nums[fast] * nums[next_index(fast)] > 0):
                if slow == fast:
                    if slow != next_index(slow):
                        return True
                    break
                slow = next_index(slow)
                fast = next_index(next_index(fast))
            
            # Mark the entire path starting at i as visited (set to 0)
            j = i
            direction_positive = nums[i] > 0
            while nums[j] != 0 and (nums[j] > 0) == direction_positive:
                nxt = next_index(j)
                nums[j] = 0
                j = nxt
        
        return False