# filename: heap_time_optimized.py

from typing import List, Optional
import heapq
import itertools

class ListNode:
    __slots__ = ("val", "next")
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Time-optimized using a min-heap of size at most k.
    Reuses existing nodes (no new node allocations except the dummy head).
    
    Time:  O(N log k)
    Space: O(k) for the heap
    """
    heap = []
    counter = itertools.count()  # tie-breaker to avoid comparing nodes
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, next(counter), node))

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, next(counter), node.next))

    tail.next = None
    return dummy.next

# ---------------------------
# Helpers for local testing
# ---------------------------
def arrays_to_lists(arrs: List[List[int]]) -> List[Optional[ListNode]]:
    out = []
    for arr in arrs:
        dummy = ListNode(0)
        tail = dummy
        for v in arr:
            tail.next = ListNode(v)
            tail = tail.next
        out.append(dummy.next)
    return out

def list_to_array(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    # Example tests
    for inp in [[[1,2,4],[1,3,5],[3,6]], [], [[]]]:
        lists = arrays_to_lists(inp)
        merged = mergeKLists(lists)
        print(list_to_array(merged))
