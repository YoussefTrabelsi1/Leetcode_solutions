# HASH MAP: O(n) time, O(n) extra space (optimal time, clean & standard)
# ----------------------------------------------------------------------
# Idea:
# 1) First pass: map each original node -> cloned node with same val.
# 2) Second pass: set clone.next = map[orig.next], clone.random = map[orig.random].

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

def copyRandomList_hashmap(head: Optional[Node]) -> Optional[Node]:
    if not head:
        return None

    mp = {}  # original -> clone

    # First pass: create clones (val only)
    cur = head
    while cur:
        mp[cur] = Node(cur.val)
        cur = cur.next

    # Second pass: wire next/random via the map
    cur = head
    while cur:
        clone = mp[cur]
        clone.next = mp.get(cur.next)
        clone.random = mp.get(cur.random)
        cur = cur.next

    return mp[head]

# ------------------ Demo / Tests ------------------
if __name__ == "__main__":
    # Example 1
    inp1 = [[3, None],[7,3],[4,0],[5,1]]
    h1 = build_list(inp1)
    c1 = copyRandomList_hashmap(h1)
    print(to_pairs(c1))  # Expected: [[3,None],[7,3],[4,0],[5,1]]

    # Example 2
    inp2 = [[1, None],[2,2],[3,2]]
    h2 = build_list(inp2)
    c2 = copyRandomList_hashmap(h2)
    print(to_pairs(c2))  # Expected: [[1,None],[2,2],[3,2]]
