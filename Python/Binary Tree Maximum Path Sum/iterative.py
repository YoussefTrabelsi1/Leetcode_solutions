# Iterative post-order traversal to avoid recursion.
# We compute gains bottom-up using a postorder list and a hashmap.

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

def maxPathSum_iterative(root: TreeNode) -> int:
    if not root:
        return 0

    # Build post-order sequence
    post = []
    stack = []
    cur, last = root, None
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            peek = stack[-1]
            if peek.right and last is not peek.right:
                cur = peek.right
            else:
                post.append(peek)
                last = stack.pop()

    gains = {}
    best = -inf
    for node in post:
        lg = max(0, gains.get(node.left, 0))
        rg = max(0, gains.get(node.right, 0))
        best = max(best, node.val + lg + rg)
        gains[node] = node.val + max(lg, rg)
    return best

# ---- Demo ----
if __name__ == "__main__":
    root1 = build_tree_level([1,2,3])
    print(maxPathSum_iterative(root1))  # 6

    root2 = build_tree_level([-15,10,20,None,None,15,5,-5])
    print(maxPathSum_iterative(root2))  # 40
