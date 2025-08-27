# Brute force: you have access to head. Find the previous node and unlink.
# Time: O(n) to scan from head. Space: O(1).

from typing import Optional, List

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def delete_node_bruteforce(head: Optional[ListNode], node: ListNode) -> Optional[ListNode]:
    if head is None:
        return None
    # If the node to delete is the head
    if head is node:
        nxt = head.next
        head.next = None
        return nxt
    # Find previous of `node`
    prev = head
    while prev and prev.next is not node:
        prev = prev.next
    if prev is None:
        raise ValueError("Given node is not in the list.")
    prev.next = node.next
    node.next = None
    return head

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
    node = find_node(head, 5)  # delete value 5
    head = delete_node_bruteforce(head, node)
    print(to_list(head))  # [4, 1, 9]

    head = build_list([4,5,1,9])
    node = find_node(head, 1)  # delete value 1
    head = delete_node_bruteforce(head, node)
    print(to_list(head))  # [4, 5, 9]
