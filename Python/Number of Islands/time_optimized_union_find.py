# filename: time_optimized_union_find.py
# Union-Find (Disjoint Set Union) with path compression + union by rank.
# This is near-linear and performs very well in practice, especially when grids are large.
from typing import List

class DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0]*size
        self.count = 0  # number of disjoint sets currently representing land components

    def make_set(self, x):
        # When we see a land cell, we "activate" it by counting it as a set
        self.parent[x] = x
        self.rank[x] = 0
        self.count += 1

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression (halving)
            x = self.parent[x]
        return x

    def union(self, a: int, b: int):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        # union by rank
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        elif self.rank[ra] > self.rank[rb]:
            self.parent[rb] = ra
        else:
            self.parent[rb] = ra
            self.rank[ra] += 1
        self.count -= 1

def num_islands_union_find(grid: List[List[str]]) -> int:
    if not grid or not grid[0]:
        return 0
    m, n = len(grid), len(grid[0])

    index = lambda r, c: r*n + c
    dsu = DSU(m*n)

    # First pass: initialize sets for land cells
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                dsu.make_set(index(r, c))

    # Second pass: union adjacent lands (right & down to avoid double work)
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                if c+1 < n and grid[r][c+1] == "1":
                    dsu.union(index(r, c), index(r, c+1))
                if r+1 < m and grid[r+1][c] == "1":
                    dsu.union(index(r, c), index(r+1, c))

    return dsu.count

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
    print(num_islands_union_find(grid1))  # Expected: 1
    print(num_islands_union_find(grid2))  # Expected: 4
