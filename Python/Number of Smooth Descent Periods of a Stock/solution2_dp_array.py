# file: solution2_dp_array.py
# DP with array O(n) time, O(n) space

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [0] * n
        dp[0] = 1
        ans = 1

        for i in range(1, n):
            if prices[i - 1] - prices[i] == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 1
            ans += dp[i]

        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.getDescentPeriods([3, 2, 1, 4]))  # 7
    print(s.getDescentPeriods([8, 6, 7, 7]))  # 4
    print(s.getDescentPeriods([1]))           # 1
