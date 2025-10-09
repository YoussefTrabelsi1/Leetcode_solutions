# filename: 04_event_sweep_nlogn.py
# Alternative optimal line-sweep with event markers (O(n log n) time, O(n) space)
# Create (+1) at start, (-1) at end. Sort events; to honor non-conflict at endpoints,
# process end events before start events when times are equal.

from typing import List, Tuple

def min_days_event_sweep(intervals: List[Tuple[int,int]]) -> int:
    if not intervals:
        return 0
    events = []
    for s,e in intervals:
        events.append((s, 1))   # start
        events.append((e, -1))  # end
    # Sort by time; for equal time, end (-1) before start (+1) to avoid counting boundary as conflict
    events.sort(key=lambda x: (x[0], x[1]))
    cur = ans = 0
    for _,delta in events:
        cur += delta
        if cur > ans:
            ans = cur
    return ans

if __name__ == "__main__":
    print(min_days_event_sweep([(0,40),(5,10),(15,20)]))  # 2
    print(min_days_event_sweep([(4,9)]))                  # 1
    print(min_days_event_sweep([(0,8),(8,10)]))           # 1
    print(min_days_event_sweep([]))                       # 0
