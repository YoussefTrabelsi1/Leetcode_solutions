# filename: deque_o_n_space.py
# Approach: O(n) time using a deque for clarity; extra space O(n).
# Pop from both ends and interleave.

from typing import Optional, List
from collections import deque

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
    dq = deque()
    cur = head
    while cur:
        dq.append(cur)
        cur = cur.next
    dummy = ListNode()
    tail = dummy
    toggle = True  # True: take from left (front), False: right (back)
    while dq:
        node = dq.popleft() if toggle else dq.pop()
        tail.next = node
        tail = tail.next
        toggle = not toggle
    tail.next = None

if __name__ == "__main__":
    # Example 1
    h = build_linked_list([2,4,6,8])
    reorder_list(h)
    print(to_list(h))  # [2,8,4,6]

    # Example 2
    h = build_linked_list([2,4,6,8,10])
    reorder_list(h)
    print(to_list(h))  # [2,10,4,8,6]
