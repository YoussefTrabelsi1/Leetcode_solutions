def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area formed by the two pointers
        max_area = max(max_area, min(height[left], height[right]) * (right - left))
        
        # Move the pointer with the smaller height inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Test cases
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output: 49

height = [1,1]
print(maxArea(height))  # Output: 1
