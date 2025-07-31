def is_special(nums):
    for i in range(1, len(nums)):
        if nums[i] % 2 == nums[i-1] % 2:  # same parity
            return False
    return True
