# filename: reverse_list_recursive.py

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Recursion: reverse the sublist [head.next..] and attach head at the end.
    Time: O(n), Space: O(n) due to recursion stack.
    """
    if head is None or head.next is None:
        return head
    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None
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
    res = reverse_list_recursive(head)
    print(to_list(res))  # [3, 2, 1, 0]

    # Example 2
    head = build_list([])
    res = reverse_list_recursive(head)
    print(to_list(res))  # []
