# paint_grid_bruteforce.py
# Brute force (cell-by-cell backtracking). Only practical for small n.

import sys

MOD = 10**9 + 7

def num_of_ways_bruteforce(n: int) -> int:
    grid = [[-1] * 3 for _ in range(n)]

    def dfs(r: int, c: int) -> int:
        if r == n:
            return 1

        nr, nc = (r, c + 1) if c < 2 else (r + 1, 0)
        total = 0

        for color in (0, 1, 2):
            if c > 0 and grid[r][c - 1] == color:
                continue
            if r > 0 and grid[r - 1][c] == color:
                continue
            grid[r][c] = color
            total += dfs(nr, nc)
            grid[r][c] = -1

        return total

    return dfs(0, 0) % MOD

def solve() -> None:
    data = sys.stdin.read().strip().split()
    n = int(data[0]) if data else 1
    # Warning: exponential time; n>6 can be very slow.
    print(num_of_ways_bruteforce(n))

if __name__ == "__main__":
    solve()
