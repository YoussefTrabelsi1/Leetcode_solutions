# filename: solution_bruteforce.py
from typing import List, Tuple

def max_profit(n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    """
    Brute force (exponential).
    Works only for small n (e.g. <= 25). For larger n this will be too slow.
    """
    if n > 25:
        raise ValueError("Brute force is only intended for small n (e.g., n <= 25). Use DP solutions for full constraints.")

    children = [[] for _ in range(n + 1)]
    for u, v in hierarchy:
        children[u].append(v)

    best = 0

    def dfs(u: int, parent_bought: bool, spent: int, profit: int) -> None:
        nonlocal best
        if spent > budget:
            return
        if profit > best:
            best = profit

        # Option 1: don't buy u
        for v in children[u]:
            dfs(v, False, spent, profit)

        # Option 2: buy u (may be negative profit, but can unlock discounts)
        buy_cost = (present[u - 1] // 2) if parent_bought else present[u - 1]
        if spent + buy_cost <= budget:
            buy_profit = future[u - 1] - buy_cost
            for v in children[u]:
                dfs(v, True, spent + buy_cost, profit + buy_profit)

    # Root (CEO) has no parent, so no discount from above
    dfs(1, False, 0, 0)
    return best


if __name__ == "__main__":
    print(max_profit(2, [1, 2], [4, 3], [[1, 2]], 3))  # 5
    print(max_profit(2, [3, 4], [5, 8], [[1, 2]], 4))  # 4
