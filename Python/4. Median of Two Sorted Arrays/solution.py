def findMedianSortedArrays(nums1, nums2):
    
    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total_length = m + n
    half_length = (total_length + 1) // 2

    # Binary search on the smaller array
    left, right = 0, m
    while left <= right:
        partition1 = (left + right) // 2
        partition2 = half_length - partition1

        # Handle edges
        maxLeft1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
        minRight1 = nums1[partition1] if partition1 < m else float('inf')

        maxLeft2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
        minRight2 = nums2[partition2] if partition2 < n else float('inf')

        # Check if partition is valid
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Found the correct partition
            if total_length % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            # Move left in nums1
            right = partition1 - 1
        else:
            # Move right in nums1
            left = partition1 + 1

# Example usage:
nums1 = [1, 3]
nums2 = [2]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))  # Output: 2.5
