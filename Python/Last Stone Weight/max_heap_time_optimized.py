# filename: max_heap_time_optimized.py

from typing import List
import heapq

def last_stone_weight_heap(stones: List[int]) -> int:
    """
    Time-optimized using a max-heap (via negatives).
    Time: O(n log n); Space: O(n).
    """
    heap = [-s for s in stones]
    heapq.heapify(heap)
    while len(heap) > 1:
        y = -heapq.heappop(heap)  # heaviest
        x = -heapq.heappop(heap)  # second heaviest
        if y != x:
            heapq.heappush(heap, -(y - x))
    return -heap[0] if heap else 0


if __name__ == "__main__":
    print(last_stone_weight_heap([2,3,6,2,4]))  # 1
    print(last_stone_weight_heap([1,2]))        # 1
