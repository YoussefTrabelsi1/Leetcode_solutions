# filename: brute_force_linear.py

from math import ceil
from typing import List

def min_eating_speed_bruteforce(piles: List[int], h: int) -> int:
    """
    Brute-force: try every k from 1 to max(piles).
    Time: O(max(piles) * n) in worst case
    Space: O(1)
    """
    if not piles:
        return 0
    max_p = max(piles)

    def hours_needed(k: int) -> int:
        # early-stop accumulation to avoid unnecessary work when exceeding h
        total = 0
        for p in piles:
            total += (p + k - 1) // k
            if total > h:
                break
        return total

    for k in range(1, max_p + 1):
        if hours_needed(k) <= h:
            return k
    return max_p  # Fallback (theoretically unreachable due to the loop)

if __name__ == "__main__":
    # Self-tests
    print(min_eating_speed_bruteforce([1,4,3,2], 9))   # Expected: 2
    print(min_eating_speed_bruteforce([25,10,23,4], 4))# Expected: 25
