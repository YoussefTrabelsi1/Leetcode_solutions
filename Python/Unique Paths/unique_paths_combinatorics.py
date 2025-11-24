# unique_paths_combinatorics.py

def unique_paths_combinatorics(m: int, n: int) -> int:
    """
    Time-optimized solution using combinatorics.
    Total moves = (m-1) downs + (n-1) rights = m+n-2 moves.
    We choose where the downs (or rights) go:
    C(m+n-2, m-1) or C(m+n-2, n-1).
    Computed iteratively to avoid overflow and keep O(1) space.
    """
    from math import comb

    # Using Python's built-in comb is clean and efficient
    return comb(m + n - 2, m - 1)


def unique_paths_combinatorics_manual(m: int, n: int) -> int:
    """
    Same as above but without using math.comb, computed manually.
    Uses multiplicative formula: C(N, k) = product_{i=1..k} (N - k + i) / i
    """
    N = m + n - 2
    k = min(m - 1, n - 1)  # symmetry: choose smaller for fewer iterations

    result = 1
    for i in range(1, k + 1):
        result = result * (N - k + i) // i
    return result


if __name__ == "__main__":
    print(unique_paths_combinatorics(3, 6))          # 21
    print(unique_paths_combinatorics(3, 3))          # 6
    print(unique_paths_combinatorics_manual(3, 6))   # 21
    print(unique_paths_combinatorics_manual(3, 3))   # 6
