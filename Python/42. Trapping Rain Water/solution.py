class Solution:
    def trap(self, height):

        maxleft=[0 for i in range(len(height))]
        maxright=[0 for i in range(len(height))]
        for i in range(1,len(height)):
            maxleft[i]=max(maxleft[i-1],height[i-1])
        
        for i in range(len(height)-2,-1,-1):
            maxright[i]=max(maxright[i+1],height[i+1])
        
        water=0
        for i in range(len(height)):
            container=min(maxright[i],maxleft[i])-height[i]
            if container>0:
                water+=container
        return water

    def trap_efficient(self, height) :
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res