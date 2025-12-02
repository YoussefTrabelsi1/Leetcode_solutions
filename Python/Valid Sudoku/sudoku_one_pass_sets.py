# filename: sudoku_one_pass_sets.py

from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    # One pass using sets for rows, columns and boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]   # box index: (r//3)*3 + (c//3)

    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                continue

            box_idx = (r // 3) * 3 + (c // 3)

            if (v in rows[r]) or (v in cols[c]) or (v in boxes[box_idx]):
                return False

            rows[r].add(v)
            cols[c].add(v)
            boxes[box_idx].add(v)

    return True


if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"]]
    print(is_valid_sudoku(board))  # True
