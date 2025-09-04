from typing import List

def find_duplicate_sort(nums: List[int], mutate: bool = False) -> int:
    arr = nums if mutate else sorted(nums)
    if mutate:
        arr.sort()
    for i in range(1, len(arr)):
        if arr[i] == arr[i-1]:
            return arr[i]
    raise ValueError("No duplicate found (input violates problem statement)")

# Demo
print(find_duplicate_sort([1,2,3,2,2]))  # 2
print(find_duplicate_sort([1,2,3,4,4]))  # 4
