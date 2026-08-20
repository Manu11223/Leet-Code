# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        def get_height(node, go_left):
            h = 0
            while node:
                h += 1
                node = node.left if go_left else node.right
            return h

        left_height = get_height(root, True)
        right_height = get_height(root, False)

        if left_height == right_height:
            # Perfect binary tree: 2^h - 1 nodes
            return (1 << left_height) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)