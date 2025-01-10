def twoSum( nums, target):
    
    Map={}

    for i,num in enumerate(nums):

        diff=target-num

        if diff in Map:
            return [Map[diff],i]
        else:
            Map[num]=i
        
nums = [2,7,11,15]
target = 9

assert twoSum(nums, target)==[0, 1]