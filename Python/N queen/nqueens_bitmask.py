# File: nqueens_bitmask.py
# Approach 3 — Space & time-optimized backtracking using bitmasks.
# Uses integers to track blocked columns and diagonals; very fast for n <= 14+.
# cols, d1, d2 are bitmasks of length n (or up to 2n-1 for diagonals, but we fold by shifting).
# For each row, candidate positions are bits where none of these masks have 1s.

def solveNQueens(n: int):
    results = []
    board_cols = [-1] * n  # store chosen column per row (to reconstruct board)

    def to_board():
        board = []
        for r in range(n):
            row = ['.'] * n
            row[board_cols[r]] = 'Q'
            board.append(''.join(row))
        return board

    def backtrack(row: int, cols: int, d1: int, d2: int):
        if row == n:
            results.append(to_board())
            return
        # Bits set to 1 are free positions this row.
        # mask has 1s on columns [0..n-1]; (~(cols|d1|d2)) & mask filters allowed spots.
        mask = (1 << n) - 1
        free = ~(cols | d1 | d2) & mask
        while free:
            bit = free & -free          # lowest set bit
            free ^= bit                 # remove that bit
            c = (bit.bit_length() - 1)  # column index
            board_cols[row] = c
            # Place queen and update masks:
            # next row => shift diag masks: new d1 = (d1 | bit) << 1 (down-left), new d2 = (d2 | bit) >> 1 (down-right)
            backtrack(row + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)

    backtrack(0, 0, 0, 0)
    return results

if __name__ == "__main__":
    # Examples
    print(solveNQueens(4))
    print(solveNQueens(1))
