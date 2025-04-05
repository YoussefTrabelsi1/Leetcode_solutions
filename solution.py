class Solution:
    def findDuplicate(self, nums) -> int:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return nums[i]
        return -1

class Solution:
    def findDuplicate(self, nums) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1

class Solution:
    def findDuplicate(self, nums) -> int:
        seen = [0] * len(nums)
        for num in nums:
            if seen[num - 1]:
                return num
            seen[num - 1] = 1
        return -1

class Solution:
    def findDuplicate(self, nums) -> int:
        for num in nums :
            idx = abs(num) - 1 
            if nums[idx] < 0 :
                return abs(num)
            nums[idx] *= -1
        return -1

class Solution:
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        low, high = 1, n - 1
        while low < high:
            mid = low + (high - low) // 2
            lessOrEqual = sum(1 for num in nums if num <= mid)

            if lessOrEqual <= mid:
                low = mid + 1
            else:
                high = mid

        return low