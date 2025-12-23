# fenwick_max.py
# O(n log n) time, O(n) space, alternative approach using BIT over end times

from typing import List
from bisect import bisect_left

class FenwickMax:
    def __init__(self, n: int):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i: int, val: int) -> None:
        while i <= self.n:
            if val > self.bit[i]:
                self.bit[i] = val
            i += i & -i

    def query(self, i: int) -> int:
        res = 0
        while i > 0:
            if self.bit[i] > res:
                res = self.bit[i]
            i -= i & -i
        return res

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # coordinate compress end times
        ends = sorted({e[1] for e in events})
        bit = FenwickMax(len(ends))

        # process by increasing start; BIT stores best value for each end
        events_sorted = sorted(events, key=lambda x: x[0])

        ans = 0
        for s, e, v in events_sorted:
            # best event with end < s
            idx = bisect_left(ends, s)  # first end >= s, so <s are before it
            best_prev = bit.query(idx)  # idx is count, also Fenwick index
            ans = max(ans, v, best_prev + v)

            # update this event at its end position
            pos = bisect_left(ends, e) + 1
            bit.update(pos, v)

        return ans
