def removeDuplicates(nums):
    if not nums:
        return 0

    # Use two pointers: `i` for the position of the unique element
    i = 0

    for j in range(1, len(nums)):
        if nums[j] != nums[i]:  # Found a new unique element
            i += 1  # Move `i` to the next position
            nums[i] = nums[j]  # Copy the unique element to position `i`
    
    # Return the number of unique elements
    return i + 1
