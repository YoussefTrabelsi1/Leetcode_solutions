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