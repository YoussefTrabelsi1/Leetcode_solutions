# file: max_profit_space_optimized_sliding.py
from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2

        base = 0
        A = [0] * n
        for i in range(n):
            A[i] = prices[i] * strategy[i]
            base += A[i]

        best = base  # no modification

        # Initialize window at l=0
        sumA_window = 0
        for i in range(k):
            sumA_window += A[i]

        sumP_second = 0
        for i in range(h, k):
            sumP_second += prices[i]

        best = max(best, base + (sumP_second - sumA_window))

        # Slide l from 1 to n-k
        for l in range(1, n - k + 1):
            # update sumA over [l, l+k-1]
            sumA_window += A[l + k - 1] - A[l - 1]

            # update sumP_second over [l+h, l+k-1] (length h)
            # remove old start: (l-1)+h = l+h-1
            # add new end: l+k-1
            sumP_second += prices[l + k - 1] - prices[l + h - 1]

            best = max(best, base + (sumP_second - sumA_window))

        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumProfit([4, 2, 8], [-1, 0, 1], 2))  # 10
    print(sol.maximumProfit([5, 4, 3], [1, 1, 0], 2))   # 9
