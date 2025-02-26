def twoSum(nums, target):
    map={}
    for i,num in enumerate(nums):
        if target-num in map:
            return [map[target-num],i]
        map[num]=i

        
print(twoSum([2,7,11,15], 9))

print(twoSum([3,2,4], 6))

print(twoSum([3,3], 6))