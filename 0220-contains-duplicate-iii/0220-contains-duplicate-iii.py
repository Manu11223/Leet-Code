class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if valueDiff < 0:
            return False
        
        bucket_size = valueDiff + 1
        buckets = {}  # bucket_id -> value stored in that bucket (within current window)
        
        def get_bucket_id(num):
            # Handles negative numbers correctly (floor division)
            return num // bucket_size
        
        for i, num in enumerate(nums):
            bucket_id = get_bucket_id(num)
            
            # Check same bucket
            if bucket_id in buckets:
                return True
            
            # Check neighboring buckets (values could be close despite different bucket)
            if bucket_id - 1 in buckets and abs(num - buckets[bucket_id - 1]) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(num - buckets[bucket_id + 1]) <= valueDiff:
                return True
            
            buckets[bucket_id] = num
            
            # Evict the element that just fell outside the index window
            if i >= indexDiff:
                old_bucket_id = get_bucket_id(nums[i - indexDiff])
                del buckets[old_bucket_id]
        
        return False