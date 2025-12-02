# filename: sudoku_encoded_keys.py

from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    seen = set()

    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                continue

            row_key = f"{v} in row {r}"
            col_key = f"{v} in col {c}"
            box_key = f"{v} in box {r//3}-{c//3}"

            if row_key in seen or col_key in seen or box_key in seen:
                return False

            seen.add(row_key)
            seen.add(col_key)
            seen.add(box_key)

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
