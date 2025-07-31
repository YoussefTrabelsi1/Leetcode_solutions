def is_special(nums):
    return all((nums[i] % 2) != (nums[i-1] % 2) for i in range(1, len(nums)))
