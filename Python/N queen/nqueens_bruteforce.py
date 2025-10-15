# File: nqueens_bruteforce.py
# Approach 1 — Brute Force via permutations (O(n!) checks)
# Enumerate all permutations of columns (1 queen per row/col), then filter by diagonals.

from itertools import permutations

def solveNQueens(n: int):
    def is_valid(cols):
        # cols[r] = c means queen at (r, c)
        # Check diagonals: no two queens share r-c or r+c
        seen_diag1 = set()
        seen_diag2 = set()
        for r, c in enumerate(cols):
            d1 = r - c
            d2 = r + c
            if d1 in seen_diag1 or d2 in seen_diag2:
                return False
            seen_diag1.add(d1)
            seen_diag2.add(d2)
        return True

    boards = []
    for cols in permutations(range(n)):  # O(n!) candidates
        if is_valid(cols):
            board = []
            for c in cols:
                row = ['.'] * n
                row[c] = 'Q'
                board.append(''.join(row))
            boards.append(board)
    return boards

if __name__ == "__main__":
    # Examples
    print(solveNQueens(4))
    print(solveNQueens(1))
