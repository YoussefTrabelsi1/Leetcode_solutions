from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dfs(i, j):
            if i == len(nums):
                return 0
            
            LIS = dfs(i + 1, j) # not include

            if j == -1 or nums[j] < nums[i]:
                LIS = max(LIS, 1 + dfs(i + 1, i)) # include
            
            return LIS

        return dfs(0, -1)