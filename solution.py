import heapq


class Solution:
    def kClosest(self, points, k: int):
        points.sort(key=lambda p: p[0]**2 + p[1]**2)
        return points[:k]
class Solution:
    def kClosest(self, points, k: int) :
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res