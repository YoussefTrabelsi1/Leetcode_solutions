# filename: iterative_pairwise_merge_alternative.py

from typing import List, Optional

class ListNode:
    __slots__ = ("val", "next")
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def merge_two(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Alternative optimal approach: repeatedly merge the two smallest-length lists.
    Uses a simple queue based on lengths to reduce constant factors when list sizes vary.
    
    Time:  O(N log k) in general
    Space: O(1) extra beyond the list of heads
    """
    # Filter out empty lists
    queues = [(length_of_list(node), node) for node in lists if node]
    if not queues:
        return None
    # Sort by length and repeatedly merge the two shortest
    queues.sort(key=lambda x: x[0])
    while len(queues) > 1:
        (len1, l1) = queues.pop(0)
        (len2, l2) = queues.pop(0)
        merged = merge_two(l1, l2)
        queues.append((len1 + len2, merged))
        # Keep list sorted by length
        # (for k up to 1000 and 100 max length each, this is fine; could use heap for better asymptotics)
        queues.sort(key=lambda x: x[0])
    return queues[0][1]

def length_of_list(node: Optional[ListNode]) -> int:
    c = 0
    while node:
        c += 1
        node = node.next
    return c

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
