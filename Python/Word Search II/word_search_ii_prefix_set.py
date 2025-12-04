# file: word_search_ii_prefix_set.py

from typing import List, Set


def find_words_prefix_set(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    m, n = len(board), len(board[0])

    word_set: Set[str] = set(words)
    prefix_set: Set[str] = set()

    for w in words:
        for i in range(1, len(w) + 1):
            prefix_set.add(w[:i])

    result: List[str] = []

    def dfs(r: int, c: int, cur: str) -> None:
        if cur not in prefix_set:
            return

        if cur in word_set:
            result.append(cur)
            word_set.remove(cur)  # avoid duplicates

        tmp = board[r][c]
        board[r][c] = "#"

        if r + 1 < m and board[r + 1][c] != "#":
            dfs(r + 1, c, cur + board[r + 1][c])
        if r - 1 >= 0 and board[r - 1][c] != "#":
            dfs(r - 1, c, cur + board[r - 1][c])
        if c + 1 < n and board[r][c + 1] != "#":
            dfs(r, c + 1, cur + board[r][c + 1])
        if c - 1 >= 0 and board[r][c - 1] != "#":
            dfs(r, c - 1, cur + board[r][c - 1])

        board[r][c] = tmp

    for i in range(m):
        for j in range(n):
            ch = board[i][j]
            if ch in prefix_set:
                dfs(i, j, ch)

    return result


if __name__ == "__main__":
    board = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"]
    ]
    words = ["bat", "cat", "back", "backend", "stack"]
    print(sorted(find_words_prefix_set(board, words)))
