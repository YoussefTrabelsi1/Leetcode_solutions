# filename: space_optimized_inplace_sort_max_happiness.py
from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    """
    Space-optimized: sort in-place and accumulate.
    Time: O(n log n), Extra Space: O(1) (ignoring Python's sort internals)
    """
    happiness.sort(reverse=True)
    ans = 0
    for i in range(k):
        ans += max(happiness[i] - i, 0)
    return ans

if __name__ == "__main__":
    print(maximumHappinessSum([1, 2, 3], 2))      # 4
    print(maximumHappinessSum([1, 1, 1, 1], 2))   # 1
    print(maximumHappinessSum([2, 3, 4, 5], 1))   # 5
