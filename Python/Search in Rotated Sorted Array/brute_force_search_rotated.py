# file: brute_force_search_rotated.py

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Brute-force O(n) time, O(1) extra space.
    Simply scan linearly and return index if found, else -1.
    """
    for i, val in enumerate(nums):
        if val == target:
            return i
    return -1


if __name__ == "__main__":
    # Example 1
    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    print(search(nums, target))  # Expected: 4

    # Example 2
    nums = [3, 5, 6, 0, 1, 2]
    target = 4
    print(search(nums, target))  # Expected: -1
