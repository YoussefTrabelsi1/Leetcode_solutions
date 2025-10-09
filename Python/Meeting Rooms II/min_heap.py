# filename: 02_min_heap_nlogn.py
# Time-optimized classic solution using a min-heap of end times (O(n log n) time, O(n) space)
# Keep earliest meeting end at heap top; if it ends before current start, reuse that "day".

from typing import List, Tuple
import heapq

def min_days_heap(intervals: List[Tuple[int,int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    heap: List[int] = []  # stores end times
    for s,e in intervals:
        while heap and heap[0] <= s:
            heapq.heappop(heap)  # free a day that has finished (<= s means no conflict at boundary)
        heapq.heappush(heap, e)  # allocate/occupy a day until e
    return len(heap)

if __name__ == "__main__":
    print(min_days_heap([(0,40),(5,10),(15,20)]))  # 2
    print(min_days_heap([(4,9)]))                  # 1
    print(min_days_heap([(0,8),(8,10)]))           # 1
    print(min_days_heap([]))                       # 0
