# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> list[TreeNode]:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def build(start: int, end: int) -> list:
            if start > end:
                return [None]  # represents an empty subtree

            all_trees = []
            for i in range(start, end + 1):
                left_subtrees = build(start, i - 1)
                right_subtrees = build(i + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)

            return all_trees

        return build(1, n) if n > 0 else []