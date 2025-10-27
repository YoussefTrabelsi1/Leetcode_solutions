# filename: time_optimized_o_n_space.py
# Approach: Time-optimized (O(n) time) using an indexable array of nodes.
# Stores all nodes in a list, then relinks by two-pointer interleaving.
# Extra space O(n); simpler and very fast in practice.

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
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    i, j = 0, len(nodes) - 1
    # We will relink in-place using the array references
    while i < j:
        nodes[i].next = nodes[j]
        i += 1
        if i == j:
            break
        nodes[j].next = nodes[i]
        j -= 1
    nodes[i].next = None  # terminate

if __name__ == "__main__":
    # Example 1
    h = build_linked_list([2,4,6,8])
    reorder_list(h)
    print(to_list(h))  # [2,8,4,6]

    # Example 2
    h = build_linked_list([2,4,6,8,10])
    reorder_list(h)
    print(to_list(h))  # [2,10,4,8,6]
