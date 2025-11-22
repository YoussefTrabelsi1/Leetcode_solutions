# file: brute_force_subtree.py

from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val: int = 0,
                 left: Optional["TreeNode"] = None,
                 right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(level: List[Optional[int]]) -> Optional[TreeNode]:
    """
    Build a binary tree from level-order list representation.
    Example: [1,2,3,None,4] -> tree with root=1, etc.
    """
    if not level:
        return None
    it = iter(level)
    root = TreeNode(next(it))
    q = deque([root])

    for v in it:
        node = q.popleft()
        # left child
        if v is not None:
            node.left = TreeNode(v)
            q.append(node.left)
        # right child (may or may not exist)
        try:
            v = next(it)
        except StopIteration:
            break
        if v is not None:
            node.right = TreeNode(v)
            q.append(node.right)
    return root


def is_same_tree(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
    """Check if two trees are structurally identical with same values."""
    if not a and not b:
        return True
    if not a or not b:
        return False
    if a.val != b.val:
        return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)


def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    """
    Brute-force:
    For every node in `root`, check if the subtree rooted there equals `subRoot`.
    Time: O(N * M) worst case
    Space: O(H), recursion stack
    """
    if not subRoot:
        # Empty tree is always subtree
        return True
    if not root:
        return False

    # Check current node
    if is_same_tree(root, subRoot):
        return True

    # Or look in left / right subtrees
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)


if __name__ == "__main__":
    # Example 1
    root = build_tree([1, 2, 3, 4, 5])
    sub = build_tree([2, 4, 5])
    print(is_subtree(root, sub))  # True

    # Example 2
    root2 = build_tree([1, 2, 3, 4, 5, None, None, 6])
    sub2 = build_tree([2, 4, 5])
    print(is_subtree(root2, sub2))  # False
