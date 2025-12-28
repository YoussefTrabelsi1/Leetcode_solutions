# filename: solution_bruteforce.py

from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for x in row:
                if x < 0:
                    count += 1
        return count
