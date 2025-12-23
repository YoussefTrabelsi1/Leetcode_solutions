# suffix_binary_search.py
# O(n log n) time, O(n) extra space (suffix max), standard fast solution

from typing import List
from bisect import bisect_left

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])  # sort by start
        n = len(events)
        starts = [e[0] for e in events]

        suffix_max = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], events[i][2])

        ans = 0
        for i in range(n):
            s, e, v = events[i]
            ans = max(ans, v)  # take only this event
            j = bisect_left(starts, e + 1)  # next must start >= end+1
            ans = max(ans, v + suffix_max[j])
        return ans
