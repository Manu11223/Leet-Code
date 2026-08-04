class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        leftmost = root
        
        while leftmost.left:  # while not at leaf level
            curr = leftmost
            while curr:
                # connect the two children of curr
                curr.left.next = curr.right
                # connect curr's right child to curr.next's left child
                if curr.next:
                    curr.right.next = curr.next.left
                curr = curr.next  # move to next node at current level
            leftmost = leftmost.left  # move down to next level
        
        return root