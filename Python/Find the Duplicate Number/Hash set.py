from typing import List

def find_duplicate_hashset(nums: List[int]) -> int:
    seen = set()
    for x in nums:
        if x in seen:
            return x
        seen.add(x)
    raise ValueError("No duplicate found (input violates problem statement)")

# Demo
print(find_duplicate_hashset([1,2,3,2,2]))  # 2
print(find_duplicate_hashset([1,2,3,4,4]))  # 4
