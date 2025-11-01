# filename: head_insertion_block_reversal.py
# Approach: In-place "head-insertion" within each k-block.
# We keep the block's head anchored after group_prev; then iteratively move the next node
# to the front of the block k-1 times. O(n) time, O(1) extra space.
# (A different flavor of the iterative solution; often faster in practice due to fewer pointer writes.)

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

    # Count length
    n = 0
    cur = head
    while cur:
        n += 1
        cur = cur.next

    dummy = ListNode(0, head)
    group_prev = dummy
    curr = head

    while n >= k:
        # After this loop, the first k nodes after group_prev will be reversed.
        # 'curr' will become the tail of the block.
        for _ in range(k - 1):
            move = curr.next           # node to move to front
            curr.next = move.next      # detach 'move' from its current spot
            move.next = group_prev.next# link 'move' to current block head
            group_prev.next = move     # put 'move' at the block front
        # Advance to next group
        group_prev = curr
        curr = curr.next
        n -= k

    return dummy.next

# --- quick self-check ---
if __name__ == "__main__":
    head = list_to_linked([1,2,3,4,5,6])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,6,5,4]

    head = list_to_linked([1,2,3,4,5])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,4,5]
