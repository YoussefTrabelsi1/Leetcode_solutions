from typing import List


def three_sum_hashset(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    res = set()
    for i in range(n):
        target = -nums[i]
        seen = set()
        for j in range(i+1, n):
            need = target - nums[j]
            if need in seen:
                trip = tuple(sorted((nums[i], nums[j], need)))
                res.add(trip)
            seen.add(nums[j])
    return [list(t) for t in res]
