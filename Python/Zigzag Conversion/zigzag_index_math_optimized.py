# file: zigzag_index_math_optimized.py

def convert(s: str, numRows: int) -> str:
    # Trivial cases
    if numRows == 1 or numRows >= len(s):
        return s

    n = len(s)
    cycle_len = 2 * numRows - 2  # One full "V" cycle length
    result_chars = []

    # We build the answer row by row using index arithmetic
    for row in range(numRows):
        # j is the starting index for this row within each cycle
        j = row
        while j < n:
            # Character in the vertical part of the zigzag
            result_chars.append(s[j])

            # Character in the diagonal part (only for middle rows)
            # index = j + (cycle_len - 2*row)
            diag_index = j + cycle_len - 2 * row
            if 0 < row < numRows - 1 and diag_index < n:
                result_chars.append(s[diag_index])

            j += cycle_len

    return "".join(result_chars)


if __name__ == "__main__":
    print(convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
    print(convert("A", 1))              # A
