# Alternative without head: shift values left from each next node until the tail,
# then unlink the final node. Maintains order but costs O(k) where k = distance to tail.
# Time: O(k). Space: O(1).

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def delete_node_shift(node: ListNode) -> None:
    if node is None or node.next is None:
        raise ValueError("Node must not be the tail.")
    prev = None
    curr = node
    # Shift values forward until the last node
    while curr.next:
        curr.val = curr.next.val
        prev = curr
        curr = curr.next
    # Now 'curr' is the old tail, and 'prev' is its previous
    prev.next = None

# -------- Helpers for testing --------
def build_list(vals: List[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def find_node(head: Optional[ListNode], target: int) -> Optional[ListNode]:
    curr = head
    while curr:
        if curr.val == target:
            return curr
        curr = curr.next
    return None

def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

# -------- Demo --------
if __name__ == "__main__":
    head = build_list([4,5,1,9])
    node = find_node(head, 5)
    delete_node_shift(node)
    print(to_list(head))  # [4, 1, 9]

    head = build_list([4,5,1,9])
    node = find_node(head, 1)
    delete_node_shift(node)
    print(to_list(head))  # [4, 5, 9]
