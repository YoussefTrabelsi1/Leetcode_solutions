# filename: solution_space_optimized.py
from typing import List

NEG = -10**18

def max_profit(n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    """
    Space-optimized variant:
    - Does NOT store dp arrays for all nodes.
    - Each DFS returns (dp0_u, dp1_u), and child dp arrays are discarded after merging.

    Time:  O(n * budget^2)
    Space: O(budget * recursion_depth) in practice (plus temporary merges)
    """
    children = [[] for _ in range(n + 1)]
    for u, v in hierarchy:
        children[u].append(v)

    def merge(a: List[int], b: List[int]) -> List[int]:
        out = [NEG] * (budget + 1)
        for i, ai in enumerate(a):
            if ai == NEG:
                continue
            for j, bj in enumerate(b):
                if bj == NEG:
                    continue
                if i + j > budget:
                    break
                val = ai + bj
                if val > out[i + j]:
                    out[i + j] = val
        return out

    def dfs(u: int) -> tuple[List[int], List[int]]:
        child_dp = [dfs(v) for v in children[u]]  # list of (dp0_v, dp1_v)

        # Helper to build best dp for "parent_bought_flag" affecting u's own cost
        def build(parent_bought: bool) -> List[int]:
            # Option: don't buy u -> children use dp0
            not_buy = [NEG] * (budget + 1)
            not_buy[0] = 0
            for dp0_v, _dp1_v in child_dp:
                not_buy = merge(not_buy, dp0_v)

            # Option: buy u -> children use dp1
            c = (present[u - 1] // 2) if parent_bought else present[u - 1]
            p = future[u - 1] - c
            buy = [NEG] * (budget + 1)
            if c <= budget:
                buy[c] = p
                for _dp0_v, dp1_v in child_dp:
                    buy = merge(buy, dp1_v)

            return [max(not_buy[b], buy[b]) for b in range(budget + 1)]

        dp0_u = build(False)
        dp1_u = build(True)
        return dp0_u, dp1_u

    dp0_root, _ = dfs(1)
    return max(dp0_root)


if __name__ == "__main__":
    print(max_profit(2, [1, 2], [4, 3], [[1, 2]], 3))   # 5
    print(max_profit(2, [3, 4], [5, 8], [[1, 2]], 4))   # 4
    print(max_profit(3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10))  # 10
    print(max_profit(3, [5, 2, 3], [8, 5, 6], [[1, 2], [2, 3]], 7))    # 12
