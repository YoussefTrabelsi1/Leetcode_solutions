# file: solution_time_optimized.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Still O(n*m), but minimizes Python overhead using local bindings
        n = len(strs)
        m = len(strs[0])
        deleted = 0

        s = strs  # local alias (faster)
        for col in range(m):
            prev = s[0][col]
            bad = False
            for row in range(1, n):
                cur = s[row][col]
                if prev > cur:
                    bad = True
                    break
                prev = cur
            if bad:
                deleted += 1
        return deleted
