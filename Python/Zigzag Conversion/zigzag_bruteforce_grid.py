# file: zigzag_bruteforce_grid.py

def convert(s: str, numRows: int) -> str:
    # Trivial cases
    if numRows == 1 or numRows >= len(s):
        return s

    n = len(s)
    cycle_len = 2 * numRows - 2  # length of one full zigzag cycle
    # Each cycle adds (numRows - 1) columns at most
    cycles = (n + cycle_len - 1) // cycle_len
    max_cols = cycles * (numRows - 1)

    # 2D grid filled with empty strings
    grid = [["" for _ in range(max_cols)] for _ in range(numRows)]

    row, col = 0, 0
    going_down = True

    for ch in s:
        grid[row][col] = ch

        if going_down:
            if row == numRows - 1:
                # Turn and go up diagonally
                going_down = False
                row -= 1
                col += 1
            else:
                row += 1
        else:
            if row == 0:
                # Turn and go straight down
                going_down = True
                row += 1
            else:
                row -= 1
                col += 1

    # Read row by row, skipping empty cells
    result_chars = []
    for r in range(numRows):
        for c in range(max_cols):
            if grid[r][c]:
                result_chars.append(grid[r][c])

    return "".join(result_chars)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(convert("A", 1))              # A
