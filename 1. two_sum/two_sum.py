def twoSum( nums, target):
    
    Map={}

    for i,num in enumerate(nums):

        diff=target-num

        if diff in Map:
            return [Map[diff],i]
        else:
            Map[num]=i
        
assert twoSum([2,7,11,15], 9)==[0, 1]

assert twoSum([3,2,4], 6)==[1,2]  

assert twoSum([3,3], 6)==[0,1]  