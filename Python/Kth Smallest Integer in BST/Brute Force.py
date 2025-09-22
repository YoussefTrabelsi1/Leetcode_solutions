# filename: brute_sort.py

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list (use None for missing nodes)."""
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for left_val, right_val in zip(it, it):
        node = q.popleft()
        if left_val is not None:
            node.left = TreeNode(left_val)
            q.append(node.left)
        if right_val is not None:
            node.right = TreeNode(right_val)
            q.append(node.right)
    # If odd count, handle last leftover child
    remaining = list(it)
    if remaining and q:
        val = remaining[0]
        if val is not None:
            q[0].left = TreeNode(val)
    return root

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    BRUTE FORCE:
    Collect all values (ignoring BST property), sort, return k-th (1-indexed).
    Time: O(n log n), Space: O(n)
    """
    vals = []
    if not root:
        return -1
    q = deque([root])
    while q:
        node = q.popleft()
        vals.append(node.val)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    vals.sort()
    return vals[k - 1]

if __name__ == "__main__":
    # Example 1
    root = build_tree([2, 1, 3])
    print(kth_smallest(root, 1))  # Expected: 1

    # Example 2
    root = build_tree([4, 3, 5, 2, None])
    print(kth_smallest(root, 4))  # Expected: 5
