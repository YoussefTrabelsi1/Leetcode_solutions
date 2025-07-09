class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(n - 1, -1, -1):
            new_dp = [False] * (n + 1)
            for open in range(n):
                if s[i] == '*':
                    new_dp[open] = (dp[open + 1] or 
                                    (open > 0 and dp[open - 1]) or 
                                    dp[open])
                elif s[i] == '(':
                    new_dp[open] = dp[open + 1]
                elif open > 0:
                    new_dp[open] = dp[open - 1]
            dp = new_dp

        return dp[0]