def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # If only one row, return the string as is
    if numRows == 1 or numRows >= len(s):
        return s

    # Initialize an array to store characters for each row
    rows = [""] * numRows
    current_row = 0
    going_down = False

    # Traverse the string and place characters in the appropriate row
    for char in s:
        rows[current_row] += char
        # Change direction when reaching the top or bottom row
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    # Concatenate all rows to form the final result
    return "".join(rows)

# Test cases
s1 = "PAYPALISHIRING"
numRows1 = 3
print(convert(s1, numRows1))  # Expected: "PAHNAPLSIIGYIR"

s2 = "PAYPALISHIRING"
numRows2 = 4
print(convert(s2, numRows2))  # Expected: "PINALSIGYAHRPI"

s3 = "A"
numRows3 = 1
print(convert(s3, numRows3))  # Expected: "A"
