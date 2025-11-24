# unique_paths_bruteforce.py

def unique_paths_bruteforce(m: int, n: int) -> int:
    """
    Brute-force DFS without memoization.
    Exponential time, only for understanding / very small inputs.
    """
    def dfs(i: int, j: int) -> int:
        # If out of bounds
        if i >= m or j >= n:
            return 0
        # Reached bottom-right
        if i == m - 1 and j == n - 1:
            return 1
        # Move right or down
        return dfs(i, j + 1) + dfs(i + 1, j)

    return dfs(0, 0)


if __name__ == "__main__":
    print(unique_paths_bruteforce(3, 6))  # Very slow if m,n are large
    print(unique_paths_bruteforce(3, 3))
