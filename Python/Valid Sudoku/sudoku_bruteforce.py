# filename: sudoku_bruteforce.py

from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    # Check all rows
    for r in range(9):
        seen = set()
        for c in range(9):
            v = board[r][c]
            if v == '.':
                continue
            if v in seen:
                return False
            seen.add(v)

    # Check all columns
    for c in range(9):
        seen = set()
        for r in range(9):
            v = board[r][c]
            if v == '.':
                continue
            if v in seen:
                return False
            seen.add(v)

    # Check all 3x3 sub-boxes
    for br in range(0, 9, 3):       # box row start
        for bc in range(0, 9, 3):   # box col start
            seen = set()
            for r in range(br, br + 3):
                for c in range(bc, bc + 3):
                    v = board[r][c]
                    if v == '.':
                        continue
                    if v in seen:
                        return False
                    seen.add(v)

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
