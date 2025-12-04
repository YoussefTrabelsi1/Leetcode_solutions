# file: word_search_ii_bfs_per_word.py

from typing import List
from collections import Counter, deque


def word_exists_bfs(board: List[List[str]], word: str) -> bool:
    if not word:
        return False

    m, n = len(board), len(board[0])

    # quick pruning: character counts
    word_count = Counter(word)
    board_count = Counter(ch for row in board for ch in row)
    for ch, cnt in word_count.items():
        if board_count[ch] < cnt:
            return False

    # precompute neighbors
    neighbors = [[] for _ in range(m * n)]
    for r in range(m):
        for c in range(n):
            idx = r * n + c
            if r + 1 < m:
                neighbors[idx].append((r + 1, c))
            if r - 1 >= 0:
                neighbors[idx].append((r - 1, c))
            if c + 1 < n:
                neighbors[idx].append((r, c + 1))
            if c - 1 >= 0:
                neighbors[idx].append((r, c - 1))

    # BFS states: (r, c, index_in_word, visited_mask)
    for r in range(m):
        for c in range(n):
            if board[r][c] != word[0]:
                continue

            start_idx = r * n + c
            start_mask = 1 << start_idx
            q = deque([(r, c, 0, start_mask)])

            while q:
                cr, cc, i, mask = q.popleft()
                if i == len(word) - 1:
                    return True

                cur_idx = cr * n + cc
                for nr, nc in neighbors[cur_idx]:
                    pos = nr * n + nc
                    if (mask >> pos) & 1:
                        continue
                    if board[nr][nc] != word[i + 1]:
                        continue
                    q.append((nr, nc, i + 1, mask | (1 << pos)))

    return False


def find_words_bfs(board: List[List[str]], words: List[str]) -> List[str]:
    if not board or not board[0] or not words:
        return []

    result: List[str] = []
    for w in words:
        if word_exists_bfs(board, w):
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
    print(sorted(find_words_bfs(board, words)))
