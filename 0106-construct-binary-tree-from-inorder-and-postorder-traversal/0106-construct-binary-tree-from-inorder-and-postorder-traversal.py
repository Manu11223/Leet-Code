class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)

            mid = inorder_index[root_val]

            # Must build RIGHT before LEFT — post_idx is decrementing from the end
            root.right = build(mid + 1, right)
            root.left = build(left, mid - 1)

            return root

        return build(0, len(inorder) - 1)