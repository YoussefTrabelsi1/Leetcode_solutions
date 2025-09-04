from typing import List

def find_duplicate_bruteforce(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]
    raise ValueError("No duplicate found (input violates problem statement)")

# Demo
print(find_duplicate_bruteforce([1,2,3,2,2]))  # 2
print(find_duplicate_bruteforce([1,2,3,4,4]))  # 4
