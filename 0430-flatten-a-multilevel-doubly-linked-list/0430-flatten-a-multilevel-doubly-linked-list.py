class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        def flatten_dfs(node):
            curr = node
            last = node

            while curr:
                next_node = curr.next

                if curr.child:
                    child_head = curr.child
                    child_tail = flatten_dfs(child_head)

                    curr.next = child_head
                    child_head.prev = curr
                    curr.child = None

                    child_tail.next = next_node
                    if next_node:
                        next_node.prev = child_tail

                    last = child_tail
                else:
                    last = curr

                curr = next_node

            return last

        flatten_dfs(head)
        return head