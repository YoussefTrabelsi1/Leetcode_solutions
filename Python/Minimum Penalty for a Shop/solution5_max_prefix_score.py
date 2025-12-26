# file: solution5_max_prefix_score.py

from typing import *

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        score = 0
        best_score = 0
        best_j = 0  # j is prefix length (closing hour)

        for i, ch in enumerate(customers):
            score += 1 if ch == "Y" else -1
            # closing hour would be i+1
            if score > best_score:
                best_score = score
                best_j = i + 1

        return best_j


if __name__ == "__main__":
    s = Solution()
    tests = ["YYNY", "NNNNN", "YYYY"]
    for t in tests:
        print(t, "->", s.bestClosingTime(t))
