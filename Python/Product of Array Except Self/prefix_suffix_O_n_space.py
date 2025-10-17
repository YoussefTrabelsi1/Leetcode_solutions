# prefix_suffix_O_n_space.py
# O(n) time, O(n) extra space.
# Precompute prefix and suffix products and multiply them for each index.

from typing import List

def product_except_self_prefix_suffix(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [1] * n
    suffix = [1] * n
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]
    for i in range(n - 2, -1, -1):
        suffix[i] = suffix[i + 1] * nums[i + 1]
    return [prefix[i] * suffix[i] for i in range(n)]

if __name__ == "__main__":
    print(product_except_self_prefix_suffix([1,2,3,4]))         # [24, 12, 8, 6]
    print(product_except_self_prefix_suffix([-1,1,0,-3,3]))     # [0, 0, 9, 0, 0]
