# filename: optimal_covered_buildings.py

from typing import List, Dict
from math import inf

def count_covered_buildings_optimal(n: int, buildings: List[List[int]]) -> int:
    """
    Optimal (linear) approach: O(m) time, O(m) space.
    Key observation:
      For a building (x, y) to have:
        - a building on the left in its row x:
            there must exist some y' < y in that row.
            This is equivalent to: y > min_y_in_row[x].
        - a building on the right:
            y < max_y_in_row[x].
        - a building above in its column y:
            x > min_x_in_col[y].
        - a building below:
            x < max_x_in_col[y].

      So we only need, for each row:
        min_y and max_y,
      and for each column:
        min_x and max_x.

      Then a building is covered iff:
        min_y_row[x] < y < max_y_row[x]
        AND
        min_x_col[y] < x < max_x_col[y]
    """
    row_min: Dict[int, int] = {}
    row_max: Dict[int, int] = {}
    col_min: Dict[int, int] = {}
    col_max: Dict[int, int] = {}

    # First pass: compute min and max for each row and column
    for x, y in buildings:
        if x not in row_min:
            row_min[x] = y
            row_max[x] = y
        else:
            if y < row_min[x]:
                row_min[x] = y
            if y > row_max[x]:
                row_max[x] = y

        if y not in col_min:
            col_min[y] = x
            col_max[y] = x
        else:
            if x < col_min[y]:
                col_min[y] = x
            if x > col_max[y]:
                col_max[y] = x

    # Second pass: count covered buildings
    covered = 0
    for x, y in buildings:
        if row_min[x] < y < row_max[x] and col_min[y] < x < col_max[y]:
            covered += 1

    return covered


if __name__ == "__main__":
    # Quick manual tests
    print(count_covered_buildings_optimal(3, [[1,2],[2,2],[3,2],[2,1],[2,3]]))  # 1
    print(count_covered_buildings_optimal(3, [[1,1],[1,2],[2,1],[2,2]]))        # 0
    print(count_covered_buildings_optimal(5, [[1,3],[3,2],[3,3],[3,5],[5,3]]))  # 1
