# filename: solution_row_binary_search.py

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total = 0

        for row in grid:
            # find first index where row[idx] < 0
            lo, hi = 0, n
            while lo < hi:
                mid = (lo + hi) // 2
                if row[mid] < 0:
                    hi = mid
                else:
                    lo = mid + 1
            total += (n - lo)
        return total
