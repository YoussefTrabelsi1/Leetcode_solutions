# unique_paths_dp_2d.py

def unique_paths_dp_2d(m: int, n: int) -> int:
    """
    Classic dynamic programming with O(m*n) time and O(m*n) space.
    dp[i][j] = number of ways to reach cell (i, j).
    """
    dp = [[0] * n for _ in range(m)]

    # First row and first column can only be reached in exactly one way
    for i in range(m):
        dp[i][0] = 1
    for j in range(n):
        dp[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print(unique_paths_dp_2d(3, 6))  # 21
    print(unique_paths_dp_2d(3, 3))  # 6
