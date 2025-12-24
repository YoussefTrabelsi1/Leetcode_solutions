# filename: dp_min_boxes.py
def min_boxes_dp(apple, capacity):
    """
    DP over achievable capacity sums with minimal boxes used.
    Time: O(m * S), Space: O(S), where S = sum(capacity) <= 2500.
    """
    need = sum(apple)
    S = sum(capacity)
    INF = 10**9

    dp = [INF] * (S + 1)
    dp[0] = 0

    for c in capacity:
        for s in range(S, c - 1, -1):
            dp[s] = min(dp[s], dp[s - c] + 1)

    return min(dp[s] for s in range(need, S + 1))

if __name__ == "__main__":
    print(min_boxes_dp([1, 3, 2], [4, 3, 1, 5, 2]))  # 2
    print(min_boxes_dp([5, 5, 5], [2, 4, 2, 7]))     # 4
