# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left starting from group_prev.next
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next  # fewer than k nodes remain, leave as-is
            
            group_next = kth.next  # node right after this group
            
            # Reverse the group: prev, curr pointers
            prev, curr = group_next, group_prev.next
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # group_prev.next currently points to the old head of the group,
            # which is now the tail after reversal
            temp = group_prev.next
            group_prev.next = kth  # kth is now the head of the reversed group
            group_prev = temp      # this becomes group_prev for the next group
        
        return dummy.next