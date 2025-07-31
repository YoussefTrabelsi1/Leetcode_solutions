def is_special(nums):
    for a, b in zip(nums, nums[1:]):
        if a % 2 == b % 2:
            return False
    return True
