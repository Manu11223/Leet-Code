# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy

        # Move prev to the node just before position `left`
        for _ in range(left - 1):
            prev = prev.next

        # curr will become the tail of the reversed sublist
        curr = prev.next

        # Repeatedly take the node right after curr and move it to right after prev
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp

        return dummy.next