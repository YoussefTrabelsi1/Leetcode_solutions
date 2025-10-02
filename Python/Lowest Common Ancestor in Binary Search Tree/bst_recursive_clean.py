# Recursive LCA using BST property
# Time: O(h), Space: O(h) due to recursion stack (worst case skewed tree)

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

def lowest_common_ancestor_bst_rec(root: TreeNode, p_val: int, q_val: int) -> TreeNode:
    lo, hi = (p_val, q_val) if p_val < q_val else (q_val, p_val)
    def rec(node: TreeNode) -> TreeNode:
        if lo < node.val and hi < node.val:
            return rec(node.left)
        if lo > node.val and hi > node.val:
            return rec(node.right)
        return node  # split point or one equals node
    return rec(root)

# --- Demo / simple tests ---
if __name__ == "__main__":
    # Example 1
    root = build_tree_level([5,3,8,1,4,7,9,None,2])
    print(lowest_common_ancestor_bst_rec(root, 3, 8).val)  # Expected 5

    # Example 2
    root = build_tree_level([5,3,8,1,4,7,9,None,2])
    print(lowest_common_ancestor_bst_rec(root, 3, 4).val)  # Expected 3
