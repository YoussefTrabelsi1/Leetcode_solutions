# file: space_optimized_one_heap_plus_scan.py

from typing import List
import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        end_time = [0] * n
        count = [0] * n

        # busy: (end_time, room)
        busy = []
        for r in range(n):
            heapq.heappush(busy, (0, r))  # initially all "free" at time 0

        for start, end in meetings:
            dur = end - start

            # Pop all rooms that are free by 'start' into a temporary list
            freed = []
            while busy and busy[0][0] <= start:
                et, r = heapq.heappop(busy)
                freed.append((et, r))

            # Mark freed rooms as available by setting end_time properly (already <= start)
            # We must push them back after choosing, so we don't lose them.

            # Find smallest available room among freed rooms
            chosen = None
            if freed:
                chosen = min(r for _, r in freed)
                # push back all other freed rooms as free
                for et, r in freed:
                    if r != chosen:
                        heapq.heappush(busy, (et, r))

                # schedule chosen at 'start'
                new_end = start + dur
                heapq.heappush(busy, (new_end, chosen))
                count[chosen] += 1
            else:
                # No room free at 'start' => delay to earliest end
                et, r = heapq.heappop(busy)
                new_start = et
                new_end = new_start + dur
                heapq.heappush(busy, (new_end, r))
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
