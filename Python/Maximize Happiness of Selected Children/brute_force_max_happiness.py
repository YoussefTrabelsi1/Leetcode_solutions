# filename: brute_force_max_happiness.py
from itertools import combinations
from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    """
    Brute force (for small n): try all k-subsets, best order is descending within subset.
    Time: O(C(n,k) * k log k), Space: O(k)
    """
    n = len(happiness)
    best = 0
    for idxs in combinations(range(n), k):
        chosen = sorted((happiness[i] for i in idxs), reverse=True)
        total = 0
        for t, v in enumerate(chosen):
            total += max(v - t, 0)
        best = max(best, total)
    return best

if __name__ == "__main__":
    print(maximumHappinessSum([1, 2, 3], 2))      # 4
    print(maximumHappinessSum([1, 1, 1, 1], 2))   # 1
    print(maximumHappinessSum([2, 3, 4, 5], 1))   # 5
