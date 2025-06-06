from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]

        def dfs(node, t):
            r, c = node
            if min(r, c) < 0 or max(r, c) >= n or visit[r][c]:
                return 1000000
            if r == (n - 1) and c == (n - 1):
                return max(t, grid[r][c])
            visit[r][c] = True
            t = max(t, grid[r][c])
            res = min(dfs((r + 1, c), t),
                       dfs((r - 1, c), t),
                       dfs((r, c + 1), t),
                       dfs((r, c - 1), t))
            visit[r][c] = False
            return res
        
        return dfs((0, 0), 0)