from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i, flag):
            if i >= len(nums) or (flag and i == len(nums) - 1):
                return 0
            
            return max(dfs(i + 1, flag), 
                       nums[i] + dfs(i + 2, flag or i == 0))
        return max(dfs(0, True), dfs(1, False))