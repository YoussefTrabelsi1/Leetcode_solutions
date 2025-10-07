# filename: sweep_line_two_pointers.py

from typing import List, Tuple

def can_attend_meetings_sweepline(intervals: List[Tuple[int, int]]) -> bool:
    """
    Line sweep with two pointers.
    Time: O(n log n) for sorting starts/ends. Space: O(n) for the arrays.
    Early-exits if max overlap exceeds 1.
    """
    if not intervals:
        return True
    starts = sorted(s for s, _ in intervals)
    ends = sorted(e for _, e in intervals)
    i = j = 0
    ongoing = 0
    n = len(intervals)

    while i < n and j < n:
        if starts[i] < ends[j]:
            ongoing += 1
            if ongoing > 1:
                return False
            i += 1
        else:
            # If starts[i] == ends[j], that's not a conflict; end first.
            j += 1
            if ongoing > 0:
                ongoing -= 1
    return True


if __name__ == "__main__":
    print(can_attend_meetings_sweepline([(0,30),(5,10),(15,20)]))  # False
    print(can_attend_meetings_sweepline([(5,8),(9,15)]))           # True
    print(can_attend_meetings_sweepline([(0,8),(8,10)]))           # True
