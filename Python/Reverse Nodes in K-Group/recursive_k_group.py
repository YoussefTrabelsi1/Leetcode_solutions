# filename: recursive_k_group.py
# Approach: Recursive. If a segment of length k exists, reverse it and recurse on the rest.
# Clean and concise, but uses call stack O(n/k). Values untouched.
# Time O(n), extra space O(n/k) due to recursion depth.

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

def list_to_linked(arr: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def linked_to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or k <= 1:
        return head

    # Check k nodes ahead
    tail = head
    for _ in range(k):
        if not tail:
            return head
        tail = tail.next

    # Reverse k nodes starting at head
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # 'prev' is new head of this block, 'head' is tail. Recurse on remaining starting at 'curr'
    head.next = reverseKGroup(curr, k)
    return prev

# --- quick self-check ---
if __name__ == "__main__":
    head = list_to_linked([1,2,3,4,5,6])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,6,5,4]

    head = list_to_linked([1,2,3,4,5])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,4,5]
