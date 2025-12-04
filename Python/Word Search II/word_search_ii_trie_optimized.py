# file: word_search_ii_trie_optimized.py

from typing import List, Dict

class TrieNode:
    __slots__ = ("children", "word")

    def __init__(self):
        self.children: Dict[str, "TrieNode"] = {}
        self.word: str | None = None  # store full word at terminal node


def build_trie(words: List[str]) -> TrieNode:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = w  # mark end of word
    return root


def find_words_trie(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    m, n = len(board), len(board[0])
    root = build_trie(words)
    result = []

    def dfs(r: int, c: int, node: TrieNode):
        ch = board[r][c]
        if ch not in node.children:
            return

        nxt = node.children[ch]

        # if this node represents a complete word, record it
        if nxt.word is not None:
            result.append(nxt.word)
            # avoid duplicates by clearing it
            nxt.word = None

        # mark as visited
        board[r][c] = "#"

        # explore neighbors
        if r + 1 < m and board[r + 1][c] != "#":
            dfs(r + 1, c, nxt)
        if r - 1 >= 0 and board[r - 1][c] != "#":
            dfs(r - 1, c, nxt)
        if c + 1 < n and board[r][c + 1] != "#":
            dfs(r, c + 1, nxt)
        if c - 1 >= 0 and board[r][c - 1] != "#":
            dfs(r, c - 1, nxt)

        # restore
        board[r][c] = ch

        # optional pruning: remove leaf nodes from trie
        if not nxt.children and nxt.word is None:
            del node.children[ch]

    for i in range(m):
        for j in range(n):
            if board[i][j] in root.children:
                dfs(i, j, root)

    return result


if __name__ == "__main__":
    board = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"]
    ]
    words = ["bat", "cat", "back", "backend", "stack"]
    print(sorted(find_words_trie(board, words)))  # ["back", "backend", "cat"]
