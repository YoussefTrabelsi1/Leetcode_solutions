# filename: brute_force_triplets.py

from typing import List

MOD = 10**9 + 7

def count_special_triplets(nums: List[int]) -> int:
    n = len(nums)
    ans = 0

    for i in range(n):
        for j in range(i + 1, n):
            # nums[i] must be 2 * nums[j]
            if nums[i] != 2 * nums[j]:
                continue
            for k in range(j + 1, n):
                # nums[k] must also be 2 * nums[j]
                if nums[k] == 2 * nums[j]:
                    ans += 1
                    if ans >= MOD:
                        ans -= MOD

    return ans % MOD


if __name__ == "__main__":
    print(count_special_triplets([6, 3, 6]))       # 1
    print(count_special_triplets([0, 1, 0, 0]))    # 1
    print(count_special_triplets([8, 4, 2, 8, 4])) # 2
