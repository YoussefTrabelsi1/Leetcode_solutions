# filename: brute_force_two_pass.py

from typing import Optional, List

class ListNode:
    __slots__ = ("val", "next")
    def __init__(self, val: int = 0, next: Optional["ListNode"]=None):
        self.val = val
        self.next = next

def from_list(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Brute force (two-pass via length): O(sz) time, O(1) extra space.
    """
    dummy = ListNode(0, head)
    # 1) compute length
    length = 0
    cur = head
    while cur:
        length += 1
        cur = cur.next
    # 2) advance to (length - n)-th node (node before target)
    steps = length - n
    prev = dummy
    for _ in range(steps):
        prev = prev.next
    # 3) remove
    if prev and prev.next:
        prev.next = prev.next.next
    return dummy.next

if __name__ == "__main__":
    # Provided examples
    print(to_list(remove_nth_from_end(from_list([1,2,3,4]), 2)))  # [1,2,4]
    print(to_list(remove_nth_from_end(from_list([5]), 1)))        # []
    print(to_list(remove_nth_from_end(from_list([1,2]), 2)))      # [2]
