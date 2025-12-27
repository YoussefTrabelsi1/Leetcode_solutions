# file: brute_force_scan_all_rooms.py

from typing import List

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        end_time = [0] * n
        count = [0] * n

        for start, end in meetings:
            dur = end - start

            # Find the smallest free room
            chosen = -1
            for r in range(n):
                if end_time[r] <= start:
                    chosen = r
                    break

            if chosen != -1:
                end_time[chosen] = start + dur
                count[chosen] += 1
            else:
                # Delay: choose room that frees earliest (tie -> smaller index)
                earliest = 0
                for r in range(1, n):
                    if end_time[r] < end_time[earliest] or (end_time[r] == end_time[earliest] and r < earliest):
                        earliest = r
                new_start = end_time[earliest]
                end_time[earliest] = new_start + dur
                count[earliest] += 1

        best = 0
        for r in range(1, n):
            if count[r] > count[best]:
                best = r
        return best


if __name__ == "__main__":
    s = Solution()
    print(s.mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))  # 0
    print(s.mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))  # 1
