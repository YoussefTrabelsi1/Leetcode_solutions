# filename: heap_time_optimized_max_happiness.py
import heapq
from typing import List

def maximumHappinessSum(happiness: List[int], k: int) -> int:
    """
    Time-optimized when k << n: take k largest with a heap.
    Time: O(n log k + k log k), Space: O(k)
    """
    topk = heapq.nlargest(k, happiness)  # unsorted
    topk.sort(reverse=True)
    ans = 0
    for i, v in enumerate(topk):
        ans += max(v - i, 0)
    return ans

if __name__ == "__main__":
    print(maximumHappinessSum([1, 2, 3], 2))      # 4
    print(maximumHappinessSum([1, 1, 1, 1], 2))   # 1
    print(maximumHappinessSum([2, 3, 4, 5], 1))   # 5
