from typing import List


class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        res = []
        for q in queries:
            cur = -1
            for l, r in intervals:
                if l <= q <= r:
                    if cur == -1 or (r - l + 1) < cur:
                        cur = r - l + 1
            res.append(cur)
        return res