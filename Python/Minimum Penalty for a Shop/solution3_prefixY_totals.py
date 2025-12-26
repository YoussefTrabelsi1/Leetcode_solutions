# file: solution3_prefixY_totals.py

from typing import *

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # prefixY[j] = count of 'Y' in customers[0:j]
        prefixY = [0] * (n + 1)
        totalY = 0
        for i, ch in enumerate(customers):
            totalY += (ch == "Y")
            prefixY[i + 1] = totalY

        # penalty(j) = open_N(0..j-1) + closed_Y(j..n-1)
        # open_N = j - prefixY[j]
        # closed_Y = totalY - prefixY[j]
        best_j = 0
        best_penalty = float("inf")
        for j in range(n + 1):
            open_N = j - prefixY[j]
            closed_Y = totalY - prefixY[j]
            penalty = open_N + closed_Y
            if penalty < best_penalty:
                best_penalty = penalty
                best_j = j

        return best_j


if __name__ == "__main__":
    s = Solution()
    tests = ["YYNY", "NNNNN", "YYYY"]
    for t in tests:
        print(t, "->", s.bestClosingTime(t))
