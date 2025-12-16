# filename: solution_time_optimized.py
from typing import List, Tuple

NEG = -10**18

def max_profit(n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
    """
    Time-optimized DP:
    - Same optimal DP idea, but merges only up to current reachable max cost ("cap"),
      skipping useless budget ranges.
    - Still worst-case O(n * budget^2), but typically faster in Python.

    Constraints are small enough that this is very safe.
    """
    children = [[] for _ in range(n + 1)]
    for u, v in hierarchy:
        children[u].append(v)

    def merge(a: List[int], cap_a: int, b: List[int], cap_b: int) -> Tuple[List[int], int]:
        cap_out = min(budget, cap_a + cap_b)
        out = [NEG] * (budget + 1)
        for i in range(cap_a + 1):
            ai = a[i]
            if ai == NEG:
                continue
            max_j = min(cap_b, budget - i)
            for j in range(max_j + 1):
                bj = b[j]
                if bj == NEG:
                    continue
                val = ai + bj
                idx = i + j
                if val > out[idx]:
                    out[idx] = val
        return out, cap_out

    def dfs(u: int) -> Tuple[List[int], int, List[int], int]:
        # returns (dp0_u, cap0, dp1_u, cap1)
        child_data = [dfs(v) for v in children[u]]

        # Pre-extract for speed
        child_dp0 = [(d0, c0) for (d0, c0, _d1, _c1) in child_data]
        child_dp1 = [(_d1, _c1) for (_d0, _c0, _d1, _c1) in child_data]

        def build(parent_bought: bool) -> Tuple[List[int], int]:
            # not buy u
            not_buy = [NEG] * (budget + 1)
            not_buy[0] = 0
            cap_not = 0
            for d0, c0 in child_dp0:
                not_buy, cap_not = merge(not_buy, cap_not, d0, c0)

            # buy u
            c = (present[u - 1] // 2) if parent_bought else present[u - 1]
            p = future[u - 1] - c
            buy = [NEG] * (budget + 1)
            if c <= budget:
                buy[c] = p
                cap_buy = c
                for d1, c1 in child_dp1:
                    buy, cap_buy = merge(buy, cap_buy, d1, c1)
            else:
                cap_buy = 0  # unreachable anyway (all NEG)

            cap = max(cap_not, cap_buy)
            out = [NEG] * (budget + 1)
            for b in range(cap + 1):
                nb = not_buy[b]
                bb = buy[b]
                out[b] = nb if nb >= bb else bb
            return out, cap

        dp0, cap0 = build(False)
        dp1, cap1 = build(True)
        return dp0, cap0, dp1, cap1

    dp0_root, cap0, _, _ = dfs(1)
    return max(dp0_root[:cap0 + 1])


if __name__ == "__main__":
    print(max_profit(2, [1, 2], [4, 3], [[1, 2]], 3))   # 5
    print(max_profit(2, [3, 4], [5, 8], [[1, 2]], 4))   # 4
    print(max_profit(3, [4, 6, 8], [7, 9, 11], [[1, 2], [1, 3]], 10))  # 10
    print(max_profit(3, [5, 2, 3], [8, 5, 6], [[1, 2], [2, 3]], 7))    # 12
