def maxArea(heights):
    """
    :type height: List[int]
    :rtype: int
    """
    
    l,r=0,len(heights)-1
    max_area=0
    while l<r:
        max_area=max(max_area,(r-l)*min(heights[l],heights[r]))
        if heights[l]<heights[r]:
            l+=1
        else:
            r-=1
    return max_area

# Test cases
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49
 
height = [1,1]
print(maxArea(height))  # Output: 1
