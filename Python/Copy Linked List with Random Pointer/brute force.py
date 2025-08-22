# BRUTE FORCE: O(n^2) time, O(n) extra space for holding clones
# ------------------------------------------------------------
# Idea:
# 1) Make a linear array of cloned nodes (same order/values).
# 2) Wire their 'next' pointers sequentially.
# 3) For each original node i, find the index j of original.random by linear scan,
#    then set clones[i].random = clones[j].

from typing import Optional, List, Tuple, Union

class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random

def build_list(pairs: List[Tuple[int, Union[int, None]]]) -> Optional[Node]:
    """Builds a linked list with random pointers from [[val, random_index], ...]."""
    if not pairs:
        return None
    nodes = [Node(val) for val, _ in pairs]
    # next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    # random pointers
    for i, (_, ridx) in enumerate(pairs):
        nodes[i].random = nodes[ridx] if ridx is not None else None
    return nodes[0]

def to_pairs(head: Optional[Node]) -> List[Tuple[int, Union[int, None]]]:
    """Converts a list to [[val, random_index], ...] format."""
    nodes = []
    idx = {}
    cur = head
    i = 0
    while cur:
        nodes.append(cur)
        idx[cur] = i
        cur = cur.next
        i += 1
    res = []
    for i, node in enumerate(nodes):
        r = node.random
        res.append([node.val, idx[r] if r in idx else None])
    return res

def copyRandomList_bruteforce(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    # Collect length and allow index-based access to original by repeated traversal
    # Build clones array with same order
    clones = []
    cur = head
    while cur:
        clones.append(Node(cur.val))
        cur = cur.next
    n = len(clones)

    # Wire 'next' of clones
    for i in range(n - 1):
        clones[i].next = clones[i + 1]

    # Helper: get original node at index k by walking from head (O(k))
    def get_original_at(k: int) -> Node:
        c = head
        for _ in range(k):
            c = c.next
        return c

    # Helper: find index of a target original node by linear scan from head (O(n))
    def find_index_of_original(target: Optional[Node]) -> Optional[int]:
        if target is None:
            return None
        c, j = head, 0
        while c:
            if c is target:
                return j
            c = c.next
            j += 1
        return None

    # Set random for clones using linear scans (O(n^2) total)
    for i in range(n):
        orig_i = get_original_at(i)
        j = find_index_of_original(orig_i.random)
        clones[i].random = clones[j] if j is not None else None

    return clones[0]

# ------------------ Demo / Tests ------------------
if __name__ == "__main__":
    # Example 1
    inp1 = [[3, None],[7,3],[4,0],[5,1]]
    h1 = build_list(inp1)
    c1 = copyRandomList_bruteforce(h1)
    print(to_pairs(c1))  # Expected: [[3,None],[7,3],[4,0],[5,1]]

    # Example 2
    inp2 = [[1, None],[2,2],[3,2]]
    h2 = build_list(inp2)
    c2 = copyRandomList_bruteforce(h2)
    print(to_pairs(c2))  # Expected: [[1,None],[2,2],[3,2]]
