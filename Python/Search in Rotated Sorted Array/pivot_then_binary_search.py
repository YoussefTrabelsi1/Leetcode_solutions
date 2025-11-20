# file: pivot_then_binary_search.py

from typing import List

def find_pivot(nums: List[int]) -> int:
    """
    Find index of the smallest element (rotation pivot) in O(log n).
    nums is a rotated sorted array with unique elements.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        # Pivot is in the right half if mid element is greater than the rightmost
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # Pivot is in the left half including mid
            right = mid
    return left  # index of the smallest element (rotation pivot)


def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
    """
    Standard binary search on a subarray nums[left:right+1].
    """
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def search(nums: List[int], target: int) -> int:
    """
    Time-optimized O(log n) using:
    1. O(log n) pivot search to find rotation point.
    2. O(log n) binary search in the appropriate half.
    Total: O(log n) time, O(1) extra space.
    """
    if not nums:
        return -1

    n = len(nums)
    pivot = find_pivot(nums)

    # If array is not rotated, pivot will be 0 (smallest is first element)
    if nums[pivot] <= target <= nums[n - 1]:
        # Target is in the right sorted half
        return binary_search(nums, pivot, n - 1, target)
    else:
        # Target is in the left sorted half
        return binary_search(nums, 0, pivot - 1, target)


if __name__ == "__main__":
    # Example 1
    nums = [3, 4, 5, 6, 1, 2]
    target = 1
    print(search(nums, target))  # Expected: 4

    # Example 2
    nums = [3, 5, 6, 0, 1, 2]
    target = 4
    print(search(nums, target))  # Expected: -1
