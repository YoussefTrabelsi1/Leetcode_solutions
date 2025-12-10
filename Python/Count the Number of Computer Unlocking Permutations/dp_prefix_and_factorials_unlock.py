# filename: dp_prefix_and_factorials_unlock.py

MOD = 10 ** 9 + 7
MAX_N = 10 ** 5

# Precompute factorials up to MAX_N
FACT = [1] * (MAX_N + 1)
for i in range(1, MAX_N + 1):
    FACT[i] = FACT[i - 1] * i % MOD


def count_unlock_permutations_dp(complexity):
    """
    O(n) time, O(1) extra per call (factorials precomputed globally).
    Uses a prefix-min style reachability argument.
    """
    n = len(complexity)
    if n <= 1:
        return 1

    if n - 1 > MAX_N:
        raise ValueError("n exceeds precomputed factorial limit")

    min_reachable = complexity[0]

    # Check each i > 0 is unlockable
    for i in range(1, n):
        if complexity[i] <= min_reachable:
            return 0
        # In theory we could update:
        # min_reachable = min(min_reachable, complexity[i])
        # but complexity[i] is always > min_reachable, so it never changes.

    # All non-root computers are unlockable; 0 is first, others can be any order
    return FACT[n - 1]


if __name__ == "__main__":
    # Example:
    # complexity = [int(x) for x in input().split()]
    complexity = [1, 2, 3]
    print(count_unlock_permutations_dp(complexity))  # 2
