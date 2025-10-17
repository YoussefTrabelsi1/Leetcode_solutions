# zero_aware_single_pass_variant.py
# O(n) time, O(1) extra space, explicitly handling zero counts in one scan + one pass.
# This version shows the logic when zeros are present, equivalent to the optimal one
# but spells out the zero cases first, then fills the result accordingly.

from typing import List

def product_except_self_zero_aware(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [0] * n
    zero_count = 0
    total_product_nonzero = 1
    for x in nums:
        if x == 0:
            zero_count += 1
        else:
            total_product_nonzero *= x

    if zero_count >= 2:
        # All results remain 0
        return res
    if zero_count == 1:
        # Only the index with zero gets the product of nonzero elements
        for i, x in enumerate(nums):
            if x == 0:
                res[i] = total_product_nonzero
        return res

    # No zeros: compute using running prefix from left within res
    res[0] = 1
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    # multiply by running suffix from right
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res

if __name__ == "__main__":
    print(product_except_self_zero_aware([1,2,3,4]))         # [24, 12, 8, 6]
    print(product_except_self_zero_aware([-1,1,0,-3,3]))     # [0, 0, 9, 0, 0]
