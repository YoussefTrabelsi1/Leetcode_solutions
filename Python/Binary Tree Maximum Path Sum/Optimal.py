# Classic post-order DFS: at each node, compute the best "gain" you can send upward,
# and update a global maximum for a path that bends at this node.
# Complexity: O(N) time, O(H) space (H = tree height).

from math import inf
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val  = val
        self.left = left
        self.right= right

def build_tree_level(values):
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
    try:
        v_left = next(it)
        cur = q.popleft()
        if v_left is not None:
            cur.left = TreeNode(v_left)
            q.append(cur.left)
    except StopIteration:
        pass
    return root

def maxPathSum_optimal(root: TreeNode) -> int:
    best = -inf
    def dfs(node):
        nonlocal best
        if not node:
            return 0
        left_gain  = max(0, dfs(node.left))
        right_gain = max(0, dfs(node.right))
        # Path that bends at 'node':
        best = max(best, node.val + left_gain + right_gain)
        # Best one-side gain to parent:
        return node.val + max(left_gain, right_gain)
    dfs(root)
    return best

# ---- Demo ----
if __name__ == "__main__":
    root1 = build_tree_level([1,2,3])
    print(maxPathSum_optimal(root1))  # 6

    root2 = build_tree_level([-15,10,20,None,None,15,5,-5])
    print(maxPathSum_optimal(root2))  # 40
