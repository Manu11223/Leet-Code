class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: 'TreeNode') -> list[str]:
        result = []
        path = []

        def dfs(node):
            if node is None:
                return

            path.append(str(node.val))

            if node.left is None and node.right is None:
                # leaf reached — record the full path
                result.append("->".join(path))
            else:
                dfs(node.left)
                dfs(node.right)

            path.pop()  # backtrack

        dfs(root)
        return result