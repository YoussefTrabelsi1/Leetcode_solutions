# ✅ Solution 2 — Space Optimized (Max-Heap of size k)
# Best when k << n
# Time: O(n log k)
# Space: O(k)

from typing import List
import heapq

def k_closest_heap(points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)
    if k <= 0:
        return []
    if k >= n:
        return points[:]

    # Python has a min-heap; use negative distance to simulate max-heap
    heap = []  # will store (-dist2, x, y)
    for x, y in points:
        d2 = x*x + y*y
        if len(heap) < k:
            heapq.heappush(heap, (-d2, x, y))
        else:
            # If current point is closer than the farthest in heap, replace it
            if -heap[0][0] > d2:
                heapq.heapreplace(heap, (-d2, x, y))

    # Extract points from heap
    return [[x, y] for _, x, y in heap]

# --- Example usage ---
if __name__ == "__main__":
    pts = [[1,3],[-2,2],[5,8],[0,1]]
    print("Heap:", k_closest_heap(pts, 2))
