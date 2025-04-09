class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def dfs(i, j):
            if i == (m - 1) and j == (n - 1):
                return 1
            if i >= m or j >= n:
                return 0
            return dfs(i, j + 1) + dfs(i + 1, j)
        
        return dfs(0, 0)