class Solution:
    def kClosest(self, points, k: int):
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]