# Brute force: explore every simple path by starting DFS from each node
# and walking over the implicit undirected tree (left, right, parent).
# Complexity: O(N^2) time in the worst case (e.g., a chain), O(N) space.

from collections import defaultdict, deque
from math import inf

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right= right

def build_tree_level(values):
    """Build a binary tree from level-order list with None for missing nodes."""
    if not values:
        return None
    it = iter(values)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for v_left, v_right in zip(it, it):
        cur = q.popleft()
        if v_left is not None:
            cur.left = TreeNode(v_left)
            q.append(cur.left)
        if v_right is not None:
            cur.right = TreeNode(v_right)
            q.append(cur.right)
    # If odd length, there may be one last left child value hanging
    try:
        v_left = next(it)
        cur = q.popleft()
        if v_left is not None:
            cur.left = TreeNode(v_left)
            q.append(cur.left)
    except StopIteration:
        pass
    return root

def maxPathSum_bruteforce(root: TreeNode) -> int:
    if not root:
        return 0

    # Build undirected adjacency to allow walking paths in any direction.
    adj = defaultdict(list)
    nodes = []

    stack = [root]
    while stack:
        n = stack.pop()
        nodes.append(n)
        if n.left:
            adj[n].append(n.left); adj[n.left].append(n)
            stack.append(n.left)
        if n.right:
            adj[n].append(n.right); adj[n.right].append(n)
            stack.append(n.right)

    best = -inf

    # For each node, DFS all simple paths starting there (avoid revisiting via 'prev')
    for start in nodes:
        if start.val > best:
            best = start.val
        s = [(start, None, start.val)]
        while s:
            node, prev, acc = s.pop()
            for nei in adj[node]:
                if nei is prev:
                    continue
                new_sum = acc + nei.val
                if new_sum > best:
                    best = new_sum
                s.append((nei, node, new_sum))
    return best

# ---- Demo ----
if __name__ == "__main__":
    root1 = build_tree_level([1,2,3])
    print(maxPathSum_bruteforce(root1))  # 6

    root2 = build_tree_level([-15,10,20,None,None,15,5,-5])
    print(maxPathSum_bruteforce(root2))  # 40
