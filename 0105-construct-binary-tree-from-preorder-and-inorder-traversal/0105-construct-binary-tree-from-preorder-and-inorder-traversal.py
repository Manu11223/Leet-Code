class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        inorder_index = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0

        def build(left: int, right: int) -> TreeNode:
            if left > right:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)

            mid = inorder_index[root_val]

            # Must build left before right, since pre_idx advances sequentially
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)