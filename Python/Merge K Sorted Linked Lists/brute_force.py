# filename: brute_force.py

from typing import List, Optional

class ListNode:
    __slots__ = ("val", "next")
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Brute force:
    1) Collect all values.
    2) Sort them.
    3) Build a new linked list from the sorted values.

    Time:  O(N log N) where N is total nodes
    Space: O(N) extra to store values (creates new nodes)
    """
    values = []
    for head in lists:
        while head:
            values.append(head.val)
            head = head.next
    if not values:
        return None
    values.sort()
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
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
