# file: zigzag_modulo_pattern.py

def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    cycle_len = 2 * numRows - 2
    rows = [[] for _ in range(numRows)]

    for i, ch in enumerate(s):
        # map position in cycle to row index
        pos_in_cycle = i % cycle_len
        if pos_in_cycle >= numRows:
            row = cycle_len - pos_in_cycle
        else:
            row = pos_in_cycle
        rows[row].append(ch)

    # flatten
    return "".join("".join(row) for row in rows)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(convert("A", 1))              # A
