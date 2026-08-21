# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True

        # Step 1: find middle using slow/fast pointers
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half starting after slow
        second = self._reverse(slow.next)

        # Step 3: compare first half and reversed second half
        first = head
        result = True
        p1, p2 = first, second
        while p2:
            if p1.val != p2.val:
                result = False
                break
            p1 = p1.next
            p2 = p2.next

        # Step 4 (optional but good practice): restore the list
        slow.next = self._reverse(second)

        return result

    def _reverse(self, node: ListNode) -> ListNode:
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev