# filename: recursive_merge.py

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def merge_two_lists_recursive(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Time-optimized alternative (also O(n+m)) using recursion.
    Uses call stack space up to O(n+m).
    Time: O(n+m)  |  Space: O(n+m) recursion depth
    """
    if not list1:
        return list2
    if not list2:
        return list1
    if list1.val <= list2.val:
        list1.next = merge_two_lists_recursive(list1.next, list2)
        return list1
    else:
        list2.next = merge_two_lists_recursive(list1, list2.next)
        return list2

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
    print(to_list(merge_two_lists_recursive(l1, l2)))  # [1,1,2,3,4,5]

    # Example 2
    l1 = build_list([])
    l2 = build_list([1,2])
    print(to_list(merge_two_lists_recursive(l1, l2)))  # [1,2]

    # Example 3
    l1 = build_list([])
    l2 = build_list([])
    print(to_list(merge_two_lists_recursive(l1, l2)))  # []
