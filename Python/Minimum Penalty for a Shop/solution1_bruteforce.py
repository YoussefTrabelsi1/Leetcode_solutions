# file: solution1_bruteforce.py

from typing import *

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        best_j = 0
        best_penalty = float("inf")

        for j in range(n + 1):
            penalty = 0
            # open hours: [0, j-1]
            for i in range(0, j):
                if customers[i] == "N":
                    penalty += 1
            # closed hours: [j, n-1]
            for i in range(j, n):
                if customers[i] == "Y":
                    penalty += 1

            if penalty < best_penalty:
                best_penalty = penalty
                best_j = j

        return best_j


if __name__ == "__main__":
    s = Solution()
    tests = ["YYNY", "NNNNN", "YYYY"]
    for t in tests:
        print(t, "->", s.bestClosingTime(t))
