# filename: time_optimized_binary_search.py

from typing import List

def min_eating_speed_binary_search(piles: List[int], h: int) -> int:
    """
    Optimal solution via binary search on k (parametric search).
    Predicate: f(k) = (sum over piles of ceil(p/k)) <= h is monotonic in k.
    Time: O(n * log(max(piles)))
    Space: O(1)
    """
    if not piles:
        return 0

    left = max(1, (sum(piles) + h - 1) // h)  # helpful lower bound
    right = max(piles)

    def can_finish(k: int) -> bool:
        # Early-exit if hours exceed h
        hours = 0
        for p in piles:
            hours += (p + k - 1) // k
            if hours > h:
                return False
        return True

    ans = right
    while left <= right:
        mid = (left + right) // 2
        if can_finish(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

if __name__ == "__main__":
    # Self-tests
    print(min_eating_speed_binary_search([1,4,3,2], 9))    # Expected: 2
    print(min_eating_speed_binary_search([25,10,23,4], 4)) # Expected: 25
