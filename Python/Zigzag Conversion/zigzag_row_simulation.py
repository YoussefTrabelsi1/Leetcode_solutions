# file: zigzag_row_simulation.py

def convert(s: str, numRows: int) -> str:
    # Trivial cases
    if numRows == 1 or numRows >= len(s):
        return s

    # Each row holds characters that belong to that row
    rows = ["" for _ in range(numRows)]

    cur_row = 0
    going_down = False

    for ch in s:
        rows[cur_row] += ch

        # Reverse direction when we hit top or bottom row
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down

        cur_row += 1 if going_down else -1

    # Concatenate all rows
    return "".join(rows)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(convert("A", 1))              # A
