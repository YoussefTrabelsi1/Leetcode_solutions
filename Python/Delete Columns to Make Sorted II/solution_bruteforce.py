# filename: solution_bruteforce.py
from itertools import combinations
from typing import List

def _is_sorted_after_deletions(strs: List[str], delete_set: set[int]) -> bool:
    n = len(strs)
    m = len(strs[0])
    # Compare adjacent rows lexicographically, skipping deleted columns
    for i in range(n - 1):
        a, b = strs[i], strs[i + 1]
        for j in range(m):
            if j in delete_set:
                continue
            if a[j] < b[j]:
                break
            if a[j] > b[j]:
                return False
        # if equal all the way, it's fine (a == b)
    return True

def min_deletion_size_bruteforce(strs: List[str]) -> int:
    """
    Brute force over subsets of deleted columns by increasing size.
    WARNING: Exponential in m; practical only for small m.
    For larger m, we fall back to the optimal greedy method to stay executable.
    """
    n = len(strs)
    if n <= 1:
        return 0
    m = len(strs[0])

    # Guardrail: brute force is infeasible for m up to 100
    if m > 20:
        return min_deletion_size_greedy(strs)

    cols = list(range(m))
    for k in range(m + 1):
        for del_cols in combinations(cols, k):
            delete_set = set(del_cols)
            if _is_sorted_after_deletions(strs, delete_set):
                return k
    return m  # worst-case delete all columns

def min_deletion_size_greedy(strs: List[str]) -> int:
    # Same as the optimal greedy solution (duplicated to keep this file standalone)
    n = len(strs)
    if n <= 1:
        return 0
    m = len(strs[0])

    decided = [False] * (n - 1)  # decided[i] means strs[i] < strs[i+1] already guaranteed
    deletions = 0

    for j in range(m):
        bad = False
        for i in range(n - 1):
            if not decided[i] and strs[i][j] > strs[i + 1][j]:
                bad = True
                break
        if bad:
            deletions += 1
            continue

        for i in range(n - 1):
            if not decided[i] and strs[i][j] < strs[i + 1][j]:
                decided[i] = True

        if all(decided):
            break

    return deletions

if __name__ == "__main__":
    tests = [
        (["ca", "bb", "ac"], 1),
        (["xc", "yb", "za"], 0),
        (["zyx", "wvu", "tsr"], 3),
    ]
    for strs, want in tests:
        got = min_deletion_size_bruteforce(strs)
        print(strs, "=>", got, "(want", want, ")")
