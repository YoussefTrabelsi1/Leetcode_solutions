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

class Solution:
    def findDuplicate(self, nums) -> int:
        n = len(nums)
        res = 0
        for b in range(32):
            x = y = 0
            mask = 1 << b
            for num in nums:
                if num & mask:
                    x += 1
            
            for num in range(1, n):
                if num & mask:
                    y += 1
            
            if x > y:
                res |= mask
        return res

class Solution:
    def findDuplicate(self, nums) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow