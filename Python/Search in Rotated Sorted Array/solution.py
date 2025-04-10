class Solution:
    def search(self, nums, target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1