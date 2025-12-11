# filename: time_optimized_covered_buildings.py

from typing import List, Dict
from collections import defaultdict
import bisect

def count_covered_buildings_time_optimized(n: int, buildings: List[List[int]]) -> int:
    """
    Time-optimized compared to brute force: O(m log m).
    Idea:
      - Group buildings by row and by column.
      - For each row, store sorted list of columns.
      - For each column, store sorted list of rows.
      - For each building, use binary search to check if there is:
          * a smaller and larger column in its row (left & right)
          * a smaller and larger row in its column (up & down)
    """
    row_to_cols: Dict[int, List[int]] = defaultdict(list)
    col_to_rows: Dict[int, List[int]] = defaultdict(list)

    for x, y in buildings:
        row_to_cols[x].append(y)
        col_to_rows[y].append(x)

    # Sort each row's columns and each column's rows
    for x in row_to_cols:
        row_to_cols[x].sort()
    for y in col_to_rows:
        col_to_rows[y].sort()

    covered = 0

    for x, y in buildings:
        cols = row_to_cols[x]
        rows = col_to_rows[y]

        # Binary search position of y in its row
        idx_col = bisect.bisect_left(cols, y)
        # left exists if there's something before idx_col
        has_left = idx_col > 0
        # right exists if there's something after idx_col
        has_right = idx_col < len(cols) - 1

        # Binary search position of x in its column
        idx_row = bisect.bisect_left(rows, x)
        has_up = idx_row > 0
        has_down = idx_row < len(rows) - 1

        if has_left and has_right and has_up and has_down:
            covered += 1

    return covered


if __name__ == "__main__":
    # Quick manual tests
    print(count_covered_buildings_time_optimized(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))  # 1
    print(count_covered_buildings_time_optimized(3, [[1,1],[1,2],[2,1],[2,2]]))        # 0
    print(count_covered_buildings_time_optimized(5, [[1,3],[3,2],[3,3],[3,5],[5,3]]))  # 1
