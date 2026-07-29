# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        first = second = prev = None
        curr = root

        while curr:
            if not curr.left:
                # Visit curr
                if prev and prev.val > curr.val:
                    if not first:
                        first = prev
                    second = curr
                prev = curr
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if not predecessor.right:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    # Visit curr (thread being removed = second visit)
                    if prev and prev.val > curr.val:
                        if not first:
                            first = prev
                        second = curr
                    prev = curr
                    curr = curr.right

        first.val, second.val = second.val, first.val