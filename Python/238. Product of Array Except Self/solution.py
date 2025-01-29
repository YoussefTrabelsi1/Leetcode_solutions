class Solution:
    def productExceptSelf(self, nums):
        post_fix,pre_fix=[1 for k in range(len(nums)+1)],[1 for k in range(len(nums)+1)]

        for i in range(len(nums)):
            pre_fix[i+1]=pre_fix[i]* nums[i]
            post_fix[len(nums)-i-1]=post_fix[len(nums)-i]* nums[len(nums)-i-1]
        
        res=[]
        for i in range(len(nums)):
            res.append(pre_fix[i]*post_fix[i+1])

        return res
        