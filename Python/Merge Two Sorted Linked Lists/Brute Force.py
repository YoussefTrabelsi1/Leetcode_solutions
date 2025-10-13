# filename: brute_force_merge.py

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def merge_two_lists_bruteforce(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Brute force:
      1) Dump all node values into an array
      2) Sort the array
      3) Rebuild a new linked list from the sorted values
    Time: O((n+m) log(n+m))  |  Space: O(n+m) for the array + O(n+m) new nodes
    """
    values: List[int] = []
    cur = list1
    while cur:
        values.append(cur.val)
        cur = cur.next
    cur = list2
    while cur:
        values.append(cur.val)
        cur = cur.next

    values.sort()

    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
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
    print(to_list(merge_two_lists_bruteforce(l1, l2)))  # [1,1,2,3,4,5]

    # Example 2
    l1 = build_list([])
    l2 = build_list([1,2])
    print(to_list(merge_two_lists_bruteforce(l1, l2)))  # [1,2]

    # Example 3
    l1 = build_list([])
    l2 = build_list([])
    print(to_list(merge_two_lists_bruteforce(l1, l2)))  # []
