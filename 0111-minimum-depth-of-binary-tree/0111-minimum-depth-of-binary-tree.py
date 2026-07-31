from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            if not node.left and not node.right:
                return depth  # first leaf found = minimum depth, short-circuit

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))