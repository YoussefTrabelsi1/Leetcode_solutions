# filename: linear_time_hashmaps.py

from typing import List
from collections import defaultdict

MOD = 10**9 + 7

def count_special_triplets(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0

    # right initially has the frequency of all elements
    right = defaultdict(int)
    for v in nums:
        right[v] += 1

    left = defaultdict(int)
    ans = 0

    for j, v in enumerate(nums):
        # remove nums[j] from the right part (j is the middle now)
        right[v] -= 1

        target = 2 * v
        left_count = left.get(target, 0)
        right_count = right.get(target, 0)

        if left_count and right_count:
            ans = (ans + left_count * right_count) % MOD

        # now j moves to the left side for the next iterations
        left[v] += 1

    return ans


if __name__ == "__main__":
    print(count_special_triplets([6, 3, 6]))       # 1
    print(count_special_triplets([0, 1, 0, 0]))    # 1
    print(count_special_triplets([8, 4, 2, 8, 4])) # 2
