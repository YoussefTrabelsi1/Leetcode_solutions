class Solution:
    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]  

        for i in range(n - 1, -1, -1):
            for j in range(i - 1, -2, -1):
                LIS = dp[i + 1][j + 1]  # Not including nums[i]

                if j == -1 or nums[j] < nums[i]:
                    LIS = max(LIS, 1 + dp[i + 1][i + 1])  # Including nums[i]

                dp[i][j + 1] = LIS

        return dp[0][0]