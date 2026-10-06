class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def sort(lo: int, hi: int) -> int:  # sorts nums[lo:hi], returns pair count
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) >> 1
            cnt = sort(lo, mid) + sort(mid, hi)
            j = mid
            for i in range(lo, mid):
                while j < hi and nums[i] > 2 * nums[j]:
                    j += 1
                cnt += j - mid
            nums[lo:hi] = sorted(nums[lo:hi])
            return cnt

        return sort(0, len(nums))