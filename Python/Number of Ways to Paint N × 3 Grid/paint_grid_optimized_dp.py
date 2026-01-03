# paint_grid_optimized_dp.py
# Optimal O(n) time, O(1) space using 2 pattern types (ABA: 2 colors, ABC: 3 colors).

import sys

MOD = 10**9 + 7

def num_of_ways_optimized(n: int) -> int:
    # Row patterns:
    # ABA (two colors): 3*2 = 6
    # ABC (three colors): 3*2*1 = 6
    two = 6
    three = 6

    for _ in range(2, n + 1):
        new_two = (two * 3 + three * 2) % MOD
        new_three = (two * 2 + three * 2) % MOD
        two, three = new_two, new_three

    return (two + three) % MOD

def solve() -> None:
    data = sys.stdin.read().strip().split()
    n = int(data[0]) if data else 1
    print(num_of_ways_optimized(n))

if __name__ == "__main__":
    solve()
