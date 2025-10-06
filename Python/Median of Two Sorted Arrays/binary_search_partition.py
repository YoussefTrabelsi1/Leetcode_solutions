# binary_search_partition.py

from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Optimal time O(log(min(m, n))) using binary search on partition.
    Space: O(1)
    """
    A, B = nums1, nums2
    m, n = len(A), len(B)

    # Ensure A is the smaller array
    if m > n:
        A, B, m, n = B, A, n, m

    if n == 0:
        raise ValueError("At least one array must be non-empty per constraints.")

    total = m + n
    half = (total + 1) // 2  # left partition size

    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2         # cut in A (left size in A)
        j = half - i               # cut in B

        A_left_max  = A[i-1] if i > 0 else float("-inf")
        A_right_min = A[i]   if i < m else float("inf")
        B_left_max  = B[j-1] if j > 0 else float("-inf")
        B_right_min = B[j]   if j < n else float("inf")

        # Check if correct partition
        if A_left_max <= B_right_min and B_left_max <= A_right_min:
            if total % 2 == 1:
                return float(max(A_left_max, B_left_max))
            else:
                left_max  = max(A_left_max, B_left_max)
                right_min = min(A_right_min, B_right_min)
                return (left_max + right_min) / 2.0
        elif A_left_max > B_right_min:
            # Move left in A
            hi = i - 1
        else:
            # Move right in A
            lo = i + 1

    # Should never reach here if inputs are valid and sorted
    raise ValueError("Input arrays must be sorted.")


if __name__ == "__main__":
    print(find_median_sorted_arrays([1,3], [2]))        # 2.0
    print(find_median_sorted_arrays([1,2], [3,4]))      # 2.5
    print(find_median_sorted_arrays([], [1]))           # 1.0
    print(find_median_sorted_arrays([0,0], [0,0]))      # 0.0
