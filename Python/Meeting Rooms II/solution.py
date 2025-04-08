"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from collections import defaultdict
import heapq


class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort(key=lambda x: x.start)
        min_heap = []

        for interval in intervals:
            if min_heap and min_heap[0] <= interval.start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)

        return len(min_heap)

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        mp = defaultdict(int)
        for i in intervals:
            mp[i.start] += 1
            mp[i.end] -= 1
        prev = 0
        res = 0
        for i in sorted(mp.keys()):
            prev += mp[i]
            res = max(res, prev)
        return res