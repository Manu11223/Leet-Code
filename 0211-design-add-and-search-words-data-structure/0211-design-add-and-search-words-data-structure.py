class TrieNode:
    __slots__ = ('children', 'is_end')

    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, i: int) -> bool:
            if node is None:
                return False
            if i == len(word):
                return node.is_end

            ch = word[i]
            if ch == '.':
                return any(dfs(child, i + 1) for child in node.children if child is not None)
            else:
                idx = ord(ch) - ord('a')
                return dfs(node.children[idx], i + 1)

        return dfs(self.root, 0)