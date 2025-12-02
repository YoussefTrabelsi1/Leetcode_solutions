# filename: sudoku_bitmask_optimized.py

from typing import List

def is_valid_sudoku(board: List[List[str]]) -> bool:
    # Bitmask version: O(1) time, O(1) space with integers instead of sets
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9

    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == '.':
                continue

            digit = ord(v) - ord('1')      # '1'->0, '2'->1, ..., '9'->8
            bit = 1 << digit
            box_idx = (r // 3) * 3 + (c // 3)

            if (rows[r] & bit) or (cols[c] & bit) or (boxes[box_idx] & bit):
                return False

            rows[r] |= bit
            cols[c] |= bit
            boxes[box_idx] |= bit

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
