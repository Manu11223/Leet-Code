class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        
        def dfs(node, current):
            nonlocal total
            if not node:
                return
            
            current = current * 10 + node.val
            
            if not node.left and not node.right:  # leaf
                total += current
                return
            
            dfs(node.left, current)
            dfs(node.right, current)
        
        dfs(root, 0)
        return total