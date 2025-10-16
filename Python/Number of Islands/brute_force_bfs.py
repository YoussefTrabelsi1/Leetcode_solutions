# filename: brute_force_bfs.py
from collections import deque
from copy import deepcopy

def num_islands_bfs(grid):
    """
    Brute-force baseline using BFS + visited set (does not mutate input).
    Time: O(m*n), Space: O(m*n) for visited + queue in worst case.
    """
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]

    def bfs(sr, sc):
        q = deque([(sr, sc)])
        visited[sr][sc] = True
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == "1":
                    visited[nr][nc] = True
                    q.append((nr, nc))

    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1" and not visited[i][j]:
                islands += 1
                bfs(i, j)
    return islands

if __name__ == "__main__":
    grid1 = [
        ["0","1","1","1","0"],
        ["0","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    grid2 = [
        ["1","1","0","0","1"],
        ["1","1","0","0","1"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    # deepcopy to emphasize function does not mutate input
    print(num_islands_bfs(deepcopy(grid1)))  # Expected: 1
    print(num_islands_bfs(deepcopy(grid2)))  # Expected: 4
