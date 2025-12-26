# file: solution2_prefix_suffix.py

from typing import *

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        # prefixN[j] = number of 'N' in customers[0:j] (open penalty if close at j)
        prefixN = [0] * (n + 1)
        for i in range(n):
            prefixN[i + 1] = prefixN[i] + (1 if customers[i] == "N" else 0)

        # suffixY[j] = number of 'Y' in customers[j:n] (closed penalty if close at j)
        suffixY = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffixY[i] = suffixY[i + 1] + (1 if customers[i] == "Y" else 0)

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
