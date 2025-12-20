# file: solution_bruteforce.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        deleted = 0

        for col in range(m):
            for row in range(1, n):
                if strs[row - 1][col] > strs[row][col]:
                    deleted += 1
                    break
        return deleted
