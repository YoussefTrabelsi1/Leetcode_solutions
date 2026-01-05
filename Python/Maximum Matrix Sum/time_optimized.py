# time_optimized.py
from typing import List


class Solution:
    """
    Same optimal math, written a bit tighter for speed.
    Still O(n^2) time (you must read all cells), O(1) space.
    """

    def maximumMatrixSum(self, matrix: List[List[int]]) -> int:
        total_abs = 0
        min_abs = 10**18
        neg_count = 0
        has_zero = False

        for row in matrix:
            for x in row:
                if x == 0:
                    has_zero = True
                    ax = 0
                elif x < 0:
                    neg_count += 1
                    ax = -x
                else:
                    ax = x

                total_abs += ax
                if ax < min_abs:
                    min_abs = ax

        if has_zero or (neg_count & 1) == 0:
            return total_abs
        return total_abs - (min_abs << 1)
