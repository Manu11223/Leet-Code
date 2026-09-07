class Solution:
    def deserialize(self, s: str) -> 'NestedInteger':
        # Edge case: single integer, no brackets at all
        if s[0] != '[':
            return NestedInteger(int(s))

        stack = []
        cur = None
        num_start = None

        for i, ch in enumerate(s):
            if ch == '[':
                if cur is not None:
                    stack.append(cur)
                cur = NestedInteger()
            elif ch == ']':
                if num_start is not None:
                    cur.add(NestedInteger(int(s[num_start:i])))
                    num_start = None
                if stack:
                    parent = stack.pop()
                    parent.add(cur)
                    cur = parent
            elif ch == ',':
                if num_start is not None:
                    cur.add(NestedInteger(int(s[num_start:i])))
                    num_start = None
            else:  # digit or '-'
                if num_start is None:
                    num_start = i

        return cur