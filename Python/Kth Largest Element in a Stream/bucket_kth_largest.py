# file: bucket_kth_largest.py
from typing import List

class KthLargest:
    """
    Optimized for this problem's constraints: values are in [-1000, 1000].
    We maintain a frequency array and scan from high to low to find the k-th largest.
    """
    OFFSET = 1000
    RANGE = 2001  # covers [-1000, 1000]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.freq = [0] * self.RANGE
        self.count = 0
        if nums:
            for x in nums:
                self.freq[x + self.OFFSET] += 1
                self.count += 1

    def add(self, val: int) -> int:
        idx = val + self.OFFSET
        self.freq[idx] += 1
        self.count += 1

        # Walk from largest to smallest accumulating counts
        remaining = self.k
        for i in range(self.RANGE - 1, -1, -1):
            c = self.freq[i]
            if c == 0:
                continue
            remaining -= c
            if remaining <= 0:
                return i - self.OFFSET

        # Given the problem guarantees, this should not be reached.
        raise RuntimeError("Insufficient elements to determine the k-th largest.")

if __name__ == "__main__":
    # Example usage
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print("null")               # constructor
    print(kthLargest.add(3))    # -> 3
    print(kthLargest.add(5))    # -> 3
    print(kthLargest.add(6))    # -> 3
    print(kthLargest.add(7))    # -> 5
    print(kthLargest.add(8))    # -> 6
