class Codec:
    def serialize(self, root: 'TreeNode') -> str:
        if not root:
            return ""

        vals = []
        stack = [root]

        while stack:
            node = stack.pop()
            vals.append(str(node.val))
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return ','.join(vals)

    def deserialize(self, data: str) -> 'TreeNode':
        if not data:
            return None

        vals = list(map(int, data.split(',')))
        root = TreeNode(vals[0])
        stack = [root]

        for val in vals[1:]:
            node = TreeNode(val)

            if val < stack[-1].val:
                stack[-1].left = node
            else:
                parent = stack[-1]
                while stack and stack[-1].val < val:
                    parent = stack.pop()
                parent.right = node

            stack.append(node)

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans