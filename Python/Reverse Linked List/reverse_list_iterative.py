# filename: reverse_list_iterative.py

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Space-optimized, in-place iterative reversal using three pointers.
    Time: O(n), Space: O(1).
    """
    prev: Optional[ListNode] = None
    curr: Optional[ListNode] = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# ----- Helpers & tests -----
def build_list(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    tail = dummy
    for v in arr:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out: List[int] = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    # Example 1
    head = build_list([0, 1, 2, 3])
    res = reverse_list_iterative(head)
    print(to_list(res))  # [3, 2, 1, 0]

    # Example 2
    head = build_list([])
    res = reverse_list_iterative(head)
    print(to_list(res))  # []
