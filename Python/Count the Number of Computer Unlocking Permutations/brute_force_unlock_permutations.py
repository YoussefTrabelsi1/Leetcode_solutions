# filename: brute_force_unlock_permutations.py

from itertools import permutations

MOD = 10 ** 9 + 7


def is_valid_permutation(perm, complexity):
    """
    Check if a permutation perm of [0..n-1] is a valid unlock order.
    We enforce perm[0] == 0 (root unlocked first).
    """
    n = len(complexity)
    if perm[0] != 0:
        return False

    unlocked = {0}  # computer 0 is unlocked first

    for pos in range(1, n):
        i = perm[pos]
        ci = complexity[i]

        ok = False
        # Need some unlocked j < i with complexity[j] < complexity[i]
        for j in unlocked:
            if j < i and complexity[j] < ci:
                ok = True
                break

        if not ok:
            return False

        unlocked.add(i)

    return True


def count_unlock_permutations_bruteforce(complexity):
    """
    Brute force all permutations with 0 first.
    Complexity: O((n-1)! * n^2). Only for very small n.
    """
    n = len(complexity)
    if n <= 1:
        return 1

    total = 0
    others = list(range(1, n))

    for tail in permutations(others):
        perm = (0,) + tail
        if is_valid_permutation(perm, complexity):
            total = (total + 1) % MOD

    return total


if __name__ == "__main__":
    # Example usage:
    # complexity = [int(x) for x in input().split()]
    complexity = [1, 2, 3]
    print(count_unlock_permutations_bruteforce(complexity))  # 2
