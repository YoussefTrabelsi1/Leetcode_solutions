# filename: brute_force_array_relink.py
# Approach: Brute-force using an array of node references, reverse each k-block in the array,
# then relink pointers from the reordered array. O(n) time, O(n) extra space. Values untouched.

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

    # Collect node references
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    # Reverse in chunks of k by reordering references (no value changes)
    for i in range(0, len(nodes), k):
        if i + k <= len(nodes):
            nodes[i:i+k] = reversed(nodes[i:i+k])

    # Relink pointers according to the new order
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if nodes:
        nodes[-1].next = None
        return nodes[0]
    return None

# --- quick self-check ---
if __name__ == "__main__":
    head = list_to_linked([1,2,3,4,5,6])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,6,5,4]

    head = list_to_linked([1,2,3,4,5])
    k = 3
    print(linked_to_list(reverseKGroup(head, k)))  # [3,2,1,4,5]
