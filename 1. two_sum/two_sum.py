def twoSum( nums, target):
    
    Map={}

    for i,num in enumerate(nums):

        diff=target-num

        if diff in Map:
            return [Map[diff],i]
        else:
            Map[num]=i
        
print(twoSum([2,7,11,15], 9))

print(twoSum([3,2,4], 6))

print(twoSum([3,3], 6))