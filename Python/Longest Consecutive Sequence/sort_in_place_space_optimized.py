# sort_in_place_space_optimized.py
# Space-optimized approach: sort in-place then sweep (O(n log n) time, O(1) extra besides sorting).
# NOTE: This modifies the input list order. If you must preserve it, pass a copy.

from typing import List

def longest_consecutive_sort_in_place(nums: List[int]) -> int:
    if not nums:
        return 0
    nums.sort()  # In-place sort; Python's Timsort is O(n log n)
    best = 1
    curr = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]:
            # duplicate; ignore it for counting, don't reset streak
            continue
        if nums[i] == nums[i-1] + 1:
            curr += 1
            if curr > best:
                best = curr
        else:
            curr = 1
    return best

if __name__ == "__main__":
    print(longest_consecutive_sort_in_place([100,4,200,1,3,2]))           # 4
    print(longest_consecutive_sort_in_place([0,3,7,2,5,8,4,6,0,1]))       # 9
