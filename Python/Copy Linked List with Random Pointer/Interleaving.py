# INTERLEAVING / O(1) EXTRA SPACE: O(n) time, O(1) space
# -------------------------------------------------------
# Idea:
# 1) Interleave clone nodes immediately after each original: A -> A' -> B -> B' -> ...
# 2) Set A'.random = A.random.next (because A.random's clone sits right after it).
# 3) Detach the interleaved list into original and cloned lists.

from typing import Optional, List, Tuple, Union

class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random

def build_list(pairs: List[Tuple[int, Union[int, None]]]) -> Optional[Node]:
    if not pairs:
        return None
    nodes = [Node(val) for val, _ in pairs]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i, (_, ridx) in enumerate(pairs):
        nodes[i].random = nodes[ridx] if ridx is not None else None
    return nodes[0]

def to_pairs(head: Optional[Node]) -> List[Tuple[int, Union[int, None]]]:
    nodes, idx = [], {}
    cur, i = head, 0
    while cur:
        nodes.append(cur)
        idx[cur] = i
        cur = cur.next
        i += 1
    res = []
    for node in nodes:
        res.append([node.val, idx[node.random] if node.random in idx else None])
    return res

def copyRandomList_interleaved(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    # 1) Interleave cloned nodes
    cur = head
    while cur:
        nxt = cur.next
        copy = Node(cur.val, next=nxt)
        cur.next = copy
        cur = nxt

    # 2) Assign random for clones (cur points to originals)
    cur = head
    while cur:
        copy = cur.next
        copy.random = cur.random.next if cur.random else None
        cur = copy.next

    # 3) Detach the copy list
    dummy = Node(0)
    copy_tail = dummy
    cur = head
    while cur:
        copy = cur.next
        nxt_orig = copy.next

        # append copy
        copy_tail.next = copy
        copy_tail = copy

        # restore original next
        cur.next = nxt_orig
        cur = nxt_orig

    return dummy.next

# ------------------ Demo / Tests ------------------
if __name__ == "__main__":
    # Example 1
    inp1 = [[3, None],[7,3],[4,0],[5,1]]
    h1 = build_list(inp1)
    c1 = copyRandomList_interleaved(h1)
    print(to_pairs(c1))  # Expected: [[3,None],[7,3],[4,0],[5,1]]

    # Example 2
    inp2 = [[1, None],[2,2],[3,2]]
    h2 = build_list(inp2)
    c2 = copyRandomList_interleaved(h2)
    print(to_pairs(c2))  # Expected: [[1,None],[2,2],[3,2]]
