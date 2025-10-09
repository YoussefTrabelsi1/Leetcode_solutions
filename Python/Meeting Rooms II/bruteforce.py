# filename: 01_bruteforce_greedy_n2.py
# Brute-force-ish greedy (O(n^2) time, O(n) space)
# For each interval, linearly scan existing "days" to place it if no overlap; otherwise open a new day.
# Overlap rule: [s1,e1) and [s2,e2) conflict iff s2 < e1 and s1 < e2.
# Non-conflict at endpoints: if start >= last_end, it's fine.

from typing import List, Tuple

def min_days_bruteforce(intervals: List[Tuple[int,int]]) -> int:
    if not intervals:
        return 0
    # Sort by start time to make greedy valid for interval graphs
    intervals.sort(key=lambda x: x[0])
    # Track for each day the last end time scheduled on that day
    day_last_end: List[int] = []
    for s,e in intervals:
        placed = False
        # Try to place on some existing day
        for i in range(len(day_last_end)):
            if s >= day_last_end[i]:
                # Can schedule here; update last_end
                day_last_end[i] = e
                placed = True
                break
        if not placed:
            day_last_end.append(e)
    return len(day_last_end)

if __name__ == "__main__":
    print(min_days_bruteforce([(0,40),(5,10),(15,20)]))  # 2
    print(min_days_bruteforce([(4,9)]))                  # 1
    print(min_days_bruteforce([(0,8),(8,10)]))           # 1
    print(min_days_bruteforce([]))                       # 0
