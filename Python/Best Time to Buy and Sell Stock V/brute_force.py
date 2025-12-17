# brute_force.py
# True brute force (no memo). Only usable for small n (explodes exponentially).

from typing import List

class Solution:
    def maxProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n > 20:
            raise ValueError("Brute force is exponential; please use a DP solution for n > 20.")

        # state: 0=flat, 1=long, 2=short
        best = 0

        def dfs(day: int, completed: int, state: int, profit: int) -> None:
            nonlocal best
            if day == n:
                if state == 0:
                    best = max(best, profit)
                return

            # Option 1: do nothing today
            dfs(day + 1, completed, state, profit)

            if state == 0:
                # Open long (buy)
                dfs(day + 1, completed, 1, profit - prices[day])
                # Open short (sell)
                dfs(day + 1, completed, 2, profit + prices[day])
            elif state == 1:
                # Close long (sell) -> completes one transaction
                if completed < k:
                    dfs(day + 1, completed + 1, 0, profit + prices[day])
            else:  # state == 2
                # Close short (buy back) -> completes one transaction
                if completed < k:
                    dfs(day + 1, completed + 1, 0, profit - prices[day])

        dfs(0, 0, 0, 0)
        return best
