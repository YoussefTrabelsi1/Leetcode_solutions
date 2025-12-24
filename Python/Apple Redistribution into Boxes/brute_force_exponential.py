# filename: brute_force_exponential.py
from itertools import combinations

def min_boxes_bruteforce(apple, capacity):
    """
    Brute force: try all subsets by size.
    Exponential in m (only for demonstration / very small m).
    """
    total = sum(apple)
    m = len(capacity)
    for k in range(1, m + 1):
        for idxs in combinations(range(m), k):
            if sum(capacity[i] for i in idxs) >= total:
                return k
    return m  # guaranteed feasible by statement

if __name__ == "__main__":
    print(min_boxes_bruteforce([1, 3, 2], [4, 3, 1, 5, 2]))  # 2
    print(min_boxes_bruteforce([5, 5, 5], [2, 4, 2, 7]))     # 4
