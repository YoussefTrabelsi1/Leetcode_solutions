# brute_force.py
# O(n^2) time, O(1) extra space (will TLE for n=1e5, but correct)

from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        ans = 0
        for i in range(n):
            ans = max(ans, events[i][2])  # take only one
            si, ei, vi = events[i]
            for j in range(i + 1, n):
                sj, ej, vj = events[j]
                # non-overlap with inclusive ends: need ei < sj OR ej < si
                if ei < sj or ej < si:
                    ans = max(ans, vi + vj)
        return ans
