from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def pathSum(self, root, targetSum: int) -> int:
        prefix_counts = defaultdict(int)
        prefix_counts[0] = 1  # empty prefix, handles paths starting at root

        def dfs(node, current_sum):
            if not node:
                return 0

            current_sum += node.val
            # how many ancestor prefixes equal (current_sum - targetSum)?
            count = prefix_counts[current_sum - targetSum]

            prefix_counts[current_sum] += 1
            count += dfs(node.left, current_sum)
            count += dfs(node.right, current_sum)
            prefix_counts[current_sum] -= 1  # backtrack when leaving this path

            return count

        return dfs(root, 0)