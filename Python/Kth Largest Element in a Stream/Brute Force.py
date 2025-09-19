# file: brute_force_kth_largest.py
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = list(nums or [])

    def add(self, val: int) -> int:
        self.nums.append(val)
        # Sort descending and pick the k-th element
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]

if __name__ == "__main__":
    # Example usage
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print("null")               # constructor
    print(kthLargest.add(3))    # -> 3
    print(kthLargest.add(5))    # -> 3
    print(kthLargest.add(6))    # -> 3
    print(kthLargest.add(7))    # -> 5
    print(kthLargest.add(8))    # -> 6
