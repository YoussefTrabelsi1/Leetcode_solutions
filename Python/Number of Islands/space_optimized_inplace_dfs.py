# filename: space_optimized_inplace_dfs.py
from typing import List

def num_islands_inplace_iterative(grid: List[List[str]]) -> int:
    """
    Space-optimized (in-place) iterative DFS.
    We mutate the grid to avoid an external visited matrix.
    Time: O(m*n)
    Extra space: O(1) besides the explicit stack used by DFS (worst-case O(m*n)).
    """
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    def sink(sr, sc):
        stack = [(sr, sc)]
        grid[sr][sc] = "0"  # mark as visited (sunk)
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"
                    stack.append((nr, nc))

    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                islands += 1
                sink(i, j)
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
    print(num_islands_inplace_iterative(grid1))  # Expected: 1
    print(num_islands_inplace_iterative(grid2))  # Expected: 4
