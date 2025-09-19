# file: min_heap_kth_largest.py
from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        # Build a min-heap that keeps only the k largest elements
        if nums:
            for x in nums:
                self.add(x)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            # If the new value is larger than the smallest in heap, replace it
            if val > self.min_heap[0]:
                heapq.heapreplace(self.min_heap, val)
            # else do nothing; kth largest remains unchanged
        return self.min_heap[0]

if __name__ == "__main__":
    # Example usage
    kthLargest = KthLargest(3, [1, 2, 3, 3])
    print("null")               # constructor
    print(kthLargest.add(3))    # -> 3
    print(kthLargest.add(5))    # -> 3
    print(kthLargest.add(6))    # -> 3
    print(kthLargest.add(7))    # -> 5
    print(kthLargest.add(8))    # -> 6
