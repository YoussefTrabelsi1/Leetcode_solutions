# space_optimized.py
from typing import List


class Solution:
    """
    O(n^2) time, O(1) extra space.
    Key idea:
      - Flipping adjacent pair is equivalent to choosing signs subject to constraints.
      - If there's any 0, you can effectively flip any single element (use a path ending at 0),
        so you can make every value non-negative => sum(abs).
      - If no 0, parity of negatives is invariant, so:
          * even negatives -> make all positive => sum(abs)
          * odd negatives  -> one must stay negative, choose smallest |x| => sum(abs) - 2*min_abs
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
                if x < 0:
                    neg_count += 1
                ax = -x if x < 0 else x
                total_abs += ax
                if ax < min_abs:
                    min_abs = ax

        if has_zero:
            return total_abs
        if neg_count % 2 == 0:
            return total_abs
        return total_abs - 2 * min_abs
