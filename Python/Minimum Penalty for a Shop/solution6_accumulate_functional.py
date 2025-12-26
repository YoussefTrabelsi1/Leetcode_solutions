# file: solution6_accumulate_functional.py

from typing import *
from itertools import accumulate

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # prefixN[j] = count of 'N' in [0:j]
        prefixN = [0] + list(accumulate(1 if c == "N" else 0 for c in customers))

        # suffixY[j] = count of 'Y' in [j:n]
        # build reversed prefix on reversed string, then reverse back
        rev_prefixY = [0] + list(accumulate(1 if c == "Y" else 0 for c in reversed(customers)))
        suffixY = list(reversed(rev_prefixY))  # length n+1, aligned to j

        best_j = 0
        best_penalty = float("inf")
        for j in range(n + 1):
            penalty = prefixN[j] + suffixY[j]
            if penalty < best_penalty:
                best_penalty = penalty
                best_j = j

        return best_j


if __name__ == "__main__":
    s = Solution()
    tests = ["YYNY", "NNNNN", "YYYY"]
    for t in tests:
        print(t, "->", s.bestClosingTime(t))
