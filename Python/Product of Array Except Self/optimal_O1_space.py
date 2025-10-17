# optimal_O1_space.py
# O(n) time, O(1) extra space (excluding the output).
# Use the output array to store prefix products, then sweep from the right
# accumulating a running suffix product.

from typing import List

def product_except_self_optimal(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    # res[i] will hold product of all elements to the LEFT of i
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    # carry will hold product of all elements to the RIGHT of i
    carry = 1
    for i in range(n - 1, -1, -1):
        res[i] *= carry
        carry *= nums[i]
    return res

if __name__ == "__main__":
    print(product_except_self_optimal([1,2,3,4]))         # [24, 12, 8, 6]
    print(product_except_self_optimal([-1,1,0,-3,3]))     # [0, 0, 9, 0, 0]
