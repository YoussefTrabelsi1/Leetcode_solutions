# file: solution4_rolling_penalty_O1.py

from typing import *

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # If we close at hour 0, shop is closed for all hours: penalty = count('Y')
        penalty = customers.count("Y")
        best_penalty = penalty
        best_j = 0

        # Move closing time from j -> j+1 by "opening" hour j
        # If customers[j] == 'Y': previously counted as closed+customer => penalty - 1
        # If customers[j] == 'N': now counted as open+no customer => penalty + 1
        for j in range(n):
            if customers[j] == "Y":
                penalty -= 1
            else:
                penalty += 1

            # closing time is now j+1
            if penalty < best_penalty:
                best_penalty = penalty
                best_j = j + 1

        return best_j


if __name__ == "__main__":
    s = Solution()
    tests = ["YYNY", "NNNNN", "YYYY"]
    for t in tests:
        print(t, "->", s.bestClosingTime(t))
