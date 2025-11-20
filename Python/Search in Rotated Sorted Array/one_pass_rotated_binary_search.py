# file: one_pass_rotated_binary_search.py

from typing import List

def search(nums: List[int], target: int) -> int:
    """
    Space- and time-optimized one-pass binary search in a rotated sorted array.
    Directly decides which half is sorted at each step and narrows the search.
    Runs in O(log n) time, O(1) extra space.
    """
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check which side is sorted: left..mid or mid..right
        if nums[left] <= nums[mid]:
            # Left half is sorted
            if nums[left] <= target < nums[mid]:
                # Target lies in the sorted left half
                right = mid - 1
            else:
                # Target lies in the right half
                left = mid + 1
        else:
            # Right half is sorted
            if nums[mid] < target <= nums[right]:
                # Target lies in the sorted right half
                left = mid + 1
            else:
                # Target lies in the left half
                right = mid - 1

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
