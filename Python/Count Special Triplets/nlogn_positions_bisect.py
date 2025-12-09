# filename: nlogn_positions_bisect.py

from typing import List
from collections import defaultdict
import bisect

MOD = 10**9 + 7

def count_special_triplets(nums: List[int]) -> int:
    n = len(nums)
    if n < 3:
        return 0

    # map value -> sorted list of indices where it appears
    positions = defaultdict(list)
    for idx, v in enumerate(nums):
        positions[v].append(idx)

    ans = 0

    for j, v in enumerate(nums):
        target = 2 * v
        if target not in positions:
            continue

        pos_list = positions[target]

        # number of indices < j
        left_count = bisect.bisect_left(pos_list, j)
        # number of indices > j
        right_count = len(pos_list) - bisect.bisect_right(pos_list, j)

        if left_count and right_count:
            ans = (ans + left_count * right_count) % MOD

    return ans


if __name__ == "__main__":
    print(count_special_triplets([6, 3, 6]))       # 1
    print(count_special_triplets([0, 1, 0, 0]))    # 1
    print(count_special_triplets([8, 4, 2, 8, 4])) # 2
