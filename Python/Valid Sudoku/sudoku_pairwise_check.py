# filename: sudoku_pairwise_check.py

from typing import List, Tuple

def is_valid_sudoku(board: List[List[str]]) -> bool:
    filled_cells: List[Tuple[int, int, str]] = []

    # Collect all filled cells
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v != '.':
                filled_cells.append((r, c, v))

    n = len(filled_cells)

    # Check all pairs of filled cells for conflicts
    for i in range(n):
        r1, c1, v1 = filled_cells[i]
        for j in range(i + 1, n):
            r2, c2, v2 = filled_cells[j]

            # Only conflicts if same digit
            if v1 != v2:
                continue

            # Same row, same column, or same 3x3 box
            same_row = r1 == r2
            same_col = c1 == c2
            same_box = (r1 // 3 == r2 // 3) and (c1 // 3 == c2 // 3)

            if same_row or same_col or same_box:
                return False

    return True


if __name__ == "__main__":
    board1 = [["5","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]

    board2 = [["8","3",".",".","7",".",".",".","."],
              ["6",".",".","1","9","5",".",".","."],
              [".","9","8",".",".",".",".","6","."],
              ["8",".",".",".","6",".",".",".","3"],
              ["4",".",".","8",".","3",".",".","1"],
              ["7",".",".",".","2",".",".",".","6"],
              [".","6",".",".",".",".","2","8","."],
              [".",".",".","4","1","9",".",".","5"],
              [".",".",".",".","8",".",".","7","9"]]

    print(is_valid_sudoku(board1))  # True
    print(is_valid_sudoku(board2))  # False
