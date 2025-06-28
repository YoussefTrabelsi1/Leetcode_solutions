class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [0] * (n + 1)

        dp[n] = 1
        for i in range(m - 1, -1, -1):
            prev = 1
            for j in range(n - 1, -1, -1):
                res = dp[j]
                if s[i] == t[j]:
                    res += prev

                prev = dp[j]
                dp[j] = res 
                
        return dp[0]