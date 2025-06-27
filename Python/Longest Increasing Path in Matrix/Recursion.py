from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(r, c, prevVal):
            if (min(r, c) < 0 or r >= ROWS or 
                c >= COLS or matrix[r][c] <= prevVal
            ):
                return 0
            
            res = 1
            for d in directions:
                res = max(res, 1 + dfs(r + d[0], c + d[1], matrix[r][c]))
            return res

        LIP = 0
        for r in range(ROWS):
            for c in range(COLS):
                LIP = max(LIP, dfs(r, c, float('-inf')))
        return LIP