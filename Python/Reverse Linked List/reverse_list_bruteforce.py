# filename: reverse_list_bruteforce.py

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def reverse_list_bruteforce(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Brute force: dump values to an array, reverse the array,
    then rebuild a new linked list from the reversed values.
    Time: O(n), Space: O(n) extra.
    """
    # Collect values
    vals: List[int] = []
    curr = head
    while curr:
        vals.append(curr.val)
        curr = curr.next

    # Rebuild reversed list
    new_head: Optional[ListNode] = None
    tail: Optional[ListNode] = None
    for v in reversed(vals):
        node = ListNode(v)
        if new_head is None:
            new_head = node
            tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return new_head

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
    res = reverse_list_bruteforce(head)
    print(to_list(res))  # [3, 2, 1, 0]

    # Example 2
    head = build_list([])
    res = reverse_list_bruteforce(head)
    print(to_list(res))  # []
