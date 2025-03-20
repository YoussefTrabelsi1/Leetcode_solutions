class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start, path):
            # Append the current subset to the result
            result.append(path[:])
            # Iterate through the remaining numbers
            for i in range(start, len(nums)):
                # Include nums[i] in the subset
                path.append(nums[i])
                # Recurse to build further subsets
                backtrack(i + 1, path)
                # Backtrack and remove the last element
                path.pop()
        
        result = []
        backtrack(0, [])
        return result