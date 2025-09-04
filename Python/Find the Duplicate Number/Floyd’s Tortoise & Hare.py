from typing import List

def find_duplicate_floyd(nums: List[int]) -> int:
    # Phase 1: find intersection in the cycle
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    # Phase 2: find entrance to the cycle = duplicate
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return hare

# Demo
print(find_duplicate_floyd([1,2,3,2,2]))  # 2
print(find_duplicate_floyd([1,2,3,4,4]))  # 4
