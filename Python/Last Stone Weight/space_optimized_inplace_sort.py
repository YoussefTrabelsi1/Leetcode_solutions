# filename: space_optimized_inplace_sort.py

from typing import List
import bisect

def last_stone_weight_inplace(stones: List[int]) -> int:
    """
    Space-optimized (O(1) extra): keep the list sorted in-place, pop two largest, re-insert the difference.
    Time: O(k * log n + k) ~ O(n^2) in worst-case due to list insertions; Space: O(1) auxiliary.
    """
    a = stones[:]  # if strict in-place is needed on input, remove this copy
    a.sort()       # ascending
    while len(a) > 1:
        y = a.pop()  # heaviest
        x = a.pop()  # second heaviest
        d = y - x
        if d:
            # Insert back while keeping sorted order
            bisect.insort(a, d)
    return a[0] if a else 0


if __name__ == "__main__":
    print(last_stone_weight_inplace([2,3,6,2,4]))  # 1
    print(last_stone_weight_inplace([1,2]))        # 1
