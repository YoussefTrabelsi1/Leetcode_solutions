def find_min_binary(nums):
    """
    Classic binary search for rotated sorted array with UNIQUE elements.
    Invariant: minimum is always within [lo, hi].
    If nums[mid] > nums[hi], minimum is in (mid, hi]; else it's in [lo, mid].
    Time:  O(log n)
    Space: O(1)
    """
    if not nums:
        raise ValueError("nums must be a non-empty list")

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            # Minimum is strictly to the right of mid
            lo = mid + 1
        else:
            # Minimum is at mid or to the left of mid
            hi = mid
    return nums[lo]


if __name__ == "__main__":
    # Given examples
    print(find_min_binary([3,4,5,6,1,2]))  # 1
    print(find_min_binary([4,5,0,1,2,3]))  # 0
    print(find_min_binary([4,5,6,7]))      # 4

    # Edge cases
    print(find_min_binary([1]))            # 1
    print(find_min_binary([2,3,4,5,6,7]))  # 2 (no rotation)
