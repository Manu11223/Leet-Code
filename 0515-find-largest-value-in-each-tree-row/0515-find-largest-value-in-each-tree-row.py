class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, d = stack.pop()
            if d == len(res):
                res.append(node.val)
            elif node.val > res[d]:
                res[d] = node.val
            if node.right:
                stack.append((node.right, d + 1))
            if node.left:
                stack.append((node.left, d + 1))
        return res