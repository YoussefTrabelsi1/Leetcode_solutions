# file: zigzag_itertools_cycle.py

from itertools import cycle

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    # Build one full zigzag row-index pattern, e.g. for 4 rows:
    # [0, 1, 2, 3, 2, 1]
    down = list(range(numRows))
    up = list(range(numRows - 2, 0, -1))
    pattern = down + up

    rows = [[] for _ in range(numRows)]
    pattern_iter = cycle(pattern)

    for ch, row_idx in zip(s, pattern_iter):
        rows[row_idx].append(ch)

    return "".join("".join(row) for row in rows)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(convert("A", 1))              # A
