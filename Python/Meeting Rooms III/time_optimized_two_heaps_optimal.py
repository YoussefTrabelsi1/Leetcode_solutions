# file: time_optimized_two_heaps_optimal.py

from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n))
        heapq.heapify(available)

        busy = []  # (end_time, room)
        count = [0] * n

        for start, end in meetings:
            dur = end - start

            # Free up rooms that finished by 'start'
            while busy and busy[0][0] <= start:
                et, r = heapq.heappop(busy)
                heapq.heappush(available, r)

            if available:
                r = heapq.heappop(available)
                heapq.heappush(busy, (start + dur, r))
                count[r] += 1
            else:
                # Delay to earliest room release
                et, r = heapq.heappop(busy)
                new_start = et
                heapq.heappush(busy, (new_start + dur, r))
                count[r] += 1

        best = 0
        for r in range(1, n):
            if count[r] > count[best]:
                best = r
        return best


if __name__ == "__main__":
    s = Solution()
    print(s.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))  # 0
    print(s.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))  # 1
