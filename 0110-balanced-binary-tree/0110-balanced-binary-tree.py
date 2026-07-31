# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def check(node: TreeNode) -> int:
            if not node:
                return 0

            left_height = check(node.left)
            if left_height == -1:
                return -1  # imbalance already found below — propagate failure

            right_height = check(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) > 1:
                return -1  # this node itself is imbalanced

            return 1 + max(left_height, right_height)

        return check(root) != -1