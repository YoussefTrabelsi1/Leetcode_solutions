# file: solution_space_optimized.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Uses O(1) extra space (same as others), kept explicit as "space optimized"
        n = len(strs)
        m = len(strs[0])
        deleted = 0

        for j in range(m):
            # check column j without building any extra arrays/strings
            for i in range(1, n):
                if strs[i][j] < strs[i - 1][j]:
                    deleted += 1
                    break
        return deleted
