class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node = root
        
        while node:
            if node.left:
                # Find the rightmost node of the left subtree
                # (this will become the predecessor of node.right)
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                
                # Rewire: attach original right subtree to the rightmost node
                rightmost.right = node.right
                
                # Move left subtree to right, clear left
                node.right = node.left
                node.left = None
            
            # Move to next node in the flattened list
            node = node.right