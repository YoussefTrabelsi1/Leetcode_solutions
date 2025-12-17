# dp_3d.py
# Clear DP with full table: O(n*k) time, O(n*k) space.

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        NEG = -10**30

        # dp[day][completed][state]
        dp = [[[NEG] * 3 for _ in range(k + 1)] for _ in range(n + 1)]
        dp[0][0][0] = 0

        for day in range(n):
            p = prices[day]
            for c in range(k + 1):
                flat, longp, shortp = dp[day][c]

                # do nothing
                dp[day + 1][c][0] = max(dp[day + 1][c][0], flat)
                dp[day + 1][c][1] = max(dp[day + 1][c][1], longp)
                dp[day + 1][c][2] = max(dp[day + 1][c][2], shortp)

                # open positions from flat
                if flat > NEG // 2:
                    dp[day + 1][c][1] = max(dp[day + 1][c][1], flat - p)  # buy -> long
                    dp[day + 1][c][2] = max(dp[day + 1][c][2], flat + p)  # sell -> short

                # close positions (complete one transaction)
                if c < k:
                    if longp > NEG // 2:
                        dp[day + 1][c + 1][0] = max(dp[day + 1][c + 1][0], longp + p)
                    if shortp > NEG // 2:
                        dp[day + 1][c + 1][0] = max(dp[day + 1][c + 1][0], shortp - p)

        return max(dp[n][c][0] for c in range(k + 1))
