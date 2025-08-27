# Optimal: only the node to delete is given (not the head).
# Copy the next node's value into this node and bypass the next.
# Time: O(1). Space: O(1).

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def delete_node_O1(node: ListNode) -> None:
    if node is None or node.next is None:
        # Problem guarantees node is not the tail, but guard just in case.
        raise ValueError("Node must not be the tail.")
    nxt = node.next
    node.val = nxt.val
    node.next = nxt.next
    nxt.next = None  # help GC; not required for correctness

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

# -------- Demo (matches the prompt's examples) --------
if __name__ == "__main__":
    head = build_list([4,5,1,9])
    node = find_node(head, 5)  # we only pass `node` to the deletion function
    delete_node_O1(node)
    print(to_list(head))  # [4, 1, 9]

    head = build_list([4,5,1,9])
    node = find_node(head, 1)
    delete_node_O1(node)
    print(to_list(head))  # [4, 5, 9]
