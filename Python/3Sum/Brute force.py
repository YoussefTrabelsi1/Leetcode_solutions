from typing import List

def three_sum_bruteforce(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    seen = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    trip = tuple(sorted((nums[i], nums[j], nums[k])))
                    seen.add(trip)
    return [list(t) for t in seen]
