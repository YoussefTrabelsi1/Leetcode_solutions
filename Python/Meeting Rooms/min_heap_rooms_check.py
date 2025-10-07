# filename: min_heap_rooms_check.py

from typing import List, Tuple
import heapq

def can_attend_meetings_heap(intervals: List[Tuple[int, int]]) -> bool:
    """
    Min-heap of end times; equivalent to checking if required rooms <= 1.
    Time: O(n log n), Space: O(n) in worst case.
    """
    if not intervals:
        return True

    intervals_sorted = sorted(intervals, key=lambda x: x[0])
    min_heap: List[int] = []  # stores end times

    for start, end in intervals_sorted:
        # Free all meetings that have ended by 'start'
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)
        if len(min_heap) > 1:
            return False
    return True


if __name__ == "__main__":
    print(can_attend_meetings_heap([(0,30),(5,10),(15,20)]))  # False
    print(can_attend_meetings_heap([(5,8),(9,15)]))           # True
    print(can_attend_meetings_heap([(0,8),(8,10)]))           # True
