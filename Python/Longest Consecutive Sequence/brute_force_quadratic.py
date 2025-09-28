# brute_force_quadratic.py
# Brute-force (O(n^2) time, O(1) extra space)
# For each value, we linearly scan to see if (val+1), (val+2), ... are present.

from typing import List

def longest_consecutive_bruteforce(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0

    def contains(arr, target):
        # Linear scan: O(n)
        for x in arr:
            if x == target:
                return True
        return False

    best = 0
    for v in nums:  # O(n)
        # Try to build the streak starting at v by repeated linear contains checks
        length = 1
        next_val = v + 1
        while contains(nums, next_val):  # Each check is O(n); total worst-case O(n^2)
            length += 1
            next_val += 1
        if length > best:
            best = length
    return best

if __name__ == "__main__":
    print(longest_consecutive_bruteforce([100,4,200,1,3,2]))           # 4
    print(longest_consecutive_bruteforce([0,3,7,2,5,8,4,6,0,1]))       # 9
