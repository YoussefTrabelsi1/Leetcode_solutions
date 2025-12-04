# file: word_search_ii_bruteforce.py

from typing import List

def find_words_bruteforce(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0]:
        return []

    m, n = len(board), len(board[0])

    def dfs(r: int, c: int, word: str, idx: int, visited: List[List[bool]]) -> bool:
        # word is fully matched
        if idx == len(word):
            return True

        # out of bounds or already used or mismatch
        if r < 0 or r >= m or c < 0 or c >= n:
            return False
        if visited[r][c] or board[r][c] != word[idx]:
            return False

        visited[r][c] = True

        # explore neighbors: up, down, left, right
        if (dfs(r + 1, c, word, idx + 1, visited) or
            dfs(r - 1, c, word, idx + 1, visited) or
            dfs(r, c + 1, word, idx + 1, visited) or
            dfs(r, c - 1, word, idx + 1, visited)):
            return True

        visited[r][c] = False  # backtrack
        return False

    def exists(word: str) -> bool:
        # quick pruning: if word has a letter more times than board, skip
        from collections import Counter
        word_count = Counter(word)
        board_count = Counter(ch for row in board for ch in row)
        for ch, cnt in word_count.items():
            if board_count[ch] < cnt:
                return False

        visited = [[False] * n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    # reset visited for each start if we want strict brute force
                    for i in range(m):
                        for j in range(n):
                            visited[i][j] = False
                    if dfs(r, c, word, 0, visited):
                        return True
        return False

    result = []
    for w in words:
        if exists(w):
            result.append(w)
    return result


if __name__ == "__main__":
    board = [
        ["a", "b", "c", "d"],
        ["s", "a", "a", "t"],
        ["a", "c", "k", "e"],
        ["a", "c", "d", "n"]
    ]
    words = ["bat", "cat", "back", "backend", "stack"]
    print(find_words_bruteforce(board, words))  # ["cat","back","backend"]
