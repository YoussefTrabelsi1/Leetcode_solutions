# dp_prefix_suffix_trap.py

from typing import List

def trap(height: List[int]) -> int:
    n = len(height)
    if n == 0:
        return 0

    # Precompute highest bar to the left for each index
    left_max = [0] * n
    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    # Precompute highest bar to the right for each index
    right_max = [0] * n
    right_max[-1] = height[-1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    # Water at each index is determined by min(left_max, right_max)
    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
    print(trap([4,2,0,3,2,5]))              # 9
