# filename: sort_adjacent_inplace.py

from typing import List, Tuple

def can_attend_meetings_sort_inplace(intervals: List[Tuple[int, int]]) -> bool:
    """
    Sort by start time in-place (O(n log n) time, O(1) extra space besides sort).
    Check only adjacent intervals for conflicts.
    """
    intervals.sort(key=lambda x: x[0])  # in-place
    for i in range(1, len(intervals)):
        # conflict if current starts before previous ends
        if intervals[i][0] < intervals[i-1][1]:
            return False
    return True


if __name__ == "__main__":
    data1 = [(0,30),(5,10),(15,20)]
    data2 = [(5,8),(9,15)]
    data3 = [(0,8),(8,10)]
    print(can_attend_meetings_sort_inplace(data1))  # False
    print(can_attend_meetings_sort_inplace(data2))  # True
    print(can_attend_meetings_sort_inplace(data3))  # True
