# Iterative LCA using BST property
# Time: O(h) where h is tree height; Space: O(1)
# This simultaneously optimizes time (vs. full traversal) and space.

from collections import deque
from typing import Optional, List, Any

class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional['TreeNode'] = None,
                 right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_level(values: List[Any]) -> Optional[TreeNode]:
    if not values:
        return None
    vals = [None if (v is None or v == 'null') else v for v in values]
    root = TreeNode(vals[0])
    q = deque([root])
    i = 1
    n = len(vals)
    while q and i < n:
        node = q.popleft()
        if i < n and vals[i] is not None:
            node.left = TreeNode(vals[i])
            q.append(node.left)
        i += 1
        if i < n and vals[i] is not None:
            node.right = TreeNode(vals[i])
            q.append(node.right)
        i += 1
    return root

def find_node_bst(root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
    """Standard BST search (unique values)."""
    cur = root
    while cur:
        if target < cur.val:
            cur = cur.left
        elif target > cur.val:
            cur = cur.right
        else:
            return cur
    return None

def lowest_common_ancestor_bst_iter(root: TreeNode, p_val: int, q_val: int) -> TreeNode:
    """Iterative LCA using BST structure."""
    cur = root
    lo, hi = (p_val, q_val) if p_val < q_val else (q_val, p_val)
    while cur:
        if hi < cur.val:           # both in left subtree
            cur = cur.left
        elif lo > cur.val:         # both in right subtree
            cur = cur.right
        else:
            return cur             # split point (or one equals current)
    raise RuntimeError("LCA not found (inputs may be invalid).")

# --- Demo / simple tests ---
if __name__ == "__main__":
    # Example 1
    root = build_tree_level([5,3,8,1,4,7,9,None,2])
    print(lowest_common_ancestor_bst_iter(root, 3, 8).val)  # Expected 5

    # Example 2
    root = build_tree_level([5,3,8,1,4,7,9,None,2])
    print(lowest_common_ancestor_bst_iter(root, 3, 4).val)  # Expected 3
