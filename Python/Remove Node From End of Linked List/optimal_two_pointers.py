# filename: optimal_two_pointers.py

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
    Optimal single-pass two-pointer with dummy head.
    Time: O(sz), Space: O(1).
    """
    dummy = ListNode(0, head)
    fast = slow = dummy
    # Move fast n+1 steps ahead so the gap is n and slow ends up before the target
    for _ in range(n + 1):
        fast = fast.next
    # Move both until fast hits the end
    while fast:
        fast = fast.next
        slow = slow.next
    # Delete slow.next
    slow.next = slow.next.next
    return dummy.next

if __name__ == "__main__":
    print(to_list(remove_nth_from_end(from_list([1,2,3,4]), 2)))  # [1,2,4]
    print(to_list(remove_nth_from_end(from_list([5]), 1)))        # []
    print(to_list(remove_nth_from_end(from_list([1,2]), 2)))      # [2]
