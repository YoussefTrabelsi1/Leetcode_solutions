# filename: dp_space_optimized_om2n.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        def ok(i: int, j: int) -> bool:
            # Column i can come before column j if for every row: strs[row][i] <= strs[row][j]
            for r in range(n):
                if strs[r][i] > strs[r][j]:
                    return False
            return True

        # dp[j] = length of longest valid chain ending at column j
        dp = [1] * m
        best = 1 if m > 0 else 0

        for j in range(m):
            for i in range(j):
                if ok(i, j):
                    dp[j] = max(dp[j], dp[i] + 1)
            best = max(best, dp[j])

        return m - best


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletionSize(["babca", "bbazb"]))  # 3
    print(sol.minDeletionSize(["edcba"]))           # 4
    print(sol.minDeletionSize(["ghi", "def", "abc"]))  # 0
