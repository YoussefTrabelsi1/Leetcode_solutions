# filename: quadratic_space_optimized.py

from typing import List

MOD = 10**9 + 7

def count_special_triplets(nums: List[int]) -> int:
    n = len(nums)
    ans = 0

    # j must be strictly between i and k, so 1 .. n-2
    for j in range(1, n - 1):
        target = 2 * nums[j]

        # count how many nums[i] == target for i < j
        left_count = 0
        for i in range(j):
            if nums[i] == target:
                left_count += 1

        if left_count == 0:
            continue  # no need to scan right if left is zero

        # count how many nums[k] == target for k > j
        right_count = 0
        for k in range(j + 1, n):
            if nums[k] == target:
                right_count += 1

        ans = (ans + left_count * right_count) % MOD

    return ans


if __name__ == "__main__":
    print(count_special_triplets([6, 3, 6]))       # 1
    print(count_special_triplets([0, 1, 0, 0]))    # 1
    print(count_special_triplets([8, 4, 2, 8, 4])) # 2
