# two_pointer_stream.py

from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Space-optimized two-pointer: walk until the median position.
    Time: O(m+n), Space: O(1)
    """
    m, n = len(nums1), len(nums2)
    total = m + n
    target1 = (total - 1) // 2  # left median index
    target2 = total // 2        # right median index

    i = j = -1
    a = b = 0  # last two seen numbers
    p1 = p2 = 0  # pointers within arrays

    while (i < target2) and (p1 < m or p2 < n):
        prev = b
        if p2 >= n or (p1 < m and nums1[p1] <= nums2[p2]):
            b = nums1[p1]; p1 += 1
        else:
            b = nums2[p2]; p2 += 1
        i += 1
        if i == target1:
            a = b
        if i == target1 + 1:
            # prev == element at target1
            a = prev

    if total % 2 == 1:
        return float(b)  # i == target2
    else:
        return (a + b) / 2.0


if __name__ == "__main__":
    print(find_median_sorted_arrays([1,3], [2]))        # 2.0
    print(find_median_sorted_arrays([1,2], [3,4]))      # 2.5
    print(find_median_sorted_arrays([], [1]))           # 1.0
    print(find_median_sorted_arrays([0,0], [0,0]))      # 0.0
