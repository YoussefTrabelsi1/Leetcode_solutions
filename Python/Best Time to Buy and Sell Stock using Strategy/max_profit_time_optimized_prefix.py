# file: max_profit_time_optimized_prefix.py
from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        h = k // 2

        # base profit and prefix sums
        prefixA = [0] * (n + 1)  # A[i] = strategy[i] * prices[i]
        prefixP = [0] * (n + 1)  # prices
        base = 0

        for i, (p, s) in enumerate(zip(prices, strategy)):
            a = p * s
            base += a
            prefixA[i + 1] = prefixA[i] + a
            prefixP[i + 1] = prefixP[i] + p

        best = base  # allow no modification

        # Key identity for window starting at l:
        # delta(l) = sum(prices[l+h : l+k]) - sum(A[l : l+k])
        for l in range(0, n - k + 1):
            sumA = prefixA[l + k] - prefixA[l]
            sumP_second = prefixP[l + k] - prefixP[l + h]
            best = max(best, base + (sumP_second - sumA))

        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximumProfit([4, 2, 8], [-1, 0, 1], 2))  # 10
    print(sol.maximumProfit([5, 4, 3], [1, 1, 0], 2))   # 9
