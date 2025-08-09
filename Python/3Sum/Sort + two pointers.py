from typing import List


def three_sum_two_pointers(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue  # skip duplicate anchor
        # since array sorted, if anchor > 0, no triplet can sum to 0
        if nums[i] > 0:
            break
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                # skip duplicates on left and right
                l_val, r_val = nums[l], nums[r]
                while l < r and nums[l] == l_val: l += 1
                while l < r and nums[r] == r_val: r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
