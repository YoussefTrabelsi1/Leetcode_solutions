import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        adj = [[] for _ in range(n)]
        dist = [[INF] * (k + 5) for _ in range(n)]
        for u, v, cst in flights:
            adj[u].append([v, cst])
        
        dist[src][0] = 0
        minHeap = [(0, src, -1)] # cost, node, stops
        while len(minHeap):
            cst, node, stops = heapq.heappop(minHeap)
            if dst == node: return cst
            if stops == k or dist[node][stops + 1] < cst:
                continue
            for nei, w in adj[node]:
                nextCst = cst + w
                nextStops = 1 + stops
                if dist[nei][nextStops + 1] > nextCst:
                    dist[nei][nextStops + 1] = nextCst
                    heapq.heappush(minHeap, (nextCst, nei, nextStops))

        return -1