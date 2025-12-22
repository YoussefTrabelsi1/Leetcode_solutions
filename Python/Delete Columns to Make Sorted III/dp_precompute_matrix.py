# filename: dp_precompute_matrix.py

from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])
        if m == 0:
            return 0

        ok = [[False] * m for _ in range(m)]
        for i in range(m):
            for j in range(i + 1, m):
                good = True
                for r in range(n):
                    if strs[r][i] > strs[r][j]:
                        good = False
                        break
                ok[i][j] = good

        dp = [1] * m
        best = 1
        for j in range(m):
            for i in range(j):
                if ok[i][j]:
                    dp[j] = max(dp[j], dp[i] + 1)
            best = max(best, dp[j])

        return m - best


if __name__ == "__main__":
    sol = Solution()
    print(sol.minDeletionSize(["babca", "bbazb"]))  # 3
    print(sol.minDeletionSize(["edcba"]))           # 4
    print(sol.minDeletionSize(["ghi", "def", "abc"]))  # 0
