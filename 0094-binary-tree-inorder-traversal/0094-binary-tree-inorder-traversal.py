class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        curr = root

        while curr:
            if not curr.left:
                result.append(curr.val)
                curr = curr.right
            else:
                # Find the rightmost node in the left subtree (inorder predecessor)
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right

                if not predecessor.right:
                    # First visit: create a temporary thread back to curr
                    predecessor.right = curr
                    curr = curr.left
                else:
                    # Second visit: thread already exists, remove it, node is ready
                    predecessor.right = None
                    result.append(curr.val)
                    curr = curr.right

        return result