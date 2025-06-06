from typing import List


class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = [[False] * n for _ in range(n)]
        minH = maxH = grid[0][0]
        for row in range(n):
            maxH = max(maxH, max(grid[row]))
            minH = min(minH, min(grid[row]))

        def dfs(node, t):
            r, c = node
            if (min(r, c) < 0 or max(r, c) >= n or 
                visit[r][c] or grid[r][c] > t):
                return False
            if r == (n - 1) and c == (n - 1):
                return True
            visit[r][c] = True
            return (dfs((r + 1, c), t) or
                    dfs((r - 1, c), t) or
                    dfs((r, c + 1), t) or
                    dfs((r, c - 1), t))
            
        for t in range(minH, maxH):
            if dfs((0, 0), t):
                return t
            for r in range(n):
                for c in range(n):
                    visit[r][c] = False
        
        return maxH