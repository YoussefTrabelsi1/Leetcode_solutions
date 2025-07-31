def is_special(nums):
    parity = [x % 2 for x in nums]
    return all(parity[i] != parity[i-1] for i in range(1, len(parity)))
