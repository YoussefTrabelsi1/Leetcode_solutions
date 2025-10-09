# filename: 03_two_pointer_space_optimized.py
# Space-optimized sweep with two pointers (O(n log n) time for sorting, O(1) extra space beyond the arrays)
# Extract starts and ends, sort each, then sweep to find peak overlap (max concurrent intervals).

from typing import List, Tuple

def min_days_two_pointer(intervals: List[Tuple[int,int]]) -> int:
    n = len(intervals)
    if n == 0:
        return 0
    starts = [s for s,_ in intervals]
    ends   = [e for _,e in intervals]
    starts.sort()
    ends.sort()
    i = j = 0
    used = max_used = 0
    while i < n and j < n:
        if starts[i] < ends[j]:
            used += 1           # a meeting starts before the next one ends → need another day
            if used > max_used:
                max_used = used
            i += 1
        else:
            # ends[j] <= starts[i] → one meeting finished; boundary equality frees a day
            used -= 1
            j += 1
    return max_used

if __name__ == "__main__":
    print(min_days_two_pointer([(0,40),(5,10),(15,20)]))  # 2
    print(min_days_two_pointer([(4,9)]))                  # 1
    print(min_days_two_pointer([(0,8),(8,10)]))           # 1
    print(min_days_two_pointer([]))                       # 0
