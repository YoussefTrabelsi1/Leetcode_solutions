# filename: space_optimized_lower_bound_scan.py

from math import ceil
from typing import List

def min_eating_speed_lowerbound_scan(piles: List[int], h: int) -> int:
    """
    Linear scan but starts from a strong lower bound:
      k >= ceil(sum(piles) / h)  (information-theoretic lower bound)
    Then increases k until feasible.
    Time: O((max(piles) - LB) * n) in worst case, but often far fewer checks.
    Space: O(1)
    """
    if not piles:
        return 0
    total = sum(piles)
    lb = max(1, (total + h - 1) // h)   # ceil(total/h)
    ub = max(piles)

    def hours_needed(k: int) -> int:
        total_h = 0
        for p in piles:
            total_h += (p + k - 1) // k
            if total_h > h:
                break
        return total_h

    for k in range(lb, ub + 1):
        if hours_needed(k) <= h:
            return k
    return ub  # Fallback

if __name__ == "__main__":
    # Self-tests
    print(min_eating_speed_lowerbound_scan([1,4,3,2], 9))    # Expected: 2
    print(min_eating_speed_lowerbound_scan([25,10,23,4], 4)) # Expected: 25
