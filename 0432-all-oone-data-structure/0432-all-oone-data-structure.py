class Node:
    __slots__ = ('count', 'keys', 'prev', 'next')
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None


class AllOne:
    def __init__(self):
        # sentinel head/tail; list stays sorted by count ascending
        self.head = Node(0)   # count = 0 sentinel (never holds real keys)
        self.tail = Node(float('inf'))  # sentinel
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_node = {}    # key -> Node it currently lives in

    def _insert_after(self, node, new_count):
        # insert a fresh bucket with new_count right after `node`
        new_node = Node(new_count)
        new_node.prev = node
        new_node.next = node.next
        node.next.prev = new_node
        node.next = new_node
        return new_node

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_node:
            # key starts at count 1; belongs right after head
            if self.head.next.count != 1:
                self._insert_after(self.head, 1)
            self.head.next.keys.add(key)
            self.key_node[key] = self.head.next
        else:
            cur = self.key_node[key]
            nxt = cur.next
            if nxt.count != cur.count + 1:
                nxt = self._insert_after(cur, cur.count + 1)
            nxt.keys.add(key)
            self.key_node[key] = nxt

            cur.keys.remove(key)
            if not cur.keys:
                self._remove(cur)

    def dec(self, key: str) -> None:
        cur = self.key_node[key]
        if cur.count == 1:
            del self.key_node[key]
        else:
            prv = cur.prev
            if prv.count != cur.count - 1:
                prv = self._insert_after(cur.prev, cur.count - 1)
            prv.keys.add(key)
            self.key_node[key] = prv

        cur.keys.remove(key)
        if not cur.keys:
            self._remove(cur)

    def getMaxKey(self) -> str:
        if self.tail.prev is self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        if self.head.next is self.tail:
            return ""
        return next(iter(self.head.next.keys))