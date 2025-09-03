def find_min_pivot(nums):
    """
    Finds the rotation pivot (index of minimum) using binary search,
    leveraging the sorted halves property.
    Time:  O(log n)
    Space: O(1)
    """
    if not nums:
        raise ValueError("nums must be a non-empty list")

    lo, hi = 0, len(nums) - 1

    # If array is not rotated (already sorted), first element is min.
    if nums[lo] <= nums[hi]:
        return nums[lo]

    # Binary search for the pivot (the only place where nums[i] < nums[i-1])
    while lo <= hi:
        mid = (lo + hi) // 2
        # Check if mid is the pivot (smaller than previous)
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        # Decide which side is sorted and move accordingly
        if nums[mid] >= nums[lo]:
            # Left half [lo..mid] is sorted; pivot must be in right half
            lo = mid + 1
        else:
            # Right half [mid..hi] is sorted; pivot must be in left half
            hi = mid - 1

    # Fallback (shouldn't hit with valid rotated sorted unique array)
    return nums[0]


if __name__ == "__main__":
    # Given examples
    print(find_min_pivot([3,4,5,6,1,2]))  # 1
    print(find_min_pivot([4,5,0,1,2,3]))  # 0
    print(find_min_pivot([4,5,6,7]))      # 4

    # Edge cases
    print(find_min_pivot([1]))            # 1
    print(find_min_pivot([2,3,4,5,6,7]))  # 2 (no rotation)
