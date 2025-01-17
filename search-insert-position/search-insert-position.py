def searchInsert(nums, target):

    low=0
    high=len(nums)

    while low<high:
        mid=(low+high)//2
        if nums[mid]<target:
            low=mid+1
        else:
            high=mid
    
    return low


nums = [1,3,5,6]
target = 5

print(searchInsert(nums, target))

nums = [1,3,5,6]
target = 2

print(searchInsert(nums, target))


nums = [1,3,5,6]
target = 7

print(searchInsert(nums, target))
