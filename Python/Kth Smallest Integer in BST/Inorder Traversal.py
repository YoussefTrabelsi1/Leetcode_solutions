# filename: inorder_list.py

from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    """Builds a binary tree from a level-order list (use None for missing nodes)."""
    from collections import deque
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
    remaining = list(it)
    if remaining and q:
        val = remaining[0]
        if val is not None:
            q[0].left = TreeNode(val)
    return root

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    INORDER (build full sorted list):
    Uses the BST property: inorder returns sorted values.
    Time: O(n), Space: O(n)
    """
    def inorder(node: Optional[TreeNode], out: List[int]) -> None:
        if not node:
            return
        inorder(node.left, out)
        out.append(node.val)
        inorder(node.right, out)

    arr: List[int] = []
    inorder(root, arr)
    return arr[k - 1]

if __name__ == "__main__":
    # Example 1
