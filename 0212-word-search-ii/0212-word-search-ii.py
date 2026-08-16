from typing import List

class TrieNode:
    __slots__ = ('children', 'word')

    def __init__(self):
        self.children = {}
        self.word = None  # stores the complete word at terminal nodes


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w

        rows, cols = len(board), len(board[0])
        result = []

        def dfs(r: int, c: int, node: TrieNode):
            ch = board[r][c]
            child = node.children.get(ch)
            if child is None:
                return

            if child.word is not None:
                result.append(child.word)
                child.word = None  # avoid duplicate results

            board[r][c] = '#'  # mark visited
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, child)
            board[r][c] = ch  # backtrack

            if not child.children:
                node.children.pop(ch, None)

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return result