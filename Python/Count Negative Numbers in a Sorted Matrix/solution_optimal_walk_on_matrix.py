# filename: solution_optimal_walk_on_matrix.py

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        # Start at bottom-left
        r, c = m - 1, 0
        count = 0

        while r >= 0 and c < n:
            if grid[r][c] < 0:
                # everything to the right in this row is negative
                count += (n - c)
                r -= 1  # move up
            else:
                c += 1  # move right

        return count
