# filename: math_optimal_unlock.py

MOD = 10 ** 9 + 7


def count_unlock_permutations_optimal(complexity):
    """
    O(n) time, O(1) extra space.

    Rule:
      - if any complexity[i] <= complexity[0] (i > 0) → no valid order → 0
      - else → (n-1)! modulo 1e9+7
    """
    n = len(complexity)
    if n <= 1:
        return 1

    root_c = complexity[0]

    # Check necessary & sufficient condition
    for i in range(1, n):
        if complexity[i] <= root_c:
            return 0

    # Compute (n-1)! mod MOD
    fact = 1
    for k in range(1, n):
        fact = (fact * k) % MOD

    return fact


if __name__ == "__main__":
    # Example:
    # complexity = [int(x) for x in input().split()]
    complexity = [1, 2, 3]
    print(count_unlock_permutations_optimal(complexity))  # 2
