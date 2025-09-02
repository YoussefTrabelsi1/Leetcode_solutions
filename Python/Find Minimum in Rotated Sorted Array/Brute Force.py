def find_min_bruteforce(nums):
    """
    Linear scan: just track the minimum while iterating.
    Time:  O(n)
    Space: O(1)
    """
    if not nums:
        raise ValueError("nums must be a non-empty list")
    m = nums[0]
    for x in nums[1:]:
        if x < m:
            m = x
    return m


if __name__ == "__main__":
    # Given examples
    print(find_min_bruteforce([3,4,5,6,1,2]))  # 1
    print(find_min_bruteforce([4,5,0,1,2,3]))  # 0
    print(find_min_bruteforce([4,5,6,7]))      # 4

    # Extra checks
    print(find_min_bruteforce([1]))            # 1
    print(find_min_bruteforce([2,3,4,5,6,7]))  # 2 (no rotation)
