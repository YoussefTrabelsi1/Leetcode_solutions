from typing import List

def find_duplicate_binary_search(nums: List[int]) -> int:
    # Values are in [1, n], length = n+1
    lo, hi = 1, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        # Count how many numbers <= mid
        cnt = sum(x <= mid for x in nums)
        if cnt > mid:
            # Duplicate is in [lo, mid]
            hi = mid
        else:
            # Duplicate is in [mid+1, hi]
            lo = mid + 1
    return lo

# Demo
print(find_duplicate_binary_search([1,2,3,2,2]))  # 2
print(find_duplicate_binary_search([1,2,3,4,4]))  # 4
