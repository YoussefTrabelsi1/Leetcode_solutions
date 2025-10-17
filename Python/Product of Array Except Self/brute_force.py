# brute_force.py
# O(n^2) time, O(1) extra space (excluding the output).
# Straightforward nested loops without division.

from typing import List

def product_except_self_bruteforce(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    for i in range(n):
        prod = 1
        for j in range(n):
            if i != j:
                prod *= nums[j]
        res[i] = prod
    return res

if __name__ == "__main__":
    print(product_except_self_bruteforce([1,2,3,4]))         # [24, 12, 8, 6]
    print(product_except_self_bruteforce([-1,1,0,-3,3]))     # [0, 0, 9, 0, 0]
