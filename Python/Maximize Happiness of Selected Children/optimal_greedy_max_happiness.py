# filename: optimal_greedy_max_happiness.py
from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    """
    Optimal greedy:
    Pick children in descending happiness. On the i-th pick, remaining values are effectively reduced by i.
    Contribution = max(sorted_h[i] - i, 0) for i=0..k-1.
    Time: O(n log n), Space: O(n) if using sorted(); O(1) if sorting in-place.
    """
    arr = sorted(happiness, reverse=True)
    ans = 0
    for i in range(k):
        ans += max(arr[i] - i, 0)
    return ans

if __name__ == "__main__":
    print(maximumHappinessSum([1, 2, 3], 2))      # 4
    print(maximumHappinessSum([1, 1, 1, 1], 2))   # 1
    print(maximumHappinessSum([2, 3, 4, 5], 1))   # 5
