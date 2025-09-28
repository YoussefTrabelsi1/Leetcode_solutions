# hashset_optimal_time.py
# Time-optimized O(n) using a hash set.
# Idea: only start counting from numbers that have no predecessor (x-1 not in set).

from typing import List

def longest_consecutive_hashset(nums: List[int]) -> int:
    s = set(nums)                 # O(n)
    best = 0
    for x in s:                   # O(n)
        if x - 1 not in s:        # x is a potential start
            length = 1
            y = x + 1
            while y in s:         # Each element visited at most once overall
                length += 1
                y += 1
            if length > best:
                best = length
    return best

if __name__ == "__main__":
    print(longest_consecutive_hashset([100,4,200,1,3,2]))           # 4
    print(longest_consecutive_hashset([0,3,7,2,5,8,4,6,0,1]))       # 9
