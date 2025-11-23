# two_pointers_trap.py

from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0

    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0

    # Move the pointer from the side with smaller height
    while left <= right:
        if height[left] <= height[right]:
            # Left side is the limiting side
            if height[left] >= left_max:
                left_max = height[left]  # update left_max
            else:
                water += left_max - height[left]  # water trapped at left
            left += 1
        else:
            # Right side is the limiting side
            if height[right] >= right_max:
                right_max = height[right]  # update right_max
            else:
                water += right_max - height[right]  # water trapped at right
            right -= 1

    return water


if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))              # 9
