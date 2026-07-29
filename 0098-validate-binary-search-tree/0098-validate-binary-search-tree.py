class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        curr = root
        prev_val = float('-inf')

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            if curr.val <= prev_val:
                return False
            prev_val = curr.val
            curr = curr.right

        return True