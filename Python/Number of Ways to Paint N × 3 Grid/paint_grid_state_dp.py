# paint_grid_state_dp.py
# DP with state compression over all valid row patterns (12 states), O(n * 12^2), O(12) space.

import sys

MOD = 10**9 + 7

def num_of_ways_state_dp(n: int) -> int:
    # Generate all row colorings of length 3 with no horizontal equals.
    states = []
    for a in range(3):
        for b in range(3):
            if b == a:
                continue
            for c in range(3):
                if c == b:
                    continue
                states.append((a, b, c))  # total 12

    m = len(states)  # 12

    # Precompute compatibility: vertical adjacency must differ in each column.
    compat = [[] for _ in range(m)]
    for i, s1 in enumerate(states):
        for j, s2 in enumerate(states):
            if s1[0] != s2[0] and s1[1] != s2[1] and s1[2] != s2[2]:
                compat[i].append(j)

    dp = [1] * m  # for row 1, each valid pattern is possible exactly once

    for _ in range(2, n + 1):
        ndp = [0] * m
        for i in range(m):
            total = 0
            for j in compat[i]:
                total += dp[j]
            ndp[i] = total % MOD
        dp = ndp

    return sum(dp) % MOD

def solve() -> None:
    data = sys.stdin.read().strip().split()
    n = int(data[0]) if data else 1
    print(num_of_ways_state_dp(n))

if __name__ == "__main__":
    solve()
