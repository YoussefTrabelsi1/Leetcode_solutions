# brute_force_merge.py

from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Brute force: merge then take median.
    Time: O(m+n), Space: O(m+n)
    """
    m, n = len(nums1), len(nums2)
    merged = [0] * (m + n)
    i = j = k = 0

    while i < m and j < n:
        if nums1[i] <= nums2[j]:
            merged[k] = nums1[i]
            i += 1
        else:
            merged[k] = nums2[j]
            j += 1
        k += 1

    while i < m:
        merged[k] = nums1[i]; i += 1; k += 1
    while j < n:
        merged[k] = nums2[j]; j += 1; k += 1

    total = m + n
    mid = total // 2
    if total % 2 == 1:
        return float(merged[mid])
    else:
        return (merged[mid - 1] + merged[mid]) / 2.0


if __name__ == "__main__":
    print(find_median_sorted_arrays([1,3], [2]))        # 2.0
    print(find_median_sorted_arrays([1,2], [3,4]))      # 2.5
    print(find_median_sorted_arrays([], [1]))           # 1.0
    print(find_median_sorted_arrays([0,0], [0,0]))      # 0.0
