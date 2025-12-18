# file: max_profit_bruteforce.py
from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2

        base = 0
        for p, s in zip(prices, strategy):
            base += p * s

        best = base  # allow "no modification"

        # O(n*k) brute force over all windows
        for l in range(n - k + 1):
            sumA = 0  # sum of original contributions in the window
            sumP_second = 0  # sum of prices in the last half (which becomes all sells)
            for i in range(l, l + k):
                sumA += strategy[i] * prices[i]
                if i >= l + h:
                    sumP_second += prices[i]
            delta = sumP_second - sumA
            best = max(best, base + delta)

        return best


if __name__ == "__main__":
    # Simple sanity checks
    sol = Solution()
    print(sol.maximumProfit([4, 2, 8], [-1, 0, 1], 2))  # 10
    print(sol.maximumProfit([5, 4, 3], [1, 1, 0], 2))   # 9
