# ✅ Solution 1 — Brute Force (Sort Everything)
# Time: O(n log n) due to sorting
# Space: O(n) to hold all distances

from typing import List, Tuple

def k_closest_bruteforce(points: List[List[int]], k: int) -> List[List[int]]:
    n = len(points)
    if k <= 0: 
        return []
    if k >= n:
        return points[:]  # any order allowed

    # Pair each point with its squared distance
    with_dist: List[Tuple[int, List[int]]] = []
    for p in points:
        d2 = p[0]*p[0] + p[1]*p[1]
        with_dist.append((d2, p))

    # Sort by distance and take first k points
    with_dist.sort(key=lambda t: t[0])
    return [p for _, p in with_dist[:k]]

# --- Example usage ---
if __name__ == "__main__":
    pts = [[1,3],[-2,2],[5,8],[0,1]]
    print("Brute Force:", k_closest_bruteforce(pts, 2))
