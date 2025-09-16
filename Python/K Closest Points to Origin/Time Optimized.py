# ✅ Solution 3 — Time Optimized (Quickselect in-place)
# Average Time: O(n) to find the k-th boundary + O(k log k) optional final sort
# Space: O(1) extra (in-place partitioning)
# Note: Any order is acceptable; we optionally sort the first k for stable output.

from typing import List
import random

def k_closest_quickselect(points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)
    if k <= 0:
        return []
    if k >= n:
        return points[:]

    def dist2(i: int) -> int:
        x, y = points[i]
        return x*x + y*y

    def partition(left: int, right: int, pivot_idx: int) -> int:
        pivot_dist = dist2(pivot_idx)
        # Move pivot to end
        points[pivot_idx], points[right] = points[right], points[pivot_idx]
        store = left
        for i in range(left, right):
            if dist2(i) <= pivot_dist:
                points[store], points[i] = points[i], points[store]
                store += 1
        # Move pivot to its final place
        points[store], points[right] = points[right], points[store]
        return store

    def quickselect(left: int, right: int, k_smallest: int):
        while left <= right:
            pivot_idx = random.randint(left, right)
            mid = partition(left, right, pivot_idx)
            if mid == k_smallest:
                return
            elif mid < k_smallest:
                left = mid + 1
            else:
                right = mid - 1

    # Select k elements with smallest distances (indices 0..k-1 after partitioning)
    quickselect(0, n - 1, k - 1)

    # Optionally sort the first k by distance for nicer output (not required)
    first_k = points[:k]
    first_k.sort(key=lambda p: p[0]*p[0] + p[1]*p[1])
    return first_k

# --- Example usage ---
if __name__ == "__main__":
    pts = [[1,3],[-2,2],[5,8],[0,1],[2,-2]]
    print("Quickselect:", k_closest_quickselect(pts, 2))
