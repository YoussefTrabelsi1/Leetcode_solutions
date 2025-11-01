# filename: iterative_inplace_two_pointers.py
# Approach: Optimal iterative in-place group reversal using O(1) extra space.
# For each k-block, reverse pointers, stitch the block between 'group_prev' and 'next_group_head'.
# O(n) time, O(1) space.

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

    # Utility: check there are at least k nodes from 'start'
    def has_k(start: Optional[ListNode], k: int) -> bool:
        cnt = 0
        while start and cnt < k:
            start = start.next
            cnt += 1
        return cnt == k

    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        group_head = group_prev.next
        if not has_k(group_head, k):
            break

        # Reverse k nodes
        prev = None
        curr = group_head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 'prev' is new head of this block; 'group_head' is now tail
        # 'curr' is head of next block
        group_prev.next.next = curr      # old head -> next block
        next_group_prev = group_prev.next  # will become the previous for the next round (tail now)
        group_prev.next = prev           # connect previous block to new head

        group_prev = next_group_prev     # advance

    return dummy.next

# --- quick self-check ---
if __name__ == "__main__":
    head = list_to_linked([1,2,3,4,5,6])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,6,5,4]

    head = list_to_linked([1,2,3,4,5])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,4,5]
