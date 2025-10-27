# filename: brute_force_n2_o1.py
# Approach: Brute Force (O(n^2) time, O(1) extra space)
# Repeatedly find the last node and splice it after the current front node.

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def build_linked_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return
    cur = head
    while cur and cur.next:
        # Find prev_to_last and last
        prev, tail = None, cur
        while tail.next:
            prev, tail = tail, tail.next
        if tail is cur or tail is cur.next:
            # No more reordering needed (already interleaved)
            break
        # Splice: cur -> tail -> cur.next -> ...
        nxt = cur.next
        cur.next = tail
        tail.next = nxt
        # Cut tail from its previous position
        if prev:
            prev.next = None
        # Advance to the next pair spot
        cur = nxt

if __name__ == "__main__":
    # Example 1
    h = build_linked_list([2,4,6,8])
    reorder_list(h)
    print(to_list(h))  # [2,8,4,6]

    # Example 2
    h = build_linked_list([2,4,6,8,10])
    reorder_list(h)
    print(to_list(h))  # [2,10,4,8,6]
    # Example 3
    h = build_linked_list([1,2,3,4,5])
    reorder_list(h)
    print(to_list(h))  # [1,5,2,4,3]