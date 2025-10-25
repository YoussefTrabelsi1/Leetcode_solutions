# filename: recursive_postorder.py

from typing import Optional, List, Tuple

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
    Recursive post-order removal.
    Time: O(sz), Space: O(sz) recursion stack.
    """
    dummy = ListNode(0, head)

    def recurse(node: Optional[ListNode]) -> int:
        if not node:
            return 0
        idx_from_end = recurse(node.next) + 1
        # When the next node is the nth from end, skip it
        if idx_from_end == n + 1:
            node.next = node.next.next
        return idx_from_end

    recurse(dummy)
    return dummy.next

if __name__ == "__main__":
    print(to_list(remove_nth_from_end(from_list([1,2,3,4]), 2)))  # [1,2,4]
    print(to_list(remove_nth_from_end(from_list([5]), 1)))        # []
    print(to_list(remove_nth_from_end(from_list([1,2]), 2)))      # [2]
