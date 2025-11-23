# brute_force_trap.py

from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0

    water = 0

    # For each position, look left and right to find max bars
    for i in range(n):
        # Max height to the left of i (including i)
        left_max = 0
        for l in range(i, -1, -1):
            left_max = max(left_max, height[l])

        # Max height to the right of i (including i)
        right_max = 0
        for r in range(i, n):
            right_max = max(right_max, height[r])

        # Water above this bar = min(left_max, right_max) - height[i]
        water += min(left_max, right_max) - height[i]

    return water


if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))              # 9
