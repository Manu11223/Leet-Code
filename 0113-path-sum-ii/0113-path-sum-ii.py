class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        path = []
        
        def dfs(node, remaining):
            if not node:
                return
            
            path.append(node.val)
            remaining -= node.val
            
            if not node.left and not node.right and remaining == 0:
                result.append(path[:])  # copy the path
            else:
                dfs(node.left, remaining)
                dfs(node.right, remaining)
            
            path.pop()  # backtrack
        
        dfs(root, targetSum)
        return result