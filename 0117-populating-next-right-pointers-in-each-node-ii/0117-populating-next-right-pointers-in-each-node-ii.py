class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost:
            dummy = Node(0)  # dummy head for the next level
            tail = dummy     # tail pointer to build next level's list
            curr = leftmost
            
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            
            leftmost = dummy.next  # move to the start of next level
        
        return root