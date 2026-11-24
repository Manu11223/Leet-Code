class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        best = float('inf')
        prev = None
        cur = root

        while cur:
            if cur.left is None:
                if prev is not None:
                    best = min(best, cur.val - prev)
                prev = cur.val
                cur = cur.right
            else:
                pred = cur.left
                while pred.right and pred.right is not cur:
                    pred = pred.right
                if pred.right is None:      # first visit: thread back to cur
                    pred.right = cur
                    cur = cur.left
                else:                       # second visit: left subtree done
                    pred.right = None       # restore the tree
                    if prev is not None:
                        best = min(best, cur.val - prev)
                    prev = cur.val
                    cur = cur.right

        return best