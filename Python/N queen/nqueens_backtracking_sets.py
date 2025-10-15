# File: nqueens_backtracking_sets.py
# Approach 2 — Time-optimized backtracking with pruning using hash sets.
# Complexity is the usual backtracking for N-Queens; pruning reduces the search space dramatically.

def solveNQueens(n: int):
    results = []
    board = [['.'] * n for _ in range(n)]
    cols = set()      # used columns
    diag1 = set()     # r - c (top-left to bottom-right)
    diag2 = set()     # r + c (top-right to bottom-left)

    def backtrack(r: int):
        if r == n:
            results.append([''.join(row) for row in board])
            return
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
            # place
            board[r][c] = 'Q'
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            # recurse
            backtrack(r + 1)
            # remove
            board[r][c] = '.'
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return results

if __name__ == "__main__":
    # Examples
    print(solveNQueens(4))
    print(solveNQueens(1))
