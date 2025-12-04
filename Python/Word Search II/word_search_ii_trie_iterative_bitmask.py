# file: word_search_ii_trie_iterative_bitmask.py

from typing import List, Dict, Optional


class TrieNode:
    __slots__ = ("children", "word")

    def __init__(self) -> None:
        self.children: Dict[str, "TrieNode"] = {}
        self.word: Optional[str] = None


def build_trie(words: List[str]) -> TrieNode:
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = w
    return root


def find_words_trie_iterative_bitmask(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    m, n = len(board), len(board[0])
    root = build_trie(words)
    result: List[str] = []

    # neighbors offsets
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    for r in range(m):
        for c in range(n):
            ch = board[r][c]
            if ch not in root.children:
                continue

            start_node = root.children[ch]
            start_pos = r * n + c
            start_mask = 1 << start_pos

            stack = [(r, c, start_node, start_mask)]

            while stack:
                cr, cc, node, mask = stack.pop()

                if node.word is not None:
                    result.append(node.word)
                    node.word = None  # avoid duplicates

                for dr, dc in dirs:
                    nr, nc = cr + dr, cc + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue
                    pos = nr * n + nc
                    if (mask >> pos) & 1:
                        continue
                    nch = board[nr][nc]
                    if nch not in node.children:
                        continue
                    next_node = node.children[nch]
                    next_mask = mask | (1 << pos)
                    stack.append((nr, nc, next_node, next_mask))

    return result


if __name__ == "__main__":
    board = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"]
    ]
    words = ["bat", "cat", "back", "backend", "stack"]
    print(sorted(find_words_trie_iterative_bitmask(board, words)))
