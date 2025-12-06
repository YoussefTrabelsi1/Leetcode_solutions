# file: zigzag_row_scan_bruteforce.py

def convert(s: str, numRows: int) -> str:
    """
    Conceptually simple but less efficient:
    For each row, scan the whole string and pick chars that belong to that row.
    Time: O(numRows * len(s)) in worst case.
    """
    if numRows == 1 or numRows >= len(s):
        return s

    n = len(s)
    cycle_len = 2 * numRows - 2
    result = []

    def row_of_index(i: int) -> int:
        pos = i % cycle_len
        if pos >= numRows:
            return cycle_len - pos
        return pos

    # For each row, collect all indices whose row matches
    for r in range(numRows):
        for i in range(n):
            if row_of_index(i) == r:
                result.append(s[i])

    return "".join(result)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(convert("A", 1))              # A
