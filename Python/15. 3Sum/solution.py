from collections import defaultdict


class Solution:
    def threeSumPointer(self, nums):
        nums.sort()

        res=[]

        for i in range(len(nums)-1):
            l,r=i+1,len(nums)-1
            while l<r:
                if nums[l]+nums[r]+nums[i]<0:
                    l+=1
                elif nums[l]+nums[r]+nums[i]>0:
                    r-=1
                else:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
        return res
             
    def threeSumMap(self, nums):
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        res = []
        for i in range(len(nums)):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue
                target = -(nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])

            for j in range(i + 1, len(nums)):
                count[nums[j]] += 1
        return res