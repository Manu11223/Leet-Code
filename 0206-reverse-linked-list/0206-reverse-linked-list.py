class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            next_node = curr.next  # save before overwriting
            curr.next = prev       # reverse the pointer
            prev = curr            # advance prev
            curr = next_node       # advance curr

        return prev