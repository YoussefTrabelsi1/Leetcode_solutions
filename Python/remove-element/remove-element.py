def removeElement(nums, val):
    k = 0  # Pointer for elements not equal to `val`
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # Move the element to the position `k`
            k += 1  # Increment `k` to store the next valid element

    return k  # Return the count of elements not equal to `val`
