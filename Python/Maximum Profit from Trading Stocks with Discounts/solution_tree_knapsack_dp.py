# filename: solution_tree_knapsack_dp.py
from typing import List

NEG = -10**18

def max_profit(n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    """
    Optimal DP on tree with knapsack by budget.
    dp0[u][b]: max profit in subtree u with cost b, when u's parent did NOT buy (no discount for u)
    dp1[u][b]: max profit in subtree u with cost b, when u's parent DID buy (discount for u)

    Time:  O(n * budget^2)
    Space: O(n * budget)
    """
    children = [[] for _ in range(n + 1)]
    for u, v in hierarchy:
        children[u].append(v)

    dp0 = [[NEG] * (budget + 1) for _ in range(n + 1)]
    dp1 = [[NEG] * (budget + 1) for _ in range(n + 1)]

    def merge(a: List[int], b: List[int]) -> List[int]:
        out = [NEG] * (budget + 1)
        for i in range(budget + 1):
            if a[i] == NEG:
                continue
            ai = a[i]
            for j in range(budget - i + 1):
                if b[j] == NEG:
                    continue
                val = ai + b[j]
                if val > out[i + j]:
                    out[i + j] = val
        return out

    def dfs(u: int) -> None:
        for v in children[u]:
            dfs(v)

        # Build arrays for two cases inside each parent-state:
        # - not buying u (children see parent not bought)
        # - buying u (children see parent bought)

        # When parent did NOT buy u:
        not_buy = [NEG] * (budget + 1)
        not_buy[0] = 0
        for v in children[u]:
            not_buy = merge(not_buy, dp0[v])

        buy_cost0 = present[u - 1]
        buy_profit0 = future[u - 1] - buy_cost0
        buy0 = [NEG] * (budget + 1)
        if buy_cost0 <= budget:
            buy0[buy_cost0] = buy_profit0
            for v in children[u]:
                buy0 = merge(buy0, dp1[v])

        for b in range(budget + 1):
            dp0[u][b] = max(not_buy[b], buy0[b])

        # When parent DID buy u:
        not_buy = [NEG] * (budget + 1)
        not_buy[0] = 0
        for v in children[u]:
            not_buy = merge(not_buy, dp0[v])

        buy_cost1 = present[u - 1] // 2
        buy_profit1 = future[u - 1] - buy_cost1
        buy1 = [NEG] * (budget + 1)
        if buy_cost1 <= budget:
            buy1[buy_cost1] = buy_profit1
            for v in children[u]:
                buy1 = merge(buy1, dp1[v])

        for b in range(budget + 1):
            dp1[u][b] = max(not_buy[b], buy1[b])

    dfs(1)
    return max(dp0[1])  # CEO has no parent, so treat as "parent not bought"


if __name__ == "__main__":
    print(max_profit(2, [1, 2], [4, 3], [[1, 2]], 3))   # 5
    print(max_profit(2, [3, 4], [5, 8], [[1, 2]], 4))   # 4
    print(max_profit(3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10))  # 10
    print(max_profit(3, [5, 2, 3], [8, 5, 6], [[1, 2], [2, 3]], 7))    # 12
