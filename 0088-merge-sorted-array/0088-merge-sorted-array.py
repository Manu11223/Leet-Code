class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        p1, p2 = m - 1, n - 1  # last real elements in each array
        write = m + n - 1      # last slot to fill

        while p2 >= 0:  # once nums2 is exhausted, nums1's remaining prefix is already in place
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1