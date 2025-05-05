import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]


class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]
    

