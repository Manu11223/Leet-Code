# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        less_dummy = ListNode(0)
        greater_dummy = ListNode(0)
        less_tail = less_dummy
        greater_tail = greater_dummy

        curr = head
        while curr:
            if curr.val < x:
                less_tail.next = curr
                less_tail = less_tail.next
            else:
                greater_tail.next = curr
                greater_tail = greater_tail.next
            curr = curr.next

        greater_tail.next = None  # terminate to avoid cycles
        less_tail.next = greater_dummy.next

        return less_dummy.next