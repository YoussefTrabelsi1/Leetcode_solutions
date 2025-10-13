# filename: iterative_inplace_merge.py

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def merge_two_lists_inplace(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Space-optimized / In-place iterative merge using a dummy head.
    Reuses existing nodes; only O(1) extra space.
    Time: O(n+m)  |  Space: O(1)
    """
    dummy = ListNode()
    tail = dummy
    p1, p2 = list1, list2

    while p1 and p2:
        if p1.val <= p2.val:
            tail.next = p1
            p1 = p1.next
        else:
            tail.next = p2
            p2 = p2.next
        tail = tail.next

    # Attach remainder
    tail.next = p1 if p1 else p2
    return dummy.next

# ---- Utilities to help run & verify ----
def build_list(nums: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for x in nums:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    # Example 1
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,5])
    print(to_list(merge_two_lists_inplace(l1, l2)))  # [1,1,2,3,4,5]

    # Example 2
    l1 = build_list([])
    l2 = build_list([1,2])
    print(to_list(merge_two_lists_inplace(l1, l2)))  # [1,2]

    # Example 3
    l1 = build_list([])
    l2 = build_list([])
    print(to_list(merge_two_lists_inplace(l1, l2)))  # []
